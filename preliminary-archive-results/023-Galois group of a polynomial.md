# Mathematical Object Origin Archive | Galois Group of a Polynomial

## 1. Archive Information

- Standard Name: Galois group of a polynomial
- Mathematical Field: Algebraic Number Theory; Field Theory
- Abstract: The Galois group of a separable polynomial is the group of base-field automorphisms of its splitting field. It was formed to encode, as permutations of the roots, exactly the algebraic symmetries left undetermined by the coefficients. For the problem of solving polynomial equations by radicals, its subgroup structure converts the existence of a radical formula into the precise condition that this finite group be solvable.

## 2. Core Record

### Precise Description

Let $K$ be a field, let $f(x)\in K[x]$ be separable, and let $L$ be a splitting field of $f$ over $K$. The **Galois group of $f$ over $K$** is
\[
\operatorname{Gal}(f/K)=\operatorname{Aut}_K(L),
\]
the group of field automorphisms of $L$ that fix every element of $K$.

If the distinct roots of $f$ in $L$ are $\alpha_1,\ldots,\alpha_n$, every $K$-automorphism of $L$ permutes these roots. Since the roots generate $L$ over $K$, this action is faithful, so $\operatorname{Gal}(f/K)$ is identified with a subgroup of $S_n$. It is not, however, an arbitrary permutation group: its elements preserve every algebraic relation over $K$ among the roots. Because $f$ is separable and $L$ is its splitting field, $L/K$ is a finite Galois extension. The Galois correspondence therefore gives an inclusion-reversing bijection
\[
H\longleftrightarrow L^H
\]
between subgroups $H\leq \operatorname{Gal}(f/K)$ and intermediate fields $K\subseteq L^H\subseteq L$. Different choices of a splitting field yield groups canonically determined only up to the usual transport by a $K$-isomorphism of splitting fields, and hence an isomorphism class independent of the choice.

### Mathematical Context and Formation

The motivating problem class is the solution of polynomial equations over a base field, especially equations over $\mathbb{Q}$, by radicals: determine whether all roots of $f$ can be obtained from its coefficients through finitely many field operations and extractions of $m$th roots. Formulas for degrees two, three, and four encouraged the search for analogous formulas in higher degree, but direct manipulation of coefficients did not reveal what distinguishes equations admitting such formulas from those that do not. The coefficients are symmetric functions of the roots and hence do not themselves record which nonsymmetric expressions in the roots can successively be made available.

The central difficulty is that a radical expression is built through a tower of field extensions, whereas the equation initially presents only an unordered set of roots. One needs to connect the stepwise structure of such a tower to constraints intrinsic to the roots. Permuting the roots supplies that connection. A permutation compatible with all relations over $K$ expresses a symmetry invisible from the base field; an expression in the roots belongs to a particular intermediate field precisely when it is fixed by the corresponding subgroup. Earlier permutation and resolvent methods showed that carefully chosen root expressions could have fewer possible values because some root permutations fixed them. The decisive structural insight is to collect all admissible permutations into one group and to pair its subgroup structure with the intermediate fields generated during a proposed solution. In modern language, this group is $\operatorname{Aut}_K(L)$, acting on the roots.

Thus the group was not introduced merely to label permutations. It answers the inadequacy of coefficient manipulation by retaining exactly the symmetries relevant over $K$, while group multiplication records their composition and subgroups record successive gains of algebraic information. The original solvability question can then be asked as a structural question about a finite group rather than as an unsuccessful search through possible formulas [1][2].

### Essential Role

For fields of characteristic zero, the resulting criterion is exact: a polynomial is solvable by radicals over $K$ if and only if its Galois group over $K$ is a solvable group [1][2]. The mechanism uses the particular structures built into the object. A radical tower, after adjoining the necessary roots of unity and passing to suitable normal closures, produces Galois groups with successive abelian (indeed, in the relevant steps cyclic) quotients. Consequently the automorphism group of the splitting field must have a subnormal series with abelian quotients. Conversely, when $\operatorname{Gal}(f/K)$ has such a series, the Galois correspondence turns the subgroup series into a tower of intermediate fields; after the required roots of unity are adjoined, cyclic extension theory realizes the relevant stages by adjoining radicals.

The Galois group therefore made the obstruction to a radical solution tractable. Rather than proving impossibility by ruling out every conceivable symbolic formula, one can show that the finite group of root symmetries is not solvable. In the generic degree-$n$ problem the relevant group is $S_n$; for $n\geq 5$, $S_n$ is not solvable, which supplies the structural obstruction behind the absence of a universal formula by radicals. This does not say that no polynomial of degree at least five is solvable by radicals: individual polynomials can have smaller solvable Galois groups.

The deeper viewpoint is that a formula for roots is controlled not simply by degree but by the organization of algebraic symmetries. Fixed fields translate symmetry constraints into available quantities, normal subgroups translate into normal intermediate extensions, and abelian quotient groups express the layer-by-layer symmetry reduction achievable by radicals. These features reformulate the equation-solving problem into a correspondence between field constructions and group structure; that reformulation, rather than the many later uses of Galois groups, is the object's direct essential role.

## 3. Notes

The Galois group of a polynomial is the Galois group of its splitting field over the stated base field; changing the base field can change the group. The classical radical-solvability statement above is restricted to characteristic zero to avoid inseparability and positive-characteristic qualifications. It is also important to distinguish the Galois group from the full symmetric group on the roots: the former consists only of permutations induced by base-field automorphisms of the splitting field.

## 4. Sources

[1] David A. Cox, *Galois Theory*, 2nd ed., Wiley, 2012, especially Chapters 6–8.

[2] Ian Stewart, *Galois Theory*, 4th ed., CRC Press, 2015, chapters on solution by radicals and the Galois correspondence.

[3] Jean-Pierre Tignol, *Galois' Theory of Algebraic Equations*, World Scientific, 2001.
