# Mathematical Object Origin Archive | Momentum Map

## 1. Archive Information

- Standard Name: Momentum map (also called moment map)
- Mathematical Field: Symplectic Geometry
- Abstract: A momentum map is a map from a symplectic manifold carrying a Lie-group symmetry to the dual of the group's Lie algebra. Its components are Hamiltonians for the infinitesimal symmetry generators. It was formed to turn continuous Hamiltonian symmetry into a coherent family of conserved quantities and, through its level sets, into a mechanism for reducing the dynamical system by that symmetry.

## 2. Core Record

### Precise Description

Let \((M,\omega)\) be a symplectic manifold, and let a Lie group \(G\) act smoothly on \(M\) by symplectomorphisms. Write \(\mathfrak g\) for the Lie algebra of \(G\), and for \(\xi\in\mathfrak g\) let
\[
\xi_M(x)=\left.\frac{d}{dt}\right|_{t=0}\exp(t\xi)\cdot x
\]
be the corresponding infinitesimal generator. A **momentum map** is a smooth map
\[
\mu:M\longrightarrow \mathfrak g^*
\]
such that, for every \(\xi\in\mathfrak g\), its component \(\mu^\xi(x)=\langle\mu(x),\xi\rangle\) satisfies
\[
d\mu^\xi=\iota_{\xi_M}\omega. \tag{1}
\]
Thus \(\xi_M\) is the Hamiltonian vector field of \(\mu^\xi\), under the convention \(\iota_{X_f}\omega=df\). A momentum map is commonly required to be equivariant:
\[
\mu(g\cdot x)=g\cdot\mu(x),
\]
where the coadjoint action used here is explicitly defined by
\[
\langle g\cdot\alpha,\xi\rangle
   =\langle\alpha,\operatorname{Ad}_{g^{-1}}\xi\rangle.
\]
Conventions differ by a sign in (1), and some authors use “momentum map” without building equivariance into the definition [1,2]. An action admitting such a map is called Hamiltonian. A merely symplectic action need not be Hamiltonian: symplecticity implies that each one-form \(\iota_{\xi_M}\omega\) is closed, but it may fail to be exact, so a global function \(\mu^\xi\) may not exist.

### Mathematical Context and Formation

The motivating problem class is the exploitation of Lie-group symmetry in Hamiltonian dynamics: given a Hamiltonian system \((M,\omega,H)\) with a continuous symmetry group \(G\), one wants both to extract the conservation laws forced by the symmetry and to remove the corresponding redundant degrees of freedom. For a single one-parameter symmetry, a scalar first integral can serve the first purpose. A general Lie group, however, supplies an entire linear space of infinitesimal generators. Treating their Hamiltonians as unrelated scalar functions leaves three connected difficulties unresolved.

First, the equation defining a Hamiltonian for \(\xi_M\) is global: it asks for a primitive of the closed one-form \(\iota_{\xi_M}\omega\). Local primitives or separately chosen functions do not overcome the obstruction to exactness. Second, even where primitives \(J_\xi\) exist, each is determined only up to an additive constant; arbitrary choices need not depend linearly on \(\xi\) or transform correctly under a noncommutative group. Third, symmetry reduction requires a geometrically natural common constraint set preserved by the appropriate group action, not merely a list of first integrals in chosen coordinates.

The forming insight is that a linear family \(\xi\mapsto J_\xi(x)\) is equivalently one covector in \(\mathfrak g^*\) at every point \(x\). Packaging all components as \(\mu(x)\) converts the separate equations into (1). Equivariance then imposes the compatibility between the group action on \(M\) and the coadjoint action on \(\mathfrak g^*\); it removes the arbitrariness that would make the family geometrically incoherent. The fibers \(\mu^{-1}(\alpha)\) simultaneously fix all symmetry-generated quantities and therefore supply the common constraint sets needed for reduction. This is a mathematical reconstruction of the object's formation from the symmetry-and-reduction problem, rather than a claim that it resulted from one isolated historical episode [1,2].

### Essential Role

The momentum map makes the conservation-law part of the problem tractable component by component but without losing the full group structure. If \(H\) is \(G\)-invariant and \(x(t)\) is an integral curve of its Hamiltonian vector field, then
\[
\frac{d}{dt}\mu^\xi(x(t))
 =d\mu^\xi(X_H)
 =\omega(\xi_M,X_H)
 =-dH(\xi_M)=0.
\]
Hence every component \(\mu^\xi\) is conserved. The value \(\mu(x(t))\in\mathfrak g^*\) records all these conservation laws in one coordinate-free object, while equivariance describes how that value transforms under symmetry. The definition also exposes, rather than conceals, the exact obstruction: if \([\iota_{\xi_M}\omega]\neq0\) in \(H^1_{\mathrm{dR}}(M)\) for some \(\xi\), the symplectic action has no momentum map satisfying (1).

More decisively for eliminating symmetry, a fixed momentum value produces a canonical constraint manifold. Under the regularity, freeness, and properness hypotheses of symplectic reduction, the quotient
\[
M_\alpha=\mu^{-1}(\alpha)/G_\alpha,
\]
where \(G_\alpha\) is the coadjoint stabilizer of \(\alpha\), carries a reduced symplectic form \(\omega_\alpha\) characterized by
\[
\pi^*\omega_\alpha=i^*\omega,
\]
with \(i:\mu^{-1}(\alpha)\hookrightarrow M\) and \(\pi:\mu^{-1}(\alpha)\to M_\alpha\) [1,3]. Thus the components of \(\mu\) provide the constraints, equivariance guarantees that the stabilizer preserves their common level set, and the defining differential identity ensures that precisely the symmetry directions become null directions of the restricted two-form and can be quotiented out. These features reformulate “discard the degrees of freedom generated by symmetry” as an intrinsic symplectic construction. The deeper structural viewpoint is that conserved quantities are not an external list attached to a Hamiltonian: for Hamiltonian group actions they assemble into a single map to \(\mathfrak g^*\), and its coadjoint geometry organizes both conservation and reduction.

## 3. Notes

For a translation action on a cotangent bundle, the corresponding components recover linear momentum; for a rotation action, they recover angular momentum. These examples explain the terminology but are not needed for the abstract definition. Momentum maps should not be confused with the Hamiltonian \(H\): \(H\) generates time evolution, whereas \(\mu\) generates and records the specified group action. Non-equivariant momentum maps and group-valued momentum maps require modified reduction statements and are outside this archive.

## 4. Sources

[1] Jerrold E. Marsden and Tudor S. Ratiu, *Introduction to Mechanics and Symmetry*, 2nd ed., Springer, 1999, chapters 11–13.

[2] Ana Cannas da Silva, *Lectures on Symplectic Geometry*, Lecture Notes in Mathematics 1764, Springer, 2001, chapters 21–23.

[3] Jerrold Marsden and Alan Weinstein, “Reduction of Symplectic Manifolds with Symmetry,” *Reports on Mathematical Physics* 5 (1974), 121–130.
