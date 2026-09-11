# Mathematical Object Origin Archive | Idèle Class Group

## 1. Archive Information

- Standard Name: Idèle class group
- Mathematical Field: Algebraic Number Theory
- Abstract: For a number field \(K\), the idèle class group \(C_K\) is the quotient of the restricted product of all local multiplicative groups \(K_v^\times\) by the diagonally embedded group \(K^\times\). It was formed as the single local-global object in which the reciprocity and existence problems of global abelian class field theory can be stated uniformly: its local coordinates retain valuations and unit data at every place, while the quotient imposes the relations coming from global elements.

## 2. Core Record

### Precise Description

Let \(K\) be a number field and let \(v\) range over all its places. Write \(K_v\) for the completion of \(K\) at \(v\), and, for a non-archimedean \(v\), write \(\mathcal O_v\) for its valuation ring. The **idèle group** of \(K\) is the restricted product
\[
J_K=\mathbb A_K^\times:=\prod_v' K_v^\times
 =\left\{(x_v)_v\in\prod_v K_v^\times:
 x_v\in\mathcal O_v^\times\text{ for all but finitely many non-archimedean }v\right\}.
\]
It carries the restricted-product topology with respect to the compact open subgroups \(\mathcal O_v^\times\) at the non-archimedean places. The diagonal map
\[
K^\times\longrightarrow J_K,\qquad a\longmapsto(a)_v,
\]
embeds the global multiplicative group as the subgroup of principal idèles. The **idèle class group** is the quotient topological abelian group
\[
C_K:=J_K/K^\times.
\]
With normalized local absolute values, the finite product \(|x|_{\mathbb A}=\prod_v|x_v|_v\) is defined for every idèle. The product formula makes it trivial on principal idèles, so it descends to \(C_K\); this is one visible instance of the way global relations are imposed by the quotient [1,2].

### Mathematical Context and Formation

The motivating problem class is global abelian class field theory: for a number field \(K\), classify its finite abelian extensions \(L/K\) and express the Galois group through arithmetic reciprocity and norm conditions. Prime ideals and the ideal class group organize valuations effectively and solve the unramified part of this problem, but an ideal records only the integer \(v(x_v)\) at a finite place. It forgets the local-unit component of \(x_v\in K_v^\times\), precisely the component on which ramification and conductor conditions act. Ray class groups restore selected unit congruences for a fixed modulus, but varying the allowed ramification requires varying the modulus; this does not by itself present all local multiplicative data and all conductors inside one topological group. Archimedean sign conditions also require separate treatment in a purely finite-ideal description [1,3].

The formative mathematical idea is therefore to replace the exponent attached to each prime by a full element of the corresponding local group \(K_v^\times\), but to require that element to be a unit at almost every finite place. The restriction to \(\mathcal O_v^\times\) almost everywhere preserves the finite-support feature of ideals and makes products of local reciprocity symbols meaningful, while retaining at the exceptional places the unit information needed for ramification. Taking the restricted product assembles every completion in one locally compact group. Finally, two such local families must be identified when they differ by multiplication by one global element of \(K^\times\): global reciprocity makes the product of the local symbols of a principal idèle equal to the identity. This necessity produces the quotient \(J_K/K^\times\), rather than merely the product \(J_K\), as the natural global object [1,2].

Thus the idèle class group is not just a repackaging of the ordinary ideal class group. Appropriate open local-unit subgroups give ray class quotients, but \(C_K\) retains all places and all levels of local congruence simultaneously. Its topology records conductor conditions as openness and permits finite reciprocity quotients to be handled uniformly [1,3].

### Essential Role

For a finite abelian extension \(L/K\), local class field theory supplies reciprocity maps from \(K_v^\times\) to the relevant decomposition groups. At almost every finite place the extension is unramified and local units have trivial image, so for an idèle \((x_v)_v\) the product of its local reciprocity images has only finitely many nontrivial factors. It therefore defines a global Artin map
\[
\operatorname{rec}_{L/K}:J_K\longrightarrow\operatorname{Gal}(L/K).
\]
The global reciprocity law says that this map is trivial on diagonally embedded \(K^\times\), and hence it factors through \(C_K\). The Artin reciprocity and norm theorems then give the canonical isomorphism
\[
C_K/N_{L/K}(C_L)\;\xrightarrow{\ \sim\ }\;\operatorname{Gal}(L/K),
\]
with the customary consistent choice of reciprocity normalization [1,2]. Conversely, the existence theorem identifies finite abelian extensions of \(K\) with open finite-index subgroups of \(C_K\), those arising from \(L\) being the norm subgroups \(N_{L/K}(C_L)\) [1,3].

Each defining feature of \(C_K\) addresses a specific obstacle in the motivating problem. Its factor \(K_v^\times\) retains both valuation data, which controls Frobenius behavior at unramified primes, and local units, which control inertia and conductor conditions. Restrictedness ensures that the product of local symbols is finite and that the relevant norm or congruence conditions are open. Quotienting by \(K^\times\) incorporates the principal global relation required by reciprocity. Consequently, the many modulus-dependent ray class descriptions become compatible finite quotients of one topological group, and the classification problem becomes the problem of identifying its open finite-index norm subgroups. The deeper structural viewpoint introduced is that global abelian Galois theory is governed by simultaneous local multiplicative data subject to exactly the relations imposed by global multiplicative elements, rather than by ideals alone.

## 3. Notes

The idèle group \(J_K\) and the idèle class group \(C_K\) are distinct objects; the latter is the object archived here. The symbol \(\mathbb A_K^\times\) is commonly used for \(J_K\), the unit group of the adèle ring, while \(C_K\) denotes its quotient by \(K^\times\). The ordinary ideal class group is a finite quotient obtained after discarding archimedean and local-unit information; it should not be identified with \(C_K\). Analogous definitions hold for global function fields, but the formulation of the global reciprocity map has additional degree/constant-field features, so this archive has deliberately fixed the number-field case.

## 4. Sources

[1] Jürgen Neukirch, *Algebraic Number Theory*, translated by Norbert Schappacher, Springer, 1999, Chapter VI, especially the idèle group and global class field theory.

[2] John W. S. Cassels and Albrecht Fröhlich (eds.), *Algebraic Number Theory*, Academic Press, 1967, chapters on local and global class field theory.

[3] André Weil, *Basic Number Theory*, 3rd ed., Springer, 1974, chapters on adèles, idèles, and class field theory.
