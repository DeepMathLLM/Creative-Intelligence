"""Offline regression tests for tools/verify_references.py.

All bibliographic fixtures are trimmed copies of real API responses captured
from Crossref, OpenAlex, zbMATH Open, the Internet Archive, and Open Library.
No network access, Moonshine runtime, or credentials are required.
"""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))

import verify_references as vr  # noqa: E402


# ---------------------------------------------------------------------------
# Real-response fixtures (trimmed to the fields the resolvers consume)
# ---------------------------------------------------------------------------

CROSSREF_KELLER = {
    "message": {
        "title": ["Ganze Cremona-Transformationen"],
        "author": [{"given": "Ott-Heinrich", "family": "Keller"}],
        "issued": {"date-parts": [[1939, 12]]},
        "container-title": ["Monatshefte für Mathematik und Physik"],
        "volume": "47",
        "page": "299-306",
        "DOI": "10.1007/bf01695502",
        "type": "journal-article",
    }
}

OPENALEX_KELLER = {
    "id": "W2051631976",
    "display_name": "Ganze Cremona-Transformationen",
    "publication_year": 1939,
    "doi": "https://doi.org/10.1007/bf01695502",
    "authorships": [{"author": {"display_name": "Ott-Heinrich Keller"}}],
    "biblio": {"volume": "47", "issue": "1", "first_page": "299", "last_page": "306"},
    "primary_location": {"source": {"display_name": "Monatshefte für Mathematik"}},
}

CROSSREF_ALON_QUERY = {
    "message": {
        "items": [
            {
                "title": ["Combinatorial Nullstellensatz"],
                "author": [{"given": "Noga", "family": "Alon"}],
                "issued": {"date-parts": [[1999]]},
                "container-title": ["Combinatorics, Probability and Computing"],
                "volume": "8",
                "page": "7-29",
                "DOI": "10.1017/s0963548398003411",
            }
        ]
    }
}

ZBMATH_KELLER = {
    "result": [
        {
            "title": {"title": "Ganze Cremona-Transformationen."},
            "contributors": {"authors": [{"name": "Keller, O.-H."}]},
            "year": "1939",
            "source": {
                "pages": "299-306",
                "series": [{"title": "Monatshefte für Mathematik und Physik"}],
            },
            "id": "63.0929.02",
        }
    ]
}

ARCHIVE_ORG_JORDAN = {
    "response": {
        "docs": [
            {
                "creator": "Jordan, Camille, 1838-1922",
                "identifier": "traitdessubsti00jorduoft",
                "title": "Traité des substitutions et des équations algébriques",
                "year": 1870,
            }
        ]
    }
}

OPENLIBRARY_DUDENEY = {
    "docs": [
        {
            "author_name": ["Henry Ernest Dudeney"],
            "first_publish_year": 1917,
            "key": "/works/OL1120335W",
            "title": "Amusements in mathematics",
        }
    ]
}

EMPTY_CROSSREF = {"message": {"items": []}}
EMPTY_OPENALEX = {"results": []}
EMPTY_ZBMATH = {"result": []}
EMPTY_ARCHIVE_ORG = {"response": {"docs": []}}
EMPTY_OPENLIBRARY = {"docs": []}


class FakeFetcher:
    """Substring-matched fixture fetcher; no network."""

    def __init__(self, routes=None, links=None):
        self.routes = list(routes or [])
        self.links = dict(links or {})

    def get_json(self, url):
        for needle, payload in self.routes:
            if needle in url:
                if isinstance(payload, Exception):
                    raise payload
                return payload
        if "api.crossref.org/works/" in url and "query" not in url:
            raise vr.FetchError("GET %s failed: HTTP Error 404" % url)
        raise vr.FetchError("GET %s failed: connection refused" % url)

    def check_link(self, url):
        return self.links.get(url, 200)


FULL_ROUTES = [
    ("api.crossref.org/works/10.1007", CROSSREF_KELLER),
    ("api.crossref.org/works?", CROSSREF_ALON_QUERY),
    ("api.openalex.org/works/doi:10.1007", OPENALEX_KELLER),
    ("api.openalex.org", EMPTY_OPENALEX),
    ("api.zbmath.org", ZBMATH_KELLER),
    ("archive.org", ARCHIVE_ORG_JORDAN),
    ("openlibrary.org", OPENLIBRARY_DUDENEY),
]


def make_archive(sources_block: str, body: str = "") -> str:
    header = body or (
        "# Mathematical Object Origin Archive | Test Object\n\n"
        "## 2. Core Record\n\nAs documented in [1].\n"
    )
    return header + "\n## 4. Sources\n\n" + sources_block + "\n"


KELLER_ENTRY = (
    "[1] O.-H. Keller, *Ganze Cremona-Transformationen*, Monatshefte für "
    "Mathematik und Physik 47 (1939), 299–306. https://doi.org/10.1007/bf01695502"
)


# ---------------------------------------------------------------------------
# Parsing and L0 structure
# ---------------------------------------------------------------------------

class ParsingTests(unittest.TestCase):
    def test_parse_keller_entry(self):
        (entry,) = vr.parse_entries(KELLER_ENTRY)
        self.assertEqual(entry.index, 1)
        self.assertEqual(entry.doi, "10.1007/bf01695502")
        self.assertEqual(entry.year, 1939)
        self.assertEqual(entry.volume, "47")
        self.assertEqual(entry.pages, "299-306")
        self.assertEqual(entry.title_guess, "Ganze Cremona-Transformationen")
        self.assertIn("keller", entry.surnames)
        self.assertNotIn("o.-h", entry.surnames)  # initials must not be surnames

    def test_guess_pages_ignores_life_dates(self):
        text = "C. Jordan (1838–1922), *Traité des substitutions*, Paris, 1870, pp. 1–5."
        self.assertEqual(vr.guess_pages(text), "1-5")

    def test_multiline_entry_is_joined(self):
        entries = vr.parse_entries("[1] First part,\n   second part (1939).\n\n[2] Other.")
        self.assertEqual(len(entries), 2)
        self.assertIn("second part", entries[0].raw)

    def test_missing_sources_section(self):
        with self.assertRaises(ValueError):
            vr.verify_archive_text(FakeFetcher(), "# Archive\n\nno sections here\n")

    def test_noncontiguous_numbering_fails(self):
        report = vr.verify_archive_text(
            FakeFetcher(FULL_ROUTES),
            make_archive(KELLER_ENTRY.replace("[1]", "[2]")),
        )
        self.assertEqual(report["verdict"], "fail")
        self.assertTrue(any("contiguous" in i for i in report["issues"]))

    def test_dangling_intext_citation_fails(self):
        body = "# A\n\nSee [1] and [7].\n"
        report = vr.verify_archive_text(
            FakeFetcher(FULL_ROUTES), make_archive(KELLER_ENTRY, body=body)
        )
        self.assertEqual(report["verdict"], "fail")
        self.assertTrue(any("no matching source entry" in i for i in report["issues"]))

    def test_uncited_entry_warns_only(self):
        body = "# A\n\nNo citations here.\n"
        report = vr.verify_archive_text(
            FakeFetcher(FULL_ROUTES), make_archive(KELLER_ENTRY, body=body)
        )
        self.assertEqual(report["verdict"], "pass_with_warnings")
        self.assertTrue(any("never cited" in w for w in report["warnings"]))


# ---------------------------------------------------------------------------
# L1/L3 existence and consistency
# ---------------------------------------------------------------------------

class VerificationTests(unittest.TestCase):
    def test_doi_route_verified_against_both_indexes(self):
        report = vr.verify_archive_text(FakeFetcher(FULL_ROUTES), make_archive(KELLER_ENTRY))
        self.assertEqual(report["verdict"], "pass", report["issues"])
        matched = report["entries"][0]["matched"]
        self.assertEqual({m["source"] for m in matched}, {"crossref", "openalex"})

    def test_wrong_doi_fails(self):
        entry = (
            "[1] B. Smith, *Entirely Different Paper*, J. Imaginary 1 (2001), 1–9. "
            "https://doi.org/10.1007/bf01695502"
        )
        report = vr.verify_archive_text(FakeFetcher(FULL_ROUTES), make_archive(entry))
        self.assertEqual(report["verdict"], "fail")
        self.assertTrue(any("does not match" in i for i in report["issues"]))

    def test_fabricated_reference_fails(self):
        entry = (
            "[1] Q. Nobody, *On the chromatic theory of imaginary knots*, "
            "J. Fabricated Math. 12 (1985), 1–15."
        )
        empty_routes = [
            ("api.crossref.org", EMPTY_CROSSREF),
            ("api.openalex.org", EMPTY_OPENALEX),
            ("api.zbmath.org", EMPTY_ZBMATH),
            ("archive.org", EMPTY_ARCHIVE_ORG),
            ("openlibrary.org", EMPTY_OPENLIBRARY),
        ]
        report = vr.verify_archive_text(FakeFetcher(empty_routes), make_archive(entry))
        self.assertEqual(report["verdict"], "fail")
        self.assertTrue(any("no matching bibliographic record" in i for i in report["issues"]))

    def test_stated_pages_contradicted_fail(self):
        entry = KELLER_ENTRY.replace("299–306", "229–306")
        report = vr.verify_archive_text(FakeFetcher(FULL_ROUTES), make_archive(entry))
        self.assertEqual(report["verdict"], "fail")
        self.assertTrue(any("not corroborated" in i for i in report["issues"]))

    def test_index_page_disagreement_warns(self):
        openalex_variant = dict(OPENALEX_KELLER)
        openalex_variant["biblio"] = {"volume": "47", "first_page": "229", "last_page": "306"}
        routes = [
            ("api.crossref.org/works/10.1007", CROSSREF_KELLER),
            ("api.openalex.org/works/doi:10.1007", openalex_variant),
        ]
        report = vr.verify_archive_text(FakeFetcher(routes), make_archive(KELLER_ENTRY))
        self.assertEqual(report["verdict"], "pass_with_warnings")
        self.assertTrue(any("disagree on the first page" in w for w in report["warnings"]))

    def test_bibliographic_route_without_doi(self):
        entry = (
            "[1] N. Alon, Combinatorial Nullstellensatz, Combin. Probab. "
            "Comput. 8 (1999), 7–29."
        )
        report = vr.verify_archive_text(FakeFetcher(FULL_ROUTES), make_archive(entry))
        self.assertEqual(report["verdict"], "pass", report["issues"])
        self.assertEqual(report["entries"][0]["matched"][0]["source"], "crossref")

    def test_zbmath_route_for_old_journal_article(self):
        entry = (
            "[1] O.-H. Keller, Ganze Cremona-Transformationen, "
            "Monatsh. Math. Phys. 47 (1939), 299–306."
        )
        routes = [
            ("api.crossref.org", EMPTY_CROSSREF),
            ("api.openalex.org", EMPTY_OPENALEX),
            ("api.zbmath.org", ZBMATH_KELLER),
        ]
        report = vr.verify_archive_text(FakeFetcher(routes), make_archive(entry))
        self.assertEqual(report["verdict"], "pass", report["issues"])
        self.assertEqual(report["entries"][0]["matched"][0]["source"], "zbmath")

    def test_book_routes(self):
        jordan = "[1] C. Jordan, *Traité des substitutions et des équations algébriques*, Paris, 1870."
        routes = [
            ("api.crossref.org", EMPTY_CROSSREF),
            ("api.openalex.org", EMPTY_OPENALEX),
            ("api.zbmath.org", EMPTY_ZBMATH),
            ("archive.org", ARCHIVE_ORG_JORDAN),
        ]
        report = vr.verify_archive_text(FakeFetcher(routes), make_archive(jordan))
        self.assertEqual(report["verdict"], "pass", report["issues"])
        self.assertEqual(report["entries"][0]["matched"][0]["source"], "archive.org")

        dudeney = "[1] H. E. Dudeney, *Amusements in Mathematics*, London, 1917."
        routes.append(("openlibrary.org", OPENLIBRARY_DUDENEY))
        report = vr.verify_archive_text(
            FakeFetcher([r for r in routes if "archive.org" not in r[0]]),
            make_archive(dudeney),
        )
        self.assertEqual(report["verdict"], "pass", report["issues"])
        self.assertEqual(report["entries"][0]["matched"][0]["source"], "openlibrary")


# ---------------------------------------------------------------------------
# L2 links, offline mode, cache, CLI
# ---------------------------------------------------------------------------

    def test_crossref_family_name_with_leading_initial(self):
        # real Crossref record: {"given": "Louis", "family": "H. Kauffman"}
        record = vr._crossref_record(
            {
                "title": ["State models and the jones polynomial"],
                "author": [{"given": "Louis", "family": "H. Kauffman"}],
                "issued": {"date-parts": [[1987]]},
                "DOI": "10.1016/0040-9383(87)90009-7",
                "type": "journal-article",
            }
        )
        entry = vr.parse_entries(
            "[2] L. H. Kauffman, *State models and the Jones polynomial*, "
            "Topology **26**(3) (1987), 395–407."
        )[0]
        self.assertTrue(vr._record_ok(entry, record, vr.DOI_TITLE_RATIO_THRESHOLD))

    def test_crossref_title_footnote_marks_are_stripped(self):
        record = vr._crossref_record(
            {
                "title": [
                    "Witten–Morse theory for cell complexes††Partially "
                    "supported by the National Science Foundation."
                ],
                "author": [{"family": "Forman"}],
                "issued": {"date-parts": [[1998]]},
                "type": "journal-article",
            }
        )
        self.assertEqual(record.title, "Witten–Morse theory for cell complexes")
        entry = vr.parse_entries(
            "[2] R. Forman, *Witten–Morse theory for cell complexes*, "
            "Topology **37**(5) (1998), 945–979."
        )[0]
        self.assertTrue(vr._record_ok(entry, record, vr.DOI_TITLE_RATIO_THRESHOLD))

    def test_book_hint_prefers_book_indexes(self):
        # the book and a same-titled journal article exist; the book hint
        # ("Birkhäuser") must route the entry to the book resolver first
        openlibrary_hit = {
            "docs": [
                {
                    "author_name": ["A. van den Essen"],
                    "first_publish_year": 2000,
                    "key": "/works/OL1W",
                    "title": "Polynomial automorphisms and the Jacobian conjecture",
                }
            ]
        }
        routes = [
            ("api.crossref.org", CROSSREF_ALON_QUERY),  # would be a wrong hit shape
            ("api.openalex.org", EMPTY_OPENALEX),
            ("api.zbmath.org", EMPTY_ZBMATH),
            ("archive.org", EMPTY_ARCHIVE_ORG),
            ("openlibrary.org", openlibrary_hit),
        ]
        entry = (
            "[1] A. van den Essen, *Polynomial Automorphisms and the Jacobian "
            "Conjecture*, Progress in Mathematics 190, Birkhäuser, Basel, 2000."
        )
        report = vr.verify_archive_text(FakeFetcher(routes), make_archive(entry))
        self.assertEqual(report["verdict"], "pass", report["issues"])
        self.assertEqual(report["entries"][0]["matched"][0]["source"], "openlibrary")


class InfrastructureTests(unittest.TestCase):
    def test_dead_link_warns_by_default_and_fails_when_strict(self):
        entry = KELLER_ENTRY  # carries the doi.org URL
        dead = {"https://doi.org/10.1007/bf01695502": 404}
        report = vr.verify_archive_text(
            FakeFetcher(FULL_ROUTES, links=dead), make_archive(entry)
        )
        self.assertEqual(report["verdict"], "pass_with_warnings")
        self.assertTrue(any("unreachable" in w for w in report["warnings"]))

        strict = vr.verify_archive_text(
            FakeFetcher(FULL_ROUTES, links=dead), make_archive(entry), strict_links=True
        )
        self.assertEqual(strict["verdict"], "fail")

    def test_offline_cache_miss_is_reported_honestly(self):
        with tempfile.TemporaryDirectory() as tmp:
            cache = Path(tmp) / "cache.json"
            fetcher = vr.CacheFetcher(FakeFetcher(FULL_ROUTES), cache, offline=True)
            report = vr.verify_archive_text(fetcher, make_archive(KELLER_ENTRY))
            self.assertEqual(report["verdict"], "fail")
            self.assertTrue(any("lookup failed" in i or "not cached" in i for i in report["issues"]))

    def test_offline_cache_hit_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            cache = Path(tmp) / "cache.json"
            warm = vr.CacheFetcher(FakeFetcher(FULL_ROUTES), cache)
            first = vr.verify_archive_text(warm, make_archive(KELLER_ENTRY))
            self.assertEqual(first["verdict"], "pass", first["issues"])
            warm.save()

            cold = vr.CacheFetcher(FakeFetcher([]), cache, offline=True)
            second = vr.verify_archive_text(cold, make_archive(KELLER_ENTRY))
            self.assertEqual(second["verdict"], "pass", second["issues"])

    def test_cli_exit_codes(self):
        with tempfile.TemporaryDirectory() as tmp:
            archive = Path(tmp) / "archive.md"
            archive.write_text(make_archive(KELLER_ENTRY), encoding="utf-8")
            cache = Path(tmp) / "cache.json"
            warm = vr.CacheFetcher(FakeFetcher(FULL_ROUTES), cache)
            vr.verify_archive_text(warm, make_archive(KELLER_ENTRY))
            warm.save()

            ok = vr.main([str(archive), "--offline", "--cache-file", str(cache)])
            self.assertEqual(ok, 0)
            missing = vr.main([str(Path(tmp) / "nope.md")])
            self.assertEqual(missing, 2)


if __name__ == "__main__":
    unittest.main()
