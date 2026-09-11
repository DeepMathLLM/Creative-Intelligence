# Mathematical Object Origin Archive | Cotangent Complex

## 1. Archive Information

- Standard Name: Cotangent complex
- Mathematical Field: Homological algebra; commutative algebra; algebraic geometry
- Abstract: For a homomorphism of commutative rings \(A\to B\), the cotangent complex \(L_{B/A}\) is the derived replacement for the module of Kähler differentials. It arose from the problem of constructing a cohomology theory for commutative algebras that records relations and higher relations and thereby controls square-zero extensions and infinitesimal deformation problems. Its essential move is to resolve \(B\) by polynomial \(A\)-algebras before applying differentials, so that nonlinear algebraic lifting questions become linear calculations in a derived category.

## 2. Core Record

### Precise Description

Let \(A\to B\) be a homomorphism of commutative rings. Choose an augmented simplicial \(A\)-algebra \(P_\bullet\to B\) that resolves \(B\) and whose terms are polynomial \(A\)-algebras. Form the simplicial \(B\)-module
\[
\Omega^1_{P_\bullet/A}\otimes_{P_\bullet}B.
\]
The associated normalized chain complex is the cotangent complex
\[
L_{B/A}:=N\!\left(\Omega^1_{P_\bullet/A}\otimes_{P_\bullet}B\right)\in D(B).
\]
Its quasi-isomorphism class is independent of the chosen polynomial resolution. It has a canonical augmentation \(L_{B/A}\to\Omega^1_{B/A}\) inducing \(H_0(L_{B/A})\cong\Omega^1_{B/A}\). If \(B\) is a polynomial \(A\)-algebra, then \(L_{B/A}\simeq\Omega^1_{B/A}\) concentrated in degree zero [3].

For a \(B\)-module \(M\), André–Quillen cohomology may be expressed as
\[
D^n(B/A;M)=\operatorname{Ext}^n_B(L_{B/A},M),
\]
with \(D^0(B/A;M)\cong\operatorname{Der}_A(B,M)\). For composable maps \(A\to B\to C\), the transitivity triangle
\[
L_{B/A}\otimes_B^{\mathbf L}C\longrightarrow L_{C/A}\longrightarrow L_{C/B}\longrightarrow
\bigl(L_{B/A}\otimes_B^{\mathbf L}C\bigr)[1]
\]
relates the corresponding relative complexes [3].

### Mathematical Context and Formation

The motivating problem class is the infinitesimal extension and lifting theory of commutative algebras. Given an \(A\)-algebra \(B\) and a \(B\)-module \(M\), one wants to classify square-zero \(A\)-algebra extensions
\[
0\longrightarrow M\longrightarrow B'\longrightarrow B\longrightarrow0,
\qquad M^2=0,
\]
and, more generally, to decide whether algebra maps and algebraic structures lift across square-zero surjections. A satisfactory theory should identify infinitesimal automorphisms, deformation classes, and obstructions, and it should behave coherently when ring maps are composed.

Kähler differentials solve only the degree-zero linearization: the universal property
\[
\operatorname{Hom}_B(\Omega^1_{B/A},M)\cong\operatorname{Der}_A(B,M)
\]
represents derivations. They do not by themselves retain the higher relation data needed for extension and obstruction classes. Concretely, if \(B=P/I\) with \(P\) polynomial over \(A\), the conormal sequence
\[
I/I^2\longrightarrow\Omega^1_{P/A}\otimes_P B\longrightarrow\Omega^1_{B/A}\longrightarrow0
\]
shows that \(\Omega^1_{B/A}\) is only the cokernel of the first-order relation map. Its kernel and the successive relations among relations are not visible in that module. Keeping merely the displayed presentation also fails to provide, for arbitrary \(B\), a presentation-independent record of all higher syzygies. Moreover, commutative \(A\)-algebras form a nonlinear category, so deriving only after passing to ordinary \(B\)-modules does not recover the missing algebraic relation structure.

The decisive construction is therefore to replace \(B\) inside the category of commutative \(A\)-algebras by a simplicial polynomial resolution and only then apply the universal linearization \(P\mapsto\Omega^1_{P/A}\). Tensoring levelwise with \(B\) and passing to normalized chains preserves the successive relation data while removing dependence on a chosen presentation. In this sense, the cotangent complex is the derived linearization of a commutative algebra. This construction underlies the independently developed André–Quillen (co)homology of commutative rings [1][2] and its scheme-theoretic deformation-theoretic formulation [4].

### Essential Role

The cotangent complex makes the square-zero extension problem tractable by converting it from a classification of ring multiplications into a derived module problem. For every \(B\)-module \(M\), equivalence classes of square-zero \(A\)-algebra extensions of \(B\) by \(M\) are classified by
\[
\operatorname{Ext}^1_B(L_{B/A},M),
\]
while infinitesimal automorphisms are measured in degree zero by
\(\operatorname{Hom}_{D(B)}(L_{B/A},M)\cong\operatorname{Der}_A(B,M)\) [4]. Thus the degree-zero part retains the familiar universal derivation, whereas the higher homological degrees retain precisely the relation data that \(\Omega^1_{B/A}\) discards.

The same mechanism reformulates lifting problems. A proposed lift across a square-zero thickening yields, in cotangent-complex obstruction theory, a class in a derived \(\operatorname{Ext}\) group; vanishing is the existence condition, and the neighboring groups describe choices and automorphisms, with the exact degrees determined by the particular lifting diagram [4]. This is not merely an application of a generic complex: polynomial resolutions make the construction invariant under presentation, and the transitivity triangle separates deformation data contributed by successive maps \(A\to B\to C\). The resulting long exact sequences provide the compatibility that the single module \(\Omega^1_{B/A}\) lacks. The deeper structural viewpoint is that singularities and infinitesimal behavior are encoded by a derived cotangent object whose positive homology measures failures of the underived differential module to capture higher relations.

## 3. Notes

The cotangent complex is distinct from both the module of Kähler differentials and the two-term naive cotangent complex attached to one presentation. The latter models the low-degree truncation in general and gives the full cotangent complex under additional hypotheses such as a local complete-intersection presentation; the simplicial construction is needed without such hypotheses [3]. André and Quillen independently developed the relevant (co)homology theory for commutative algebras, while Illusie developed the cotangent complex systematically for schemes and deformation theory [1][2][4].

## 4. Sources

[1] Michel André, *Homologie des algèbres commutatives*, Die Grundlehren der mathematischen Wissenschaften 206, Springer-Verlag, 1974.

[2] Daniel Quillen, “On the (co-)homology of commutative rings,” in *Applications of Categorical Algebra*, Proceedings of Symposia in Pure Mathematics 17, American Mathematical Society, 1970, pp. 65–87.

[3] The Stacks Project Authors, “The Cotangent Complex,” especially Sections 92.3 and 92.7, https://stacks.math.columbia.edu/tag/08P5 and https://stacks.math.columbia.edu/tag/08PL.

[4] Luc Illusie, *Complexe cotangent et déformations I*, Lecture Notes in Mathematics 239, Springer-Verlag, 1971.
