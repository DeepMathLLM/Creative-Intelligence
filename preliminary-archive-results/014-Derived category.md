# Mathematical Object Origin Archive | Derived Category

## 1. Archive Information

- Standard Name: Derived category
- Mathematical Field: Homological Algebra
- Abstract: For an abelian category \(\mathcal A\), the derived category \(D(\mathcal A)\) is obtained from the homotopy category of chain complexes by formally inverting quasi-isomorphisms. It was formed to make constructions depending only on cohomological data—especially derived functors built from resolutions—independent of the chosen complex or resolution, without discarding the extension and connecting-morphism information carried by complexes and mapping cones.

## 2. Core Record

### Precise Description

Let \(\operatorname{Ch}(\mathcal A)\) be the category of cochain complexes in an abelian category \(\mathcal A\), and let \(K(\mathcal A)\) be its chain-homotopy category. A chain map \(s:X^\bullet\to Y^\bullet\) is a **quasi-isomorphism** if every induced map
\[
H^n(s):H^n(X^\bullet)\longrightarrow H^n(Y^\bullet)
\]
is an isomorphism. If \(W\) denotes the class of quasi-isomorphisms, the derived category is the localization
\[
D(\mathcal A)=K(\mathcal A)[W^{-1}].
\]
Thus its objects may be taken to be complexes, while a morphism can be represented by a roof
\[
X^\bullet\xleftarrow{\ s\ }Z^\bullet\xrightarrow{\ f\ }Y^\bullet,
\qquad s\in W,
\]
modulo the equivalence relation imposed by localization. The localization functor \(Q:K(\mathcal A)\to D(\mathcal A)\) sends every quasi-isomorphism to an isomorphism and is universal with this property [1,2]. Equivalently, \(D(\mathcal A)\) is the Verdier quotient of \(K(\mathcal A)\) by its full triangulated subcategory \(\operatorname{Ac}(\mathcal A)\) of acyclic complexes.

The translation is the degree shift \(X^\bullet\mapsto X^\bullet[1]\). The distinguished triangles are the triangles isomorphic to images of mapping-cone triangles
\[
X^\bullet\xrightarrow{f}Y^\bullet\longrightarrow \operatorname{Cone}(f)\longrightarrow X^\bullet[1].
\]
These data make \(D(\mathcal A)\) a triangulated category [1,2]. Bounded-above, bounded-below, and bounded versions are denoted \(D^-(\mathcal A)\), \(D^+(\mathcal A)\), and \(D^b(\mathcal A)\), respectively.

### Mathematical Context and Formation

The motivating problem class is the construction and comparison of derived functors of nonexact additive functors. If \(F:\mathcal A\to\mathcal B\) is left exact, for example, one replaces an object \(A\) by an injective resolution \(A\to I^\bullet\) and applies \(F\). Two resolutions have isomorphic cohomology, but the problem is stronger than obtaining separate groups \(R^nF(A)\): one needs a single functorial object that is independent of the resolution and that retains connecting maps, extension data, and compatibility with morphisms and exact sequences.

Neither of the evident categories solves this problem. In \(\operatorname{Ch}(\mathcal A)\), different resolutions remain different objects and comparison maps depend on choices. Passing to \(K(\mathcal A)\) removes dependence on chain homotopies, but a quasi-isomorphism need not become invertible there. The obstruction is concrete: a nonsplit short exact sequence
\[
0\longrightarrow A\longrightarrow B\longrightarrow C\longrightarrow 0
\]
viewed as a three-term complex is acyclic but need not be contractible, so it is generally nonzero in \(K(\mathcal A)\), although it has the same cohomology as the zero complex. At the opposite extreme, replacing a complex by only its graded cohomology objects forgets the chain-level extension and connecting information needed for derived constructions.

The decisive formation principle is therefore to impose exactly the desired equivalence—quasi-isomorphism—at the categorical level. Localizing \(K(\mathcal A)\) at quasi-isomorphisms makes every resolution map an isomorphism while preserving morphisms between complexes. This localization fits naturally with mapping cones: a chain map \(f\) is a quasi-isomorphism exactly when \(\operatorname{Cone}(f)\) is acyclic. Hence formally inverting quasi-isomorphisms is equivalent to making acyclic complexes zero in the Verdier quotient. Shifts and cones then supply distinguished triangles, the replacement for short exact sequences compatible with this cohomological equivalence [1–3].

### Essential Role

The derived category makes the resolution-independence part of the motivating problem tractable. Under the usual hypotheses ensuring suitable injective, projective, or adapted resolutions, a resolution map becomes an isomorphism in \(D(\mathcal A)\). Applying \(F\) to an appropriate resolution can therefore define a total derived functor
\[
\mathbf RF:D(\mathcal A)\longrightarrow D(\mathcal B)
\]
(or \(\mathbf LF\) for left-derived constructions) whose value is independent, up to the canonical isomorphism supplied by the derived-functor construction, of the chosen resolution. Its cohomology recovers the individual derived functors: \(H^n(\mathbf RF(A))\cong R^nF(A)\) [2,3].

This works because the definition combines three specific features. First, inversion of quasi-isomorphisms treats complexes carrying the same derived information as equivalent, bypassing the absence of actual or homotopy inverses for comparison maps. Second, morphisms represented by roofs permit maps to be transported across replacements, turning resolution-based assignments into functorial constructions rather than collections tied to choices. Third, mapping-cone triangles preserve the exactness information that graded cohomology alone would erase: applying a cohomological functor to a distinguished triangle produces a long exact sequence. Thus the original difficulty is not merely suppressed; it is reformulated as functorial calculus in a triangulated localization.

The deeper structural viewpoint is that a complex is regarded not as a particular presentation but as an object determined up to quasi-isomorphism, while its shifts, extensions, and connecting morphisms remain visible. That viewpoint is the direct conceptual gain required by the resolution problem; later uses of derived categories in geometry and representation theory build on, rather than constitute, this original role.

## 3. Notes

- The derived category is not the category of graded cohomology objects: complexes with isomorphic cohomology objects need not be isomorphic for reasons determined solely by a chosen degreewise identification, and the derived category retains extension data encoded by triangles.
- A triangulated derived category suppresses higher homotopies. Differential graded and stable \(\infty\)-categorical enhancements retain such higher information; these are refinements, not alternative definitions of the object archived here.
- Set-theoretic size conditions may be required to ensure that localization yields locally small Hom-sets. Standard treatments handle this by hypotheses on \(\mathcal A\), universes, or appropriate bounded/resolution models.

## 4. Sources

[1] Jean-Louis Verdier, *Des catégories dérivées des catégories abéliennes*, Astérisque 239, Société Mathématique de France, 1996.

[2] The Stacks Project Authors, *Derived Categories*, especially Sections 13.5–13.11, https://stacks.math.columbia.edu/download/derived.pdf and https://stacks.math.columbia.edu/tag/05QJ.

[3] Charles A. Weibel, *An Introduction to Homological Algebra*, Cambridge Studies in Advanced Mathematics 38, Cambridge University Press, 1994, Chapter 10.
