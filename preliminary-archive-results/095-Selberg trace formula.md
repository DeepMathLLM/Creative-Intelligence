# Mathematical Object Origin Archive | Selberg trace formula

## 1. Archive Information

- Standard Name: Selberg trace formula
- Mathematical Field: Analytic number theory, harmonic analysis, and spectral geometry
- Abstract: The Selberg trace formula is a family of exact trace identities for automorphic quotients. In its compact hyperbolic-surface form, it equates a smoothed sum over Laplace eigenvalues with an area term and a weighted sum over hyperbolic conjugacy classes, or equivalently closed geodesics. It was formed to make the spectral analysis of nonabelian discontinuous-group quotients explicit enough to compare automorphic spectra with geometric and arithmetic data.

## 2. Core Record

### Precise Description

Let \(\Gamma\subset \operatorname{PSL}_2(\mathbb R)\) be a torsion-free cocompact discrete subgroup (equivalently, a torsion-free uniform lattice), let \(X=\Gamma\backslash\mathbb H\), and let the nonnegative hyperbolic Laplacian have eigenvalues
\[
0=\lambda_0\leq \lambda_1\leq\cdots,\qquad \lambda_j=\frac14+r_j^2,
\]
with multiplicity; parameters for eigenvalues below \(1/4\) may be imaginary. For an even test function \(h\), holomorphic in a strip wider than \(|\operatorname{Im}r|\leq 1/2\) and sufficiently decaying there, set
\[
g(u)=\frac{1}{2\pi}\int_{-\infty}^{\infty}h(r)e^{-iru}\,dr.
\]
A standard compact form of the Selberg trace formula is
\[
\sum_{j=0}^{\infty}h(r_j)
=
\frac{\operatorname{Area}(X)}{4\pi}
\int_{-\infty}^{\infty} r h(r)\tanh(\pi r)\,dr
+
\sum_{[P]\,\mathrm{primitive}}\sum_{k=1}^{\infty}
\frac{\ell(P)}{2\sinh\!\bigl(k\ell(P)/2\bigr)}\,
 g\!\bigl(k\ell(P)\bigr).
\]
Here \([P]\) runs over primitive hyperbolic conjugacy classes in \(\Gamma\), and \(\ell(P)\) is the length of the associated primitive closed geodesic. Thus the left side is spectral, while the right side consists of the identity contribution and hyperbolic orbital contributions [1][2].

The displayed identity is a clean specialization, not the full scope of the object. For quotients with torsion or cusps, elliptic and parabolic terms appear, and in the noncompact finite-area case the continuous spectrum and scattering data must also be included. More generally, the formula is understood representation-theoretically as the trace of suitable convolution operators on \(L^2(\Gamma\backslash G)\), expressed both through the spectral decomposition and through conjugacy classes in \(\Gamma\) [1][3].

### Mathematical Context and Formation

The motivating problem class was the spectral analysis of automorphic functions on quotients by discontinuous groups: for a space such as \(X=\Gamma\backslash\mathbb H\), obtain usable information about the eigenvalues and multiplicities of the invariant Laplacian and relate that information to explicit data carried by \(\Gamma\). In the surface case, the same group data are encoded geometrically by primitive closed geodesics. Selberg's 1956 treatment placed this problem in harmonic analysis on weakly symmetric spaces and sought applications to Dirichlet series [1].

The obstruction was not merely that the eigenvalues were hard to calculate. On an abelian flat quotient, characters and Poisson summation provide a direct dual-lattice comparison. By contrast, the uniform lattice defining a closed hyperbolic surface is nonabelian, so there is no frequency lattice whose ordinary Poisson summation directly organizes the automorphic spectrum. Nor is the unsmoothed sum of all Laplace eigenvalues a convergent trace. Direct spectral expansion describes an operator in terms of eigenfunctions but does not by itself expose the conjugacy classes and closed geodesics that carry the quotient's arithmetic and geometric information.

The forming insight was to replace the divergent raw spectral question by the trace of a suitably smoothed invariant operator and then calculate that one trace in two ways. Start with a radial point-pair kernel on \(\mathbb H\) whose integral operator commutes with the Laplacian, and periodize it:
\[
K_\Gamma(z,w)=\sum_{\gamma\in\Gamma}k(z,\gamma w).
\]
On the spectral side, the spherical transform of \(k\) is the test function \(h\), so the trace is \(\sum_j h(r_j)\). On the geometric side, integrate \(K_\Gamma(z,z)\) over a fundamental domain, unfold the sum, and regroup elements of \(\Gamma\) by conjugacy class. The identity class produces the area integral. For a nonidentity hyperbolic class, its centralizer and translation length reduce the orbital integral to the term involving \(\ell(P)\), its iterates \(k\ell(P)\), and the factor \(2\sinh(k\ell(P)/2)\). The Selberg/Harish-Chandra transform and ordinary Fourier transform supply the paired test functions \(h\) and \(g\). This double evaluation is the mathematical construction of the trace formula, rather than a coincidental equality between two pre-existing lists [2][3].

### Essential Role

The formula made the comparison between automorphic spectrum and quotient-group geometry tractable at the level where convergence and noncommutativity had blocked a direct comparison. Smoothing replaces an undefined raw trace by the convergent functional \(\sum_j h(r_j)\). Grouping by conjugacy classes replaces the unavailable abelian dual-lattice sum by orbital terms, and the centralizer of each hyperbolic element turns that class into explicit primitive-length and iterate data. The adjustable transform pair \(h\leftrightarrow g\) is essential: one chooses a function localized on the side to be investigated and estimates the exactly corresponding expression on the other side [2][3].

Consequently, global questions that were inaccessible from individual eigenfunctions or individual group elements could be attacked by test-function analysis. Choices of \(h\) yield spectral counting information such as Weyl-type asymptotics, while choices of \(g\) adapted to length ranges yield counting statements for primitive closed geodesics; reorganizing the hyperbolic terms as logarithmic derivatives also connects the spectrum to the Selberg zeta function and its associated Dirichlet-series questions [1][2]. These are direct consequences of the bridge built by the formula, not merely unrelated later applications.

The deeper reformulation is that the Laplace spectrum and the closed-geodesic length data are two expansions of one trace. The formula does not generally list individual eigenvalues or geodesics in closed form; its original power is instead an exact family of smoothed identities from which analytic information can be extracted.

## 3. Notes

The Selberg trace formula is distinct from the Selberg zeta function: the latter is an Euler product over primitive closed geodesics whose logarithmic derivative packages terms occurring on the geometric side. It is also distinct from the later Arthur–Selberg trace formula, which extends the trace-formula method to substantially broader reductive-group settings. The displayed formula omits elliptic, parabolic, and continuous-spectrum contributions because of the torsion-free cocompact hypothesis.

## 4. Sources

[1] Atle Selberg, “Harmonic Analysis and Discontinuous Groups in Weakly Symmetric Riemannian Spaces with Applications to Dirichlet Series,” *Journal of the Indian Mathematical Society*, New Series 20 (1956), 47–87. https://doi.org/10.18311/jims/1956/16985

[2] Dennis A. Hejhal, *The Selberg Trace Formula for PSL(2,R), Volume I*, Lecture Notes in Mathematics 548, Springer, 1976.

[3] Henryk Iwaniec, *Spectral Methods of Automorphic Forms*, 2nd ed., Graduate Studies in Mathematics 53, American Mathematical Society, 2002.
