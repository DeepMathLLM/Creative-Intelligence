# Mathematical Object Origin Archive | Gromov Width

## 1. Archive Information

- Standard Name: Gromov width
- Mathematical Field: Symplectic Geometry
- Abstract: The Gromov width is the supremal symplectic area \(\pi r^{2}\) of a standard ball that symplectically embeds into a given symplectic manifold. It was formed from the ball-into-cylinder embedding problem exposed by Gromov's non-squeezing theorem: ordinary volume and local symplectic coordinates could not detect the obstruction, whereas testing a manifold by embedded standard balls produces a monotone numerical measure of its symplectic size.

## 2. Core Record

### Precise Description

Let \((M^{2n},\omega)\) be a symplectic manifold and let
\[
\omega_0=\sum_{j=1}^{n} dx_j\wedge dy_j
\]
be the standard symplectic form on \(\mathbb{R}^{2n}\). For the Euclidean open ball
\[
B^{2n}(r)=\{z\in\mathbb{R}^{2n}:\lVert z\rVert<r\},
\]
the **Gromov width** of \((M,\omega)\) is
\[
c_G(M,\omega)
 =\sup\left\{\pi r^2:\ (B^{2n}(r),\omega_0)
 \stackrel{s}{\hookrightarrow}(M,\omega)\right\},
\]
where \(\stackrel{s}{\hookrightarrow}\) denotes a symplectic embedding, namely an embedding \(\varphi\) satisfying \(\varphi^*\omega=\omega_0\). The value may be \(+\infty\) [2].

The definition immediately gives:

- **symplectic invariance:** symplectomorphic manifolds have the same Gromov width;
- **monotonicity:** if \((M,\omega)\stackrel{s}{\hookrightarrow}(N,\eta)\), then \(c_G(M,\omega)\leq c_G(N,\eta)\);
- **conformality:** for \(a>0\), \(c_G(M,a\omega)=a\,c_G(M,\omega)\).

Darboux's theorem implies \(c_G(M,\omega)>0\) for every nonempty symplectic manifold. Writing
\[
Z^{2n}(R)=B^2(R)\times\mathbb{R}^{2n-2},
\]
Gromov's non-squeezing theorem gives, for \(n\geq 2\),
\[
c_G(B^{2n}(r),\omega_0)=\pi r^2,
\qquad
c_G(Z^{2n}(R),\omega_0)=\pi R^2.
\]
Thus \(c_G\) is a normalized symplectic capacity in the convention assigning \(\pi\) to both the unit ball and unit cylinder [1][2].

### Mathematical Context and Formation

The motivating problem is a concrete symplectic embedding problem: for which \(r,R>0\) does there exist a symplectic embedding
\[
B^{2n}(r)\stackrel{s}{\hookrightarrow}Z^{2n}(R)?
\]
A symplectic map preserves the Liouville volume \(\omega_0^n/n!\), but the target cylinder has infinite \(2n\)-dimensional volume. Consequently, total volume supplies no restriction on \(r\) relative to \(R\). Local differential data do not supply one either: by Darboux's theorem all symplectic forms are locally standard, so there is no local curvature-like quantity that records whether a large ball can pass through the cylinder's distinguished two-dimensional cross-section [2]. These available viewpoints therefore miss the relevant global rigidity.

Gromov's non-squeezing theorem identifies that rigidity: a symplectic embedding \(B^{2n}(r)\hookrightarrow Z^{2n}(R)\) can exist only when \(r\leq R\); the reverse implication follows from the evident inclusion when \(r\leq R\). Gromov established the nontrivial direction using pseudoholomorphic curves [1]. The theorem shows that symplectic size is controlled not only by \(2n\)-volume but also by an area-scale constraint in a conjugate coordinate plane.

The defining idea of the Gromov width is to turn this discovery into an invariant for an arbitrary target: use standard symplectic balls as probes and record the largest ball capacity \(\pi r^2\) admitted by the target. The supremum is forced by the fact that a largest embedded ball need not be attained, while the quantity \(\pi r^2\), rather than \(r\) or \(r^{2n}\), has exactly the linear scaling under rescaling of the symplectic form required of a symplectic capacity. Non-squeezing is the ingredient that makes this probe nontrivial: although \(Z^{2n}(R)\) is unbounded and has infinite volume, its width is the finite number \(\pi R^2\) [2]. The later axiomatic language of symplectic capacities isolates monotonicity, conformality, and ball/cylinder nontriviality as the structural properties exemplified by this construction [2][3].

### Essential Role

For the motivating ball-into-cylinder problem, the Gromov width packages the hard geometric obstruction into the scalar comparison
\[
B^{2n}(r)\stackrel{s}{\hookrightarrow}Z^{2n}(R)
\quad\Longrightarrow\quad
c_G(B^{2n}(r))\leq c_G(Z^{2n}(R)),
\]
which becomes
\[
\pi r^2\leq \pi R^2.
\]
Together with inclusion for \(r\leq R\), this recovers the exact threshold. The mechanism is specific: the supremum over ball embeddings makes width monotone under composition of embeddings, and non-squeezing computes the cylinder's width from its two-dimensional radius even though every volume-based upper bound is vacuous.

More generally, for an embedding problem \((U,\omega_U)\hookrightarrow(V,\omega_V)\), the inequality \(c_G(U)>c_G(V)\) is an immediate certificate of nonexistence. This changes one tractable part of the problem—the search for obstructions—from analysis of all possible nonlinear embeddings to comparison of two numbers. Conceptually, it introduces an area-valued, global notion of symplectic size: one asks how large a standard symplectic ball the space can receive, rather than how much volume the space contains.

The contribution is limited but precise. The inequality \(c_G(U)\leq c_G(V)\) is generally only necessary, not sufficient, for an embedding, and calculating either width can itself require difficult symplectic arguments. The Gromov width therefore does not solve every embedding construction problem; it directly overcomes the failure of volume and local invariants to see the non-squeezing obstruction and supplies a reusable numerical formulation of that obstruction.

## 3. Notes

The Gromov width is one particular symplectic capacity, not a synonym for the entire class of capacities. Some authors parametrize balls by area, writing \(B^{2n}(a)=\{z:\pi\lVert z\rVert^2<a\}\); in that convention the same definition reads \(c_G(M)=\sup\{a:B^{2n}(a)\stackrel{s}{\hookrightarrow}M\}\). “Normalized” refers here to the convention \(c(B^{2n}(1))=c(Z^{2n}(1))=\pi\).

## 4. Sources

[1] M. Gromov, “Pseudo holomorphic curves in symplectic manifolds,” *Inventiones Mathematicae* **82** (1985), 307–347. https://doi.org/10.1007/BF01388806

[2] K. Cieliebak, H. Hofer, J. Latschev, and F. Schlenk, “Quantitative symplectic geometry,” in *Dynamics, Ergodic Theory, and Geometry*, MSRI Publications **54**, Cambridge University Press, 2007, pp. 1–44. https://arxiv.org/abs/math/0506191

[3] I. Ekeland and H. Hofer, “Symplectic topology and Hamiltonian dynamics,” *Mathematische Zeitschrift* **200** (1989), 355–378. https://doi.org/10.1007/BF01215653
