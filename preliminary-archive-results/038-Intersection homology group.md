# Mathematical Object Origin Archive | Intersection Homology Group

## 1. Archive Information

- Standard Name: Intersection homology group (Goresky–MacPherson intersection homology)
- Mathematical Field: Algebraic Topology; topology of stratified spaces
- Abstract: For a stratified pseudomanifold, an intersection homology group is the homology of a chain complex in which a perversity imposes codimension-dependent limits on how chains and their boundaries may meet singular strata. It was formed to extend geometric intersection theory and Poincaré duality from manifolds to singular spaces without discarding the singular locus.

## 2. Core Record

### Precise Description

Let
\[
X=X_n\supset X_{n-2}\supset X_{n-3}\supset\cdots\supset X_0\supset X_{-1}=\varnothing
\]
be an \(n\)-dimensional PL stratified pseudomanifold, with \(X_{n-1}=X_{n-2}\), and let \(R\) be a coefficient ring. A traditional Goresky–MacPherson perversity is a function
\[
\bar p:\{2,\ldots,n\}\longrightarrow \mathbb Z_{\ge 0}
\]
such that \(\bar p(2)=0\) and \(\bar p(k+1)-\bar p(k)\in\{0,1\}\). An \(i\)-dimensional PL chain \(\xi\in C_i(X;R)\) is \(\bar p\)-allowable when, for every \(k\ge 2\),
\[
\dim\bigl(|\xi|\cap X_{n-k}\bigr)\le i-k+\bar p(k)
\]
and its boundary satisfies
\[
\dim\bigl(|\partial\xi|\cap X_{n-k}\bigr)\le i-1-k+\bar p(k),
\]
where \(\dim\varnothing=-\infty\). The allowable chains form a subcomplex \(I^{\bar p}C_*(X;R)\subset C_*(X;R)\), and the associated object is
\[
I^{\bar p}H_i(X;R)=H_i\!\left(I^{\bar p}C_*(X;R)\right),
\]
the \(i\)-th intersection homology group of perversity \(\bar p\) [1, 3]. If \(X\) is a manifold, there are no singular strata imposing restrictions, so this construction recovers ordinary homology.

### Mathematical Context and Formation

The motivating problem class was to extend the manifold intersection pairing and Poincaré duality to compact oriented singular spaces, notably singular complex algebraic varieties and, more generally, stratified pseudomanifolds [1]. On a closed oriented \(n\)-manifold, cycles of complementary dimensions can be moved into general position; their intersections define a pairing, and the resulting fundamental-class map expresses Poincaré duality. At a singular stratum this argument breaks: a neighborhood has a cone on a link rather than a Euclidean ball, and ordinary cycles may pass through the stratum with more incidence than manifold transversality permits. Consequently ordinary homology need not carry a nondegenerate complementary-dimensional intersection pairing and need not satisfy manifold-form Poincaré duality.

The two direct manifold-based choices were inadequate for opposite reasons. Retaining every ordinary chain preserved uncontrolled passages through singularities, so chain intersections could acquire excess-dimensional pieces or fail to represent the required product. Removing the singular locus restored a manifold but erased precisely the global information about how cycles approach and traverse the singularities. The formative insight was instead to stratify the singular set by codimension and admit only a controlled defect from transversality. The integer \(\bar p(k)\) measures the permitted defect along codimension-\(k\) strata, while the two dimension inequalities impose that control on both a chain and its boundary. Thus the geometric requirement survives passage to homology as an actual chain complex rather than as an informal general-position condition [1, 3].

### Essential Role

Intersection homology made the missing duality problem tractable by replacing unrestricted cycles with cycles whose singular incidence is quantitatively compatible with intersection. The bound
\[
\dim(|\xi|\cap X_{n-k})\le i-k+\bar p(k)
\]
starts from the dimension \(i-k\) expected for transverse contact with a codimension-\(k\) set and permits exactly the defect specified by \(\bar p(k)\). Requiring the corresponding bound for \(\partial\xi\) ensures closure under the boundary operator. These features allow suitably positioned allowable chains to be intersected without leaving the controlled theory.

More precisely, let \(\bar t(k)=k-2\) be the top perversity and let \(\bar p,\bar q\) be complementary traditional perversities, so \(\bar p(k)+\bar q(k)=\bar t(k)\). For a compact oriented \(n\)-dimensional PL pseudomanifold and field coefficients \(F\), the intersection construction yields the nondegenerate duality pairing
\[
I^{\bar p}H_i(X;F)\otimes I^{\bar q}H_{n-i}(X;F)\longrightarrow F,
\]
recovering ordinary Poincaré duality when the singular strata are absent [1, 2]. The object therefore did not merely attach another invariant to a singular space: it reformulated admissibility of cycles so that the failed manifold argument could be replaced by a stratified one. Its deeper structural contribution is that singularities are handled neither by ignoring them nor by allowing arbitrary contact, but by a family of homology theories indexed by perversity, with complementary choices encoding the two sides of duality.

## 3. Notes

“Intersection homology” is not the homology of pairwise intersections of arbitrary subspaces. It is the homology of the allowable-chain complex. “Intersection cohomology” is often used for a cohomological or sheaf-theoretic realization of closely related invariants; conventions for grading, supports, coefficients, and perversities must be stated when comparing formulations. The definition above is the traditional PL, chain-level version. General perversities and non-field coefficients require additional qualifications, especially in duality statements [2, 3].

## 4. Sources

[1] M. Goresky and R. MacPherson, “Intersection Homology Theory,” *Topology* 19, no. 2 (1980), 135–162.

[2] M. Goresky and R. MacPherson, “Intersection Homology II,” *Inventiones Mathematicae* 72, no. 1 (1983), 77–129.

[3] Greg Friedman, “An Introduction to Intersection Homology with General Perversity Functions,” in *Topology of Stratified Spaces*, Mathematical Sciences Research Institute Publications 58, Cambridge University Press, 2011, 177–222, https://faculty.tcu.edu/gfriedman/papers/MSRI-revised-2.pdf.
