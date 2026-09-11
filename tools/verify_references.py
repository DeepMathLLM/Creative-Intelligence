#!/usr/bin/env python3
"""Deterministic reference verification for mathematical object origin archives.

The archive runner's acceptance gate verifies historical accuracy with a model
review call. This tool adds the deterministic layer underneath it: every
numbered source in the archive's ``Sources`` section is checked for structural
consistency and against external bibliographic indexes (Crossref, OpenAlex,
zbMATH Open, the Internet Archive, and Open Library), so that fabricated or
miscopied references are caught before any model review runs.

Checks, in order:

L0  structure (offline): contiguous ``[n]`` numbering, every in-text citation
    resolves to a listed source, no orphan entries (warning only).
L1  existence: each source is resolved against the indexes above. A confident
    match requires title similarity AND surname overlap (when both sides give
    authors) AND a year within +-2 (when both sides give years).
L2  link liveness: DOIs and URLs must resolve (warning only by default;
    escalate with ``--strict``).
L3  consistency: bibliographic details claimed in the entry (year, volume,
    pages) are compared with the matched records. Claims contradicted by
    every matched record are failures; disagreement between the indexes
    themselves is reported as a warning.

The tool never decides whether a source *supports* a claim; that remains the
job of the model review in ``verify_math_object_origin_archive``.

Network access goes through an injectable fetcher with a JSON cache, so tests
run fully offline and ``--offline`` mode is CI-safe.

Exit codes: 0 = pass, 1 = at least one failure, 2 = usage/IO error.
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

USER_AGENT = (
    "CreativeIntelligence-ReferenceVerifier/0.1 "
    "(https://github.com/DeepMathLLM/Creative-Intelligence)"
)
YEAR_TOLERANCE = 2
TITLE_RATIO_THRESHOLD = 0.72
TITLE_JACCARD_THRESHOLD = 0.60
DOI_TITLE_RATIO_THRESHOLD = 0.60  # sanity floor when the DOI itself is exact

YEAR_LIKE = lambda value: 1500 <= value <= 2029  # noqa: E731
INITIALS_RE = re.compile(r"^(?:[A-Z]\.)+(?:-[A-Z]\.)*$")

DOI_RE = re.compile(r"\b10\.\d{4,9}/[^\s\"'<>]+")
URL_RE = re.compile(r"https?://[^\s\"'<>]+")
YEAR_RE = re.compile(r"\b(1[5-9]\d\d|20[0-2]\d)\b")
ENTRY_RE = re.compile(r"^\[(\d+)\]\s*(.*)$")
CITATION_RE = re.compile(r"\[(\d{1,3})\]")
PAGE_RANGE_RE = re.compile(r"\b(\d{1,5})\s*[\u2013\u2014-]\s*(\d{1,5})\b")
VOLUME_YEAR_RE = re.compile(r"\b(\d{1,4})\s*\((?:1[5-9]\d\d|20[0-2]\d)\)")
BOLD_VOLUME_RE = re.compile(r"\*\*(\d{1,4})\*\*")


# --------------------------------------------------------------------------
# Parsing
# --------------------------------------------------------------------------

@dataclass
class ReferenceEntry:
    index: int
    raw: str
    doi: Optional[str] = None
    urls: List[str] = field(default_factory=list)
    year: Optional[int] = None
    volume: Optional[str] = None
    pages: Optional[str] = None
    title_guess: Optional[str] = None
    surnames: frozenset = frozenset()
    book_hint: bool = False


BOOK_HINTS = (
    "birkhäuser", "springer", "addison-wesley", "cambridge university press",
    "gauthier-villars", "princeton university press", "progress in mathematics",
    "lecture notes in mathematics", "graduate texts in mathematics",
    "astérisque", "interscience", "academic press", "nelson and sons",
    "dover", "clarendon", "prentice hall", "wiley", "ams chelsea",
)


def find_sources_section(text: str, heading: str) -> Tuple[str, Optional[str]]:
    """Split archive text into (body, sources-section-text).

    The heading line is ``## <name>`` optionally preceded by a section number,
    matching the canonical archive template ("## 4. Sources").
    """
    pattern = re.compile(
        r"^##\s+(?:\d+\.?\s*)?" + re.escape(heading) + r"\s*$", re.IGNORECASE | re.MULTILINE
    )
    match = pattern.search(text)
    if not match:
        return text, None
    return text[: match.start()], text[match.end():]


def _looks_like_author_part(part: str) -> bool:
    """Heuristic: a comma-separated citation segment that is (part of) an
    author list, e.g. "O.-H. Keller", "H. Bass", "and D. Wright", "Gauss"."""
    words = [
        w
        for w in re.split(r"\s+", part)
        if w and w.lower() not in {"and", "&", "et", "al.", "with"}
    ]
    if not words or len(words) > 6:
        return False
    if not all(w[0].isupper() or not w[0].isalpha() for w in words):
        return False
    if any(INITIALS_RE.match(w) or re.fullmatch(r"[A-Z]\.?", w) for w in words):
        return True
    return len(words) <= 1


def _strip_markup(text: str) -> str:
    text = URL_RE.sub(" ", text)
    text = DOI_RE.sub(" ", text)
    return text


def guess_title(text: str) -> Optional[str]:
    """Best-effort title extraction from a free-form reference entry."""
    plain = _strip_markup(text)
    italics = re.findall(r"\*([^*]{4,}?)\*", plain) or re.findall(r"_([^_]{4,}?)_", plain)
    if italics:
        return max(italics, key=len).strip()
    year_match = YEAR_RE.search(plain)
    head = (plain[: year_match.start()] if year_match else plain).strip().rstrip(".")
    parts = [p.strip(" ,") for p in head.split(",") if p.strip(" ,")]
    candidates = [
        p for p in parts if len(p.split()) >= 2 and not _looks_like_author_part(p)
    ]
    if candidates:
        return max(candidates, key=len)
    longer = [p for p in parts if len(p.split()) >= 2]
    return max(longer, key=len) if longer else None


def guess_year(text: str) -> Optional[int]:
    paren = re.search(r"\((1[5-9]\d\d|20[0-2]\d)\)", text)
    if paren:
        return int(paren.group(1))
    bare = YEAR_RE.search(text)
    return int(bare.group(1)) if bare else None


def guess_surnames(text: str) -> frozenset:
    """Extract candidate author surnames from the segment before the title."""
    plain = _strip_markup(text)
    title = guess_title(text)
    head = plain
    if title:
        pos = plain.find(title)
        if pos > 0:
            head = plain[:pos]
    head = re.sub(r"[*_]", " ", head)
    stop = {
        "on", "the", "a", "an", "of", "in", "und", "sur", "des", "der", "die",
        "das", "and", "et", "al", "with", "for", "von", "van", "den", "de",
        "la", "le", "les", "di", "da",
    }
    surnames = set()
    for token in re.split(r"[\s,()]+", head):
        if INITIALS_RE.match(token) or INITIALS_RE.match(token + "."):
            continue  # bare initials such as "O.-H." are not surnames
        token = token.strip(".;:")
        if (
            len(token) >= 2
            and token[0].isupper()
            and token.lower() not in stop
            and any(c.isalpha() for c in token)
            and not re.fullmatch(r"[A-Z]", token)
        ):
            surnames.add(token.lower())
    return frozenset(surnames)


def guess_pages(text: str) -> Optional[str]:
    for start, end in reversed(PAGE_RANGE_RE.findall(text)):
        # skip life-date ranges like "1838-1922" and other year-like spans
        if YEAR_LIKE(int(start)) and YEAR_LIKE(int(end)):
            continue
        return "%d-%d" % (int(start), int(end))
    return None


def guess_volume(text: str) -> Optional[str]:
    match = VOLUME_YEAR_RE.search(text) or BOLD_VOLUME_RE.search(text)
    return match.group(1) if match else None


def _clean_token(token: str) -> str:
    """Strip trailing punctuation, keeping balanced parentheses (DOIs/URLs
    such as 10.1016/0040-9383(87)90009-7 legitimately contain them)."""
    token = token.rstrip(".,;:")
    while token.endswith((")", "]")) and token.count("(") < token.count(")"):
        token = token[:-1]
    while token.endswith("]") and token.count("[") < token.count("]"):
        token = token[:-1]
    return token


def parse_entries(section_text: str) -> List[ReferenceEntry]:
    entries: List[Tuple[int, str]] = []
    current_index: Optional[int] = None
    current_lines: List[str] = []
    for line in section_text.splitlines():
        match = ENTRY_RE.match(line.strip())
        if match:
            if current_index is not None:
                entries.append((current_index, " ".join(current_lines).strip()))
            current_index = int(match.group(1))
            current_lines = [match.group(2).strip()]
        elif current_index is not None and line.strip():
            current_lines.append(line.strip())
    if current_index is not None:
        entries.append((current_index, " ".join(current_lines).strip()))

    parsed: List[ReferenceEntry] = []
    for index, raw in entries:
        doi_match = DOI_RE.search(raw)
        doi = _clean_token(doi_match.group(0)).lower() if doi_match else None
        clean = _strip_markup(raw)  # bibliographic hints must not read DOIs/URLs
        parsed.append(
            ReferenceEntry(
                index=index,
                raw=raw,
                doi=doi,
                urls=[_clean_token(u) for u in URL_RE.findall(raw)],
                year=guess_year(clean),
                volume=guess_volume(clean),
                pages=guess_pages(clean),
                title_guess=guess_title(raw),
                surnames=guess_surnames(raw),
                book_hint=any(hint in raw.lower() for hint in BOOK_HINTS),
            )
        )
    return parsed


def check_structure(body: str, entries: Sequence[ReferenceEntry]) -> Tuple[List[str], List[str]]:
    """L0 checks. Returns (issues, warnings)."""
    issues: List[str] = []
    warnings: List[str] = []
    indices = [entry.index for entry in entries]
    if len(set(indices)) != len(indices):
        issues.append("duplicate source numbers: %s" % sorted(indices))
    expected = list(range(1, len(indices) + 1))
    if sorted(indices) != expected:
        issues.append(
            "source numbering is not contiguous from 1: found %s" % sorted(indices)
        )
    listed = set(indices)
    cited = {int(n) for n in CITATION_RE.findall(body)}
    dangling = sorted(n for n in cited if n not in listed)
    if dangling:
        issues.append("in-text citations with no matching source entry: %s" % dangling)
    orphans = sorted(n for n in listed if n not in cited)
    if orphans:
        warnings.append("source entries never cited in the text: %s" % orphans)
    for entry in entries:
        if not entry.doi and not entry.title_guess:
            issues.append(
                "source [%d] has neither a DOI nor a recognizable title; "
                "it cannot be machine-verified" % entry.index
            )
    return issues, warnings


# --------------------------------------------------------------------------
# Fetching (injectable, cacheable, offline-capable)
# --------------------------------------------------------------------------

class FetchError(RuntimeError):
    pass


class CacheMiss(FetchError):
    pass


class HttpFetcher:
    """Network fetcher. Replaceable in tests."""

    def __init__(self, timeout: float = 20.0, mailto: Optional[str] = None):
        self.timeout = timeout
        self.mailto = mailto

    def get_json(self, url: str) -> dict:
        if self.mailto and "api.crossref.org" in url:
            sep = "&" if "?" in url else "?"
            url = "%s%smailto=%s" % (url, sep, urllib.parse.quote(self.mailto))
        request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                return json.loads(response.read().decode("utf-8"))
        except (urllib.error.URLError, OSError, ValueError) as exc:
            raise FetchError("GET %s failed: %s" % (url, exc)) from exc

    def check_link(self, url: str) -> int:
        """Return an HTTP status code; 0 means the host could not be reached."""
        for method in ("HEAD", "GET"):
            request = urllib.request.Request(
                url, method=method, headers={"User-Agent": USER_AGENT}
            )
            try:
                with urllib.request.urlopen(request, timeout=self.timeout) as response:
                    return int(response.status)
            except urllib.error.HTTPError as exc:
                if exc.code in (403, 405, 501) and method == "HEAD":
                    continue  # some servers reject HEAD; retry with GET
                return int(exc.code)
            except (urllib.error.URLError, OSError):
                return 0
        return 0


class CacheFetcher:
    """JSON-file cache wrapper around another fetcher."""

    def __init__(self, inner, cache_path: Path, offline: bool = False):
        self.inner = inner
        self.cache_path = Path(cache_path)
        self.offline = offline
        self._data: Dict[str, dict] = {"json": {}, "links": {}}
        if self.cache_path.exists():
            try:
                loaded = json.loads(self.cache_path.read_text(encoding="utf-8"))
                if isinstance(loaded, dict):
                    self._data["json"].update(loaded.get("json") or {})
                    self._data["links"].update(loaded.get("links") or {})
            except (ValueError, OSError):
                pass  # a corrupt cache must never crash a verification run

    @staticmethod
    def _key(url: str) -> str:
        return hashlib.sha256(url.encode("utf-8")).hexdigest()

    def get_json(self, url: str) -> dict:
        key = self._key(url)
        if key in self._data["json"]:
            return self._data["json"][key]
        if self.offline:
            raise CacheMiss("offline: no cached response for %s" % url)
        payload = self.inner.get_json(url)
        self._data["json"][key] = payload
        return payload

    def check_link(self, url: str) -> int:
        key = self._key(url)
        if key in self._data["links"]:
            return int(self._data["links"][key])
        if self.offline:
            return -1  # unknown under --offline; reported as a warning
        status = self.inner.check_link(url)
        self._data["links"][key] = status
        return status

    def save(self) -> None:
        self.cache_path.write_text(
            json.dumps(self._data, ensure_ascii=False, indent=1, sort_keys=True),
            encoding="utf-8",
        )


# --------------------------------------------------------------------------
# Bibliographic resolvers
# --------------------------------------------------------------------------

@dataclass
class BiblioMatch:
    source: str
    title: Optional[str] = None
    surnames: frozenset = frozenset()
    year: Optional[int] = None
    volume: Optional[str] = None
    pages: Optional[str] = None
    container: Optional[str] = None
    identifier: Optional[str] = None
    doc_type: Optional[str] = None


def _normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text, flags=re.UNICODE)
    return re.sub(r"\s+", " ", text).strip()


def _title_score(claimed: str, found: str) -> Tuple[float, float]:
    """Return (difflib ratio, token Jaccard) on normalized titles."""
    a, b = _normalize(claimed), _normalize(found)
    ratio = difflib.SequenceMatcher(None, a, b).ratio()
    tokens_a, tokens_b = set(a.split()), set(b.split())
    jaccard = (
        len(tokens_a & tokens_b) / len(tokens_a | tokens_b) if tokens_a and tokens_b else 0.0
    )
    return ratio, jaccard


def _title_ok(claimed: Optional[str], found: Optional[str], threshold: float) -> bool:
    if not claimed:
        return True  # nothing parsed to compare against
    if not found:
        return False  # a title-less record can never confirm a claimed title
    ratio, jaccard = _title_score(claimed, found)
    return ratio >= threshold or jaccard >= TITLE_JACCARD_THRESHOLD


def _surname_ok(claimed: frozenset, found: frozenset) -> bool:
    if not claimed or not found:
        return True  # cannot check -> do not penalize
    return bool(claimed & found)


def _year_ok(claimed: Optional[int], found: Optional[int]) -> bool:
    if claimed is None or found is None:
        return True
    return abs(claimed - found) <= YEAR_TOLERANCE


def _last_token_surname(name: str) -> Optional[str]:
    """Best-effort surname from a display name or 'Family, Given' string."""
    name = re.sub(r"\b\d{4}\b.*", "", name)  # drop life dates (archive.org style)
    if "," in name:
        candidate = name.split(",", 1)[0].strip()
    else:
        parts = [p for p in name.split() if not re.fullmatch(r"(?:[A-Z]\.)+", p)]
        candidate = parts[-1] if parts else ""
    candidate = candidate.strip(" .")
    return candidate.lower() if len(candidate) >= 2 else None


def _record_ok(entry: ReferenceEntry, match: BiblioMatch, threshold: float) -> bool:
    return (
        _title_ok(entry.title_guess, match.title, threshold)
        and _surname_ok(entry.surnames, match.surnames)
        and _year_ok(entry.year, match.year)
    )


# --- Crossref ---------------------------------------------------------------

def _surname_variants(family: str) -> frozenset:
    """Crossref family fields sometimes carry initials ("H. Kauffman");
    keep both the full string and its final token as match candidates."""
    family = family.strip()
    variants = {family.lower()} if family else set()
    last = _last_token_surname(family)
    if last:
        variants.add(last)
    return frozenset(variants)


def _crossref_record(item: dict) -> BiblioMatch:
    titles = item.get("title") or []
    authors = item.get("author") or []
    surnames = frozenset(
        variant for a in authors for variant in _surname_variants(str(a.get("family") or ""))
    )
    date_parts = (item.get("issued") or {}).get("date-parts") or [[None]]
    containers = item.get("container-title") or []
    title = str(titles[0]).split("†")[0].strip() if titles else None  # drop footnote marks
    return BiblioMatch(
        source="crossref",
        title=title,
        surnames=surnames,
        year=date_parts[0][0],
        volume=str(item.get("volume") or "") or None,
        pages=str(item.get("page") or "") or None,
        container=str(containers[0]) if containers else None,
        identifier=str(item.get("DOI") or "") or None,
        doc_type=str(item.get("type") or "") or None,
    )


def resolve_crossref_doi(fetcher, doi: str) -> Optional[BiblioMatch]:
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi)
    try:
        payload = fetcher.get_json(url)
    except FetchError as exc:
        if "404" in str(exc):
            return None
        raise
    message = payload.get("message") if isinstance(payload, dict) else None
    if not isinstance(message, dict):
        return None
    return _crossref_record(message)


def resolve_crossref_bibliographic(fetcher, entry: ReferenceEntry) -> Optional[BiblioMatch]:
    query = " ".join(
        part for part in [entry.title_guess or "", " ".join(sorted(entry.surnames))] if part
    ).strip()
    if not query:
        return None
    url = (
        "https://api.crossref.org/works?rows=3&query.bibliographic="
        + urllib.parse.quote(query)
    )
    payload = fetcher.get_json(url)
    items = ((payload or {}).get("message") or {}).get("items") or []
    for item in items:
        record = _crossref_record(item)
        if _record_ok(entry, record, TITLE_RATIO_THRESHOLD):
            return record
    return None


# --- OpenAlex ---------------------------------------------------------------

def _openalex_record(work: dict) -> BiblioMatch:
    surnames = frozenset(
        filter(
            None,
            (
                _last_token_surname(str((a.get("author") or {}).get("display_name") or ""))
                for a in work.get("authorships") or []
            ),
        )
    )
    biblio = work.get("biblio") or {}
    first, last = biblio.get("first_page"), biblio.get("last_page")
    pages = None
    if first and last:
        pages = "%s-%s" % (first, last)
    elif first:
        pages = str(first)
    source = ((work.get("primary_location") or {}).get("source") or {})
    doi = str(work.get("doi") or "")
    return BiblioMatch(
        source="openalex",
        title=work.get("display_name") or work.get("title"),
        surnames=surnames,
        year=work.get("publication_year"),
        volume=str(biblio.get("volume") or "") or None,
        pages=pages,
        container=source.get("display_name"),
        identifier=doi.replace("https://doi.org/", "") or None,
    )


def resolve_openalex_title(fetcher, entry: ReferenceEntry) -> Optional[BiblioMatch]:
    if not entry.title_guess:
        return None
    url = (
        "https://api.openalex.org/works?per-page=3&filter=title.search:"
        + urllib.parse.quote(entry.title_guess)
    )
    payload = fetcher.get_json(url)
    for work in (payload or {}).get("results") or []:
        record = _openalex_record(work)
        if _record_ok(entry, record, TITLE_RATIO_THRESHOLD):
            return record
    return None


def resolve_openalex_doi(fetcher, doi: str) -> Optional[BiblioMatch]:
    url = "https://api.openalex.org/works/doi:" + urllib.parse.quote(doi)
    try:
        payload = fetcher.get_json(url)
    except FetchError as exc:
        if "404" in str(exc):
            return None
        raise
    if not isinstance(payload, dict) or not payload.get("id"):
        return None
    return _openalex_record(payload)


# --- zbMATH Open (covers the mathematical literature back to 1868) -----------

def resolve_zbmath_title(fetcher, entry: ReferenceEntry) -> Optional[BiblioMatch]:
    if not entry.title_guess:
        return None
    url = (
        'https://api.zbmath.org/v1/document/_search?search_string=ti:"'
        + urllib.parse.quote(entry.title_guess)
        + '"'
    )
    payload = fetcher.get_json(url)
    for doc in (payload or {}).get("result") or []:
        title = ((doc.get("title") or {}).get("title")) or None
        authors = ((doc.get("contributors") or {}).get("authors")) or []
        surnames = frozenset(
            filter(None, (_last_token_surname(str(a.get("name") or "")) for a in authors))
        )
        source = doc.get("source") or {}
        series = (source.get("series") or [{}])
        year_raw = doc.get("year")
        try:
            year = int(str(year_raw)[:4]) if year_raw else None
        except ValueError:
            year = None
        record = BiblioMatch(
            source="zbmath",
            title=title,
            surnames=surnames,
            year=year,
            volume=None,
            pages=str(source.get("pages") or "") or None,
            container=(series[0] or {}).get("title") if series else None,
            identifier=str(doc.get("id") or "") or None,
        )
        if _record_ok(entry, record, TITLE_RATIO_THRESHOLD):
            return record
    return None


# --- Internet Archive / Open Library (books, including 19th-century) ---------

def resolve_archive_org(fetcher, entry: ReferenceEntry) -> Optional[BiblioMatch]:
    if not entry.title_guess:
        return None
    query = 'title:"%s"' % entry.title_guess.replace('"', "")
    url = (
        "https://archive.org/advancedsearch.php?rows=3&output=json"
        "&fl[]=title&fl[]=creator&fl[]=year&fl[]=identifier&q="
        + urllib.parse.quote(query)
    )
    payload = fetcher.get_json(url)
    docs = ((payload or {}).get("response") or {}).get("docs") or []
    for doc in docs:
        creator = doc.get("creator") or ""
        if isinstance(creator, list):
            creator = creator[0] if creator else ""
        year_raw = doc.get("year")
        try:
            year = int(str(year_raw)[:4]) if year_raw else None
        except ValueError:
            year = None
        record = BiblioMatch(
            source="archive.org",
            title=str(doc.get("title") or "") or None,
            surnames=frozenset(filter(None, [_last_token_surname(str(creator))])),
            year=year,
            identifier=str(doc.get("identifier") or "") or None,
        )
        if _record_ok(entry, record, TITLE_RATIO_THRESHOLD):
            return record
    return None


def resolve_openlibrary(fetcher, entry: ReferenceEntry) -> Optional[BiblioMatch]:
    if not entry.title_guess:
        return None
    url = (
        "https://openlibrary.org/search.json?limit=3"
        "&fields=title,author_name,first_publish_year,key&title="
        + urllib.parse.quote(entry.title_guess)
    )
    payload = fetcher.get_json(url)
    for doc in (payload or {}).get("docs") or []:
        record = BiblioMatch(
            source="openlibrary",
            title=str(doc.get("title") or "") or None,
            surnames=frozenset(
                filter(
                    None,
                    (
                        _last_token_surname(str(a))
                        for a in doc.get("author_name") or []
                    ),
                )
            ),
            year=doc.get("first_publish_year"),
            identifier=str(doc.get("key") or "") or None,
        )
        if _record_ok(entry, record, TITLE_RATIO_THRESHOLD):
            return record
    return None


# --------------------------------------------------------------------------
# Verification
# --------------------------------------------------------------------------

def _normalize_pages(pages: Optional[str]) -> Optional[str]:
    if not pages:
        return None
    normalized = pages.replace("\u2013", "-").replace("\u2014", "-")
    match = PAGE_RANGE_RE.search(normalized)
    if match:
        return "%d-%d" % (int(match.group(1)), int(match.group(2)))
    digits = re.fullmatch(r"\d{1,5}", normalized.strip())
    return normalized.strip() if digits else None


def verify_entry(
    fetcher, entry: ReferenceEntry, *, strict_links: bool = False
) -> Dict[str, object]:
    issues: List[str] = []
    warnings: List[str] = []
    matches: List[BiblioMatch] = []

    try:
        if entry.doi:
            crossref = resolve_crossref_doi(fetcher, entry.doi)
            if crossref is None:
                issues.append("DOI %s does not resolve in Crossref" % entry.doi)
            else:
                if not _record_ok(entry, crossref, DOI_TITLE_RATIO_THRESHOLD):
                    issues.append(
                        "DOI %s resolves to '%s', which does not match the entry"
                        % (entry.doi, crossref.title)
                    )
                else:
                    matches.append(crossref)
                    openalex = resolve_openalex_doi(fetcher, entry.doi)
                    if openalex is not None and _record_ok(
                        entry, openalex, DOI_TITLE_RATIO_THRESHOLD
                    ):
                        matches.append(openalex)
        else:
            article_resolvers = (
                resolve_crossref_bibliographic,
                resolve_openalex_title,
                resolve_zbmath_title,
            )
            book_resolvers = (resolve_archive_org, resolve_openlibrary)
            # book-looking entries ask the book indexes first; journal hits for
            # a book title are typically different works sharing the title
            resolvers = (
                book_resolvers + article_resolvers
                if entry.book_hint
                else article_resolvers + book_resolvers
            )
            offline_misses = 0
            for resolver in resolvers:
                try:
                    match = resolver(fetcher, entry)
                except CacheMiss:
                    offline_misses += 1
                    continue  # under --offline an uncached index is skipped, not failed
                except FetchError:
                    continue  # one index being unreachable must not hide the others
                if match is not None:
                    matches.append(match)
                    break
            if not matches:
                if offline_misses:
                    issues.append(
                        "no confident match; %d index lookup(s) skipped "
                        "(--offline, not cached)" % offline_misses
                    )
                else:
                    issues.append(
                        "no matching bibliographic record found in Crossref, OpenAlex, "
                        "zbMATH Open, the Internet Archive, or Open Library"
                    )
    except FetchError as exc:
        issues.append("bibliographic lookup failed: %s" % exc)

    # L3: compare claimed bibliographic details against matched records.
    if matches and entry.year is not None:
        for match in matches:
            if match.year is not None and not _year_ok(entry.year, match.year):
                issues.append(
                    "stated year %s contradicts %s record (%s)"
                    % (entry.year, match.source, match.year)
                )
    if matches and entry.pages:
        claimed = _normalize_pages(entry.pages)
        claimed_start = claimed.split("-")[0] if claimed else None

        def corroborates(record_pages: Optional[str]) -> bool:
            normalized = _normalize_pages(record_pages)
            if not normalized or not claimed:
                return False
            if normalized == claimed:
                return True
            # many indexes record only the first page of an article
            return "-" not in normalized and normalized == claimed_start

        known = [m for m in matches if m.pages]
        if known and not any(corroborates(m.pages) for m in known):
            detail = ", ".join("%s: %s" % (m.source, m.pages) for m in known)
            issues.append("stated pages %s not corroborated (%s)" % (claimed, detail))
        first_pages = {
            (_normalize_pages(m.pages) or "").split("-")[0] for m in known
        }
        first_pages.discard("")
        if len(first_pages) > 1:
            warnings.append(
                "indexes disagree on the first page for this source: %s"
                % ", ".join("%s: %s" % (m.source, m.pages) for m in known)
            )
    if matches and entry.volume:
        # Volume corroboration only applies to journal articles; series
        # volumes of books/monographs are not comparable across indexes.
        articles = [m for m in matches if m.doc_type == "journal-article" and m.volume]
        if articles and all(str(m.volume) != str(entry.volume) for m in articles):
            detail = ", ".join("%s: vol. %s" % (m.source, m.volume) for m in articles)
            issues.append("stated volume %s not corroborated (%s)" % (entry.volume, detail))

    # L2: link liveness (warnings unless --strict).
    link_targets = list(dict.fromkeys(entry.urls))
    if entry.doi:
        doi_url = "https://doi.org/" + entry.doi
        if doi_url not in link_targets:
            link_targets.append(doi_url)
    for url in link_targets:
        try:
            status = fetcher.check_link(url)
        except FetchError:
            status = 0
        if status == -1:
            warnings.append("link not checked (--offline, not cached): %s" % url)
        elif status == 0 or status >= 400:
            message = "link unreachable (HTTP %s): %s" % (
                status if status else "no response",
                url,
            )
            (issues if strict_links else warnings).append(message)

    verdict = "fail" if issues else ("pass_with_warnings" if warnings else "pass")
    return {
        "index": entry.index,
        "verdict": verdict,
        "matched": [
            {
                "source": m.source,
                "title": m.title,
                "year": m.year,
                "container": m.container,
                "volume": m.volume,
                "pages": m.pages,
                "identifier": m.identifier,
            }
            for m in matches
        ],
        "issues": issues,
        "warnings": warnings,
        "parsed": {
            "doi": entry.doi,
            "year": entry.year,
            "volume": entry.volume,
            "pages": entry.pages,
            "title_guess": entry.title_guess,
        },
    }


def verify_archive_text(
    fetcher,
    text: str,
    *,
    heading: str = "Sources",
    strict_links: bool = False,
) -> Dict[str, object]:
    body, section = find_sources_section(text, heading)
    if section is None:
        raise ValueError("no '## %s' section found in the archive" % heading)
    entries = parse_entries(section)
    issues, warnings = check_structure(body, entries)
    if not entries:
        issues.append("the Sources section lists no entries")
    reports = [
        verify_entry(fetcher, entry, strict_links=strict_links) for entry in entries
    ]
    for report in reports:
        for issue in report["issues"]:
            issues.append("[%d] %s" % (report["index"], issue))
        for warning in report["warnings"]:
            warnings.append("[%d] %s" % (report["index"], warning))
    verdict = "fail" if issues else ("pass_with_warnings" if warnings else "pass")
    return {
        "verdict": verdict,
        "issues": issues,
        "warnings": warnings,
        "sources_checked": len(entries),
        "entries": reports,
        "summary": "%d source(s) checked, %d issue(s), %d warning(s)"
        % (len(entries), len(issues), len(warnings)),
    }


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def _build_fetcher(args) -> CacheFetcher:
    return CacheFetcher(
        HttpFetcher(timeout=args.timeout, mailto=args.mailto),
        cache_path=Path(args.cache_file),
        offline=args.offline,
    )


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Deterministically verify the numbered sources of a mathematical "
            "object origin archive against external bibliographic indexes."
        )
    )
    parser.add_argument("archives", nargs="+", help="archive Markdown file(s)")
    parser.add_argument(
        "--heading",
        default="Sources",
        help="name of the sources section heading (default: Sources)",
    )
    parser.add_argument("--json", action="store_true", help="print the JSON report")
    parser.add_argument(
        "--offline",
        action="store_true",
        help="use only the local cache; no network access (CI-safe)",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="treat unreachable links as failures instead of warnings",
    )
    parser.add_argument(
        "--cache-file",
        default=".reference-cache.json",
        help="JSON cache location (default: .reference-cache.json)",
    )
    parser.add_argument("--timeout", type=float, default=20.0)
    parser.add_argument(
        "--mailto",
        default=None,
        help="contact address for the Crossref polite pool (optional)",
    )
    args = parser.parse_args(argv)

    fetcher = _build_fetcher(args)
    worst = 0
    for archive_path in args.archives:
        path = Path(archive_path)
        if not path.is_file():
            print("error: no such file: %s" % path, file=sys.stderr)
            worst = max(worst, 2)
            continue
        text = path.read_text(encoding="utf-8")
        try:
            report = verify_archive_text(
                fetcher, text, heading=args.heading, strict_links=args.strict
            )
        except ValueError as exc:
            print("error: %s: %s" % (path, exc), file=sys.stderr)
            worst = max(worst, 2)
            continue
        if args.json:
            print(json.dumps({"file": str(path), **report}, ensure_ascii=False, indent=1))
        else:
            print("%s: %s" % (path, report["summary"]))
            for issue in report["issues"]:
                print("  ISSUE   %s" % issue)
            for warning in report["warnings"]:
                print("  warning %s" % warning)
            print("  verdict: %s" % report["verdict"])
        if report["verdict"] == "fail":
            worst = max(worst, 1)
    fetcher.save()
    return worst


if __name__ == "__main__":
    sys.exit(main())
