# Mathematical Object Origin Archive | Projection-Valued Measure

## 1. Archive Information

- Standard Name: Projection-valued measure
- Mathematical Field: Functional Analysis
- Abstract: A projection-valued measure replaces the finite list of eigenspace projections in matrix diagonalization by a countably additive family of orthogonal projections indexed by measurable spectral sets. It was formed to make spectral decomposition meaningful for self-adjoint operators with continuous spectrum, where eigenvectors and discrete eigenvalue sums do not suffice.

## 2. Core Record

### Precise Description

Let \(H\) be a complex Hilbert space and \((X,\Sigma)\) a measurable space. A **projection-valued measure** (PVM), also called a resolution of the identity, is a map
\[
E:\Sigma\longrightarrow \mathcal B(H)
\]
such that:

1. \(E(B)\) is an orthogonal projection for every \(B\in\Sigma\);
2. \(E(\varnothing)=0\) and \(E(X)=I\);
3. \(E(B\cap C)=E(B)E(C)\) for all \(B,C\in\Sigma\);
4. if \((B_n)\) are pairwise disjoint, then
   \[
   E\!\left(\bigcup_{n=1}^{\infty}B_n\right)x
   =\sum_{n=1}^{\infty}E(B_n)x
   \quad\text{for every }x\in H,
   \]
   with convergence in \(H\), equivalently countable additivity in the strong operator topology [1].

Thus disjoint measurable sets determine mutually orthogonal subspaces. For \(x,y\in H\),
\[
\mu_{x,y}(B)=\langle E(B)x,y\rangle
\]
is a complex measure. These scalar measures define the spectral integral: for bounded measurable \(f\), the operator \(\int_X f\,dE\) is characterized by
\[
\left\langle \left(\int_X f\,dE\right)x,y\right\rangle
=\int_X f\,d\mu_{x,y}.
\]
For a bounded self-adjoint operator \(T\), the spectral theorem supplies a unique PVM \(E_T\) on the Borel subsets of \(\sigma(T)\subset\mathbb R\) such that
\[
T=\int_{\sigma(T)}\lambda\,dE_T(\lambda).
\]
More generally, bounded normal operators admit the analogous decomposition over their complex spectra [1].

### Mathematical Context and Formation

The motivating problem is to extend orthogonal diagonalization from self-adjoint matrices to bounded self-adjoint operators on infinite-dimensional Hilbert spaces. In finite dimensions, if \(T\) has distinct eigenvalues \(\lambda_1,\ldots,\lambda_m\), then
\[
T=\sum_{j=1}^m \lambda_j P_j,
\qquad
I=\sum_{j=1}^m P_j,
\]
where \(P_j\) projects onto the \(\lambda_j\)-eigenspace. This representation simultaneously decomposes the space and makes \(f(T)=\sum_j f(\lambda_j)P_j\) calculable.

The obstruction in infinite dimensions is that a self-adjoint operator may have continuous spectrum and no nonzero eigenvectors. The concrete model is
\[
(M_tu)(t)=t\,u(t)\quad\text{on }L^2([0,1]).
\]
If \(M_tu=\lambda u\), then \((t-\lambda)u(t)=0\) almost everywhere, so \(u\) is supported on the singleton \(\{\lambda\}\), a null set; hence \(u=0\) in \(L^2([0,1])\). Therefore no eigenbasis and no discrete sum of eigenspace projections can diagonalize \(M_t\), even though its spectrum is the entire interval \([0,1]\). Merely knowing the spectral set \(\sigma(T)\) does not say how vectors split among its regions, while a scalar spectral measure attached to one vector does not by itself encode a compatible decomposition of the whole Hilbert space.

The decisive reformulation is to replace a projection for each eigenvalue by a projection for each Borel spectral set. For the multiplication operator, define
\[
(E(B)u)(t)=\mathbf 1_{B\cap[0,1]}(t)u(t).
\]
This is a PVM: intersections of sets become products of projections, and disjoint countable unions become orthogonal strong sums. Moreover,
\[
M_t=\int_{[0,1]}\lambda\,dE(\lambda).
\]
The finite-dimensional formulas are retained, but finite or countable atomic sums are replaced by operator-valued integration. In this model \(E(\{\lambda\})=0\) for every \(\lambda\), showing why the measure must act on sets rather than only on individual spectral points. The general spectral theorem establishes that this same structure exists uniquely for every bounded self-adjoint operator [1][2].

### Essential Role

The PVM makes the missing part of infinite-dimensional diagonalization tractable: it assigns to every measurable spectral region \(B\) the closed subspace \(E_T(B)H\) consisting of the component of the Hilbert space carried by that region. Orthogonality of the projection values preserves the geometry of eigenspace decomposition; strong countable additivity replaces addition over a finite eigenvalue list; and spectral integration replaces the diagonal sum.

Concretely, if a bounded measurable function is first approximated by simple functions
\[
s=\sum_{k=1}^r c_k\mathbf 1_{B_k},
\]
then
\[
\int s\,dE_T=\sum_{k=1}^r c_kE_T(B_k).
\]
Passing to bounded measurable limits produces the Borel functional calculus
\[
f(T)=\int_{\sigma(T)} f(\lambda)\,dE_T(\lambda),
\]
which includes \(T\) itself by taking \(f(\lambda)=\lambda\) [1][2]. For \(M_t\), this calculus gives \(f(M_t)u=(f\circ t)u\), exactly as diagonal substitution would, although the operator has no eigenvectors.

Thus the object does not merely record the spectrum. Its projection values encode how the operator acts on every part of the space, including nonatomic continuous-spectrum parts. The deeper structural viewpoint is that diagonalization is a multiplicative map from measurable scalar functions to operators: indicator functions become orthogonal projections, and the coordinate function becomes \(T\). This reformulates “find an eigenbasis” into “construct a spectral resolution,” a formulation that remains valid when point eigenspaces vanish.

## 3. Notes

“Spectral measure” is used both for a PVM and, in some texts, for scalar measures such as \(\mu_{x,x}\); the operator-valued meaning is intended here. A PVM is also called a spectral resolution or resolution of the identity. It differs from a positive operator-valued measure: PVM values are idempotent orthogonal projections and satisfy \(E(B\cap C)=E(B)E(C)\).

For unbounded self-adjoint operators the same PVM representation holds, but the integral of \(\lambda\) is an unbounded operator whose domain must be specified; the archive has used the bounded case to isolate the originating spectral-decomposition problem without those domain issues.

## 4. Sources

[1] L. Tomczak-Jaegermann, *The Spectral Theorem*, University of California, Berkeley lecture notes, https://math.berkeley.edu/~ltomczak/notes/SpecThm.pdf

[2] C. Remling, *The Spectral Theorem*, functional analysis lecture notes, University of Oklahoma, Chapter 10, https://math.ou.edu/~cremling/teaching/lecturenotes/fa-new/ln10.pdf
