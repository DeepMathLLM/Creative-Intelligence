# Mathematical Object Origin Archive | Turaev–Viro invariant

## 1. Archive Information

- Standard Name: Turaev–Viro invariant
- Mathematical Field: Knot Theory and Low-Dimensional Topology
- Abstract: The Turaev–Viro invariant is a finite state-sum invariant of a triangulated closed 3-manifold. It turns quantum recoupling data—edge dimensions and tetrahedral quantum \(6j\)-symbols—into a scalar whose algebraic identities exactly cancel the changes caused by elementary modifications of the triangulation.

## 2. Core Record

### Precise Description

Let \(\mathcal C\) be a spherical fusion category with nonzero global dimension
\[
\operatorname{Dim}(\mathcal C)=\sum_{i\in I}d_i^2,
\]
where \(I\) is a set of representatives of the finitely many simple isomorphism classes and \(d_i\) is the spherical quantum dimension of \(i\). Let \(T\) be a finite triangulation of a closed oriented PL 3-manifold \(M\), with an ordering of its vertices. A coloring \(\lambda\) assigns a simple object to each oriented edge, subject to \(\lambda(ba)=\lambda(ab)^*\). For an ordered face \((abc)\), its multiplicity space is
\[
H_{abc}(\lambda)=\operatorname{Hom}_{\mathcal C}
  \bigl(\mathbf 1,\lambda(ab)\otimes\lambda(bc)\otimes\lambda(ca)\bigr).
\]
The associator, duality maps, and spherical trace of \(\mathcal C\) assign to every colored tetrahedron \(\tau\) a tetrahedral tensor \(F_\tau(\lambda)\); in a basis these tensors are the category's \(6j\)- or \(F\)-symbols. Tensors belonging to tetrahedra on opposite sides of a face lie in dual face spaces and are contracted. The categorical Turaev–Viro state sum is
\[
TV_{\mathcal C}(M;T)=
\operatorname{Dim}(\mathcal C)^{-|T^0|}
\sum_{\lambda:T^1\to I}
\left(\prod_{e\in T^1}d_{\lambda(e)}\right)
\operatorname{Contr}\!\left(
  \bigotimes_{\tau\in T^3}F_\tau(\lambda)
\right).
\]
Here the contraction includes the finite sums over bases of all face multiplicity spaces. Sphericality makes the graphical evaluations independent of planar choices, while fusion makes both the edge-coloring sum and every multiplicity-space sum finite. The state-sum theorem says that the displayed scalar is independent of the vertex ordering and triangulation, so it defines \(TV_{\mathcal C}(M)\) [2].

Turaev and Viro's original construction is the multiplicity-free root-of-unity \(U_q(\mathfrak{sl}_2)\) case: the finite labels are truncated spins, the factors \(d_i\) are quantum dimensions, and each tetrahedral factor is a quantum \(6j\)-symbol [1]. Thus the categorical formula records the same object while making its structural ingredients explicit.

### Mathematical Context and Formation

The motivating problem was concrete: given a closed 3-manifold by an arbitrary finite triangulation, construct a finite, computable scalar that depends only on the PL homeomorphism type of the manifold, not on that triangulation [1]. The obstacle was presentation dependence. Counts of simplices change under subdivision, and a product of arbitrary local simplex weights also changes when a cluster of tetrahedra is replaced by another cluster filling the same 3-ball. By Pachner's theorem, it is enough—but necessary—to control the local \(2\leftrightarrow3\) and \(1\leftrightarrow4\) bistellar moves [3]. The real problem was therefore to find local data satisfying the exact identities imposed by those moves.

Ordinary triangulation data supplied no such identities, and untruncated representation-theoretic labels would generally produce non-finite sums. Quantum \(\mathfrak{sl}_2\) recoupling at a root of unity supplied the missing combination. Passing to the finite admissible set of labels made the sum finite; attaching a quantum dimension to each edge and a quantum \(6j\)-symbol to each tetrahedron made a tetrahedral replacement an identity in recoupling theory. The Biedenharn–Elliott, or pentagon, identity matches the \(2\leftrightarrow3\) move, while completeness/orthogonality identities together with the global-dimension normalization match the \(1\leftrightarrow4\) move [1]. The state sum was formed by assembling precisely these local factors and summing over all internal labels, so that the algebra required for triangulation independence was built into the definition rather than checked separately for each manifold.

### Essential Role

The Turaev–Viro invariant made the presentation-independence part of the 3-manifold-invariant problem tractable. Instead of comparing two arbitrary triangulations globally, one invokes Pachner moves and checks a fixed finite collection of recoupling identities. Its tetrahedral \(6j\)-factor handles reassociation in a \(2\leftrightarrow3\) replacement; its sum over internal labels implements completeness; its edge dimensions and vertex normalization remove the extra factors introduced by a \(1\leftrightarrow4\) replacement. Root-of-unity truncation simultaneously ensures that the resulting expression is an actual finite sum [1].

Consequently, an arbitrary triangulation becomes usable computational input rather than unwanted auxiliary structure. The invariant does not make triangulations canonical; it bypasses that impossible requirement by arranging that every elementary change of triangulation leaves the total contraction fixed. Structurally, it recasts a global topological invariance question as coherence of local tensor data. This last formulation is an interpretive synthesis of the state-sum mechanism; the precise invariance theorem and its recoupling identities are established results [1,2].

## 3. Notes

The name “Turaev–Viro invariant” is used both for the original root-of-unity quantum-\(\mathfrak{sl}_2\) family and for its spherical-fusion-category generalization, often called the Turaev–Viro–Barrett–Westbury invariant. The latter is used above to state the construction without choosing a particular level. Boundary state spaces and the associated 3-dimensional topological quantum field theory extend the same construction but are outside this archive's single closed-manifold object.

## 4. Sources

[1] V. G. Turaev and O. Ya. Viro, “State sum invariants of 3-manifolds and quantum \(6j\)-symbols,” *Topology* 31 (1992), 865–902. https://doi.org/10.1016/0040-9383(92)90015-A

[2] J. W. Barrett and B. W. Westbury, “Invariants of piecewise-linear 3-manifolds,” *Transactions of the American Mathematical Society* 348 (1996), 3997–4022. https://doi.org/10.1090/S0002-9947-96-01660-1

[3] U. Pachner, “P.L. homeomorphic manifolds are equivalent by elementary shellings,” *European Journal of Combinatorics* 12 (1991), 129–145. https://doi.org/10.1016/S0195-6698(13)80080-7
