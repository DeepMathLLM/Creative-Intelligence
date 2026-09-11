# Mathematical Object Origin Archive | Haar Measure

## 1. Archive Information

- Standard Name: Haar measure
- Mathematical Field: Harmonic Analysis; Topological Groups
- Abstract: A Haar measure is a nonzero translation-invariant Radon measure on a locally compact Hausdorff group. It was formed to solve the problem of constructing an intrinsic integral compatible with group translation when neither coordinates nor a finite invariant total measure are generally available. Local finiteness and regularity make integration analytically usable, while invariance supplies the change-of-variables principle needed for averaging and convolution.

## 2. Core Record

### Precise Description

Let \(G\) be a locally compact Hausdorff topological group. A **left Haar measure** on \(G\) is a nonzero positive regular Borel measure \(\mu\) such that

\[
\mu(gE)=\mu(E)
\]

for every \(g\in G\) and every Borel set \(E\subseteq G\), with \(\mu(K)<\infty\) for every compact \(K\subseteq G\). Equivalently, it is a nonzero left-translation-invariant Radon measure; it has full support, so every nonempty open set has positive measure. Haar's theorem states that every locally compact Hausdorff group admits such a measure and that any two left Haar measures are positive scalar multiples of one another [1,2]. Thus the normalization is canonical only up to scale. On a compact group one usually fixes \(\mu(G)=1\); on a discrete group, counting measure is a Haar measure.

A right Haar measure is defined by \(\mu(Eg)=\mu(E)\). Left and right Haar measures need not coincide. For a fixed left Haar measure their discrepancy is measured by the modular function \(\Delta:G\to(0,\infty)\), subject to the convention used to define \(\Delta\); groups for which left Haar measure is also right invariant are called unimodular [1].

### Mathematical Context and Formation

The motivating problem was to construct an intrinsic integration theory for functions on a locally compact group \(G\) that respects the group's basic symmetry. In familiar special cases the needed integral was already visible: sums over a discrete group use counting measure, integrals over \(\mathbb{R}^n\) use Lebesgue measure, and averages over a compact rotation group should not change when every argument is translated by the same group element. The general problem was to find an integral \(I\) on compactly supported continuous functions satisfying

\[
I(f\circ L_g)=I(f),\qquad (L_gx=gx),
\]

along with positivity and enough local finiteness for \(I(f)\) to be finite [1,2].

The difficulty is that an arbitrary locally compact group has no preferred coordinates, Euclidean volume element, or necessarily any differentiable structure from which to import a measure. Counting measure ceases to be locally finite on a nondiscrete group, while requiring a finite invariant measure on all of \(G\) is too restrictive for the noncompact case: for example, translation invariance on \(\mathbb{R}\) is incompatible with assigning finite positive mass to the whole line. Choosing an arbitrary Borel measure does not solve the problem, because its translates can change integrals and hence destroy the symmetry needed for group-based averaging and convolution.

The defining synthesis behind Haar measure is to retain exactly the compatible requirements. Translation invariance encodes the group symmetry; the Radon conditions—especially finiteness on compact sets and regularity—replace unattainable global finiteness by analytically useful local control; and local compactness provides the compactly supported functions and compact neighborhoods on which the construction can be organized. One may formulate the construction first as a positive invariant linear functional on \(C_c(G)\); the Riesz representation theorem then realizes that functional as a regular Borel measure [1,3]. The unavoidable freedom to multiply the functional by a positive constant becomes uniqueness of Haar measure up to scale. In this way the object is not an arbitrary measure later found to be useful: its properties are the direct mathematical formulation of the invariant-integration problem.

### Essential Role

Haar measure makes the invariant integral itself well-defined and supplies the precise substitution rule needed to manipulate it:

\[
\int_G f(gx)\,d\mu(x)=\int_G f(x)\,d\mu(x).
\]

This overcomes the absence of coordinates by making translation, rather than a coordinate Jacobian, the organizing symmetry. It bypasses the failure of finite total mass on noncompact groups because every \(f\in C_c(G)\) is still integrable, and regularity permits approximation and localization by compact and open sets.

These features make the central operation of group harmonic analysis tractable. For suitable functions, left Haar measure defines convolution by

\[
(f*h)(x)=\int_G f(y)h(y^{-1}x)\,d\mu(y).
\]

Left invariance ensures that translating variables in this integral is legitimate and that convolution interacts coherently with the regular action of \(G\). The same measure defines the spaces \(L^p(G,\mu)\) on which translations act, allowing questions about functions to be reformulated in terms of group representations and operator algebra. In the compact case, normalization to total mass one additionally turns integration into a canonical averaging operator: averaging a function or vector over the group produces an invariant component when the relevant integral is defined [2].

The direct contribution is therefore not merely the later extension of Fourier analysis to more groups. Haar measure resolves the antecedent obstruction—how to integrate without preferred coordinates while preserving translation symmetry—by combining invariance with local, rather than global, finiteness. Its uniqueness up to scale also shows that the resulting integration theory is intrinsic to the topological group, modulo the normalization that no nonzero invariant integral can determine by itself.

## 3. Notes

- “Haar measure” may mean a left or a right Haar measure; the side should be specified for a nonunimodular group.
- A left Haar measure is not generally invariant under right translations or inversion. The modular function records the resulting correction factors.
- Local compactness is essential to the classical Haar theorem stated here. Broader classes of topological groups need not admit a nontrivial locally finite translation-invariant Borel measure.
- Haar probability measure on a compact group is obtained by the normalization \(\mu(G)=1\); this is a normalized instance of the same object, not a separate construction.

## 4. Sources

[1] G. B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed., CRC Press, 2016, Chapter 2.

[2] E. Hewitt and K. A. Ross, *Abstract Harmonic Analysis*, Vol. I, 2nd ed., Springer, 1979, Chapters 2–3.

[3] W. Rudin, *Functional Analysis*, 2nd ed., McGraw–Hill, 1991, discussion of positive linear functionals and the Riesz representation theorem.
