# Mathematical Object Origin Archive | Irreducible Complex Character of a Finite Group

## 1. Archive Information

- Standard Name: Irreducible complex character of a finite group
- Mathematical Field: Representation Theory
- Abstract: An irreducible complex character is the trace function of an irreducible finite-dimensional complex representation of a finite group. Frobenius introduced group characters while solving the problem of factoring the group determinant for an arbitrary finite group, extending Dedekind’s abelian factorization. The character retained exactly the basis-independent, conjugacy-invariant information needed to distinguish irreducible constituents and organize the determinant’s noncommutative factors.

## 2. Core Record

### Precise Description

Let $G$ be a finite group and let
\[
\rho:G\longrightarrow \operatorname{GL}(V)
\]
be a finite-dimensional complex representation. Its **character** is the function
\[
\chi_\rho:G\longrightarrow \mathbb C,\qquad \chi_\rho(g)=\operatorname{tr}(\rho(g)).
\]
If $V$ has no nonzero proper $G$-invariant subspace, then $\rho$ is irreducible and $\chi_\rho$ is an **irreducible complex character**. Its degree is
\[
\chi_\rho(1)=\dim_{\mathbb C}V.
\]
Because trace is unchanged by similarity,
\[
\chi_\rho(hgh^{-1})=\chi_\rho(g),
\]
so every character is a class function. Equivalent complex representations have the same character, and, conversely, a finite-dimensional complex representation of a finite group is determined up to equivalence by its character. With the Hermitian inner product on class functions
\[
\langle \alpha,\beta\rangle_G
 =\frac1{|G|}\sum_{g\in G}\alpha(g)\overline{\beta(g)},
\]
the irreducible characters form an orthonormal basis of the space of complex-valued class functions. Consequently, if $\chi_V$ is the character of a representation $V$, the multiplicity of an irreducible representation with character $\chi$ in $V$ is $\langle\chi_V,\chi\rangle_G$ [3].

### Mathematical Context and Formation

For indeterminates $x_g$ indexed by $g\in G$, the **group determinant** is
\[
\Theta_G(x)=\det\bigl(x_{gh^{-1}}\bigr)_{g,h\in G}.
\]
The concrete problem was to factor this degree-$|G|$ polynomial in a way that reflects the multiplication law of $G. $ For a finite abelian group, Dedekind had obtained a complete product of linear factors indexed, in modern notation, by the homomorphisms $\lambda:G\to\mathbb C^\times$:
\[
\Theta_G(x)=\prod_{\lambda\in\widehat G}
\left(\sum_{g\in G}\lambda(g)x_g\right),
\]
up to replacing $g$ by $g^{-1}$ according to the indexing convention [2].

That mechanism is inadequate for a nonabelian group. One-dimensional homomorphisms factor through the abelianization $G/[G,G]$, so they cannot encode all of the noncommutative multiplication table and do not supply factors whose total degree is $|G|$. The missing constituents are higher-dimensional and therefore cannot contribute scalar linear forms; they contribute determinants of matrix-valued linear forms. Frobenius’s response was to associate numerical functions—group characters—to the irreducible constituents governing those factors, initially within his analysis of the group determinant rather than through the later abstract definition of a representation [1], [2].

In current representation-theoretic notation, Frobenius’s factorization theorem is
\[
\Theta_G(x)=
\prod_{\rho\in\operatorname{Irr}(G)}
\det\left(\sum_{g\in G}x_g\rho(g)\right)^{d_\rho},
\qquad d_\rho=\dim \rho=\chi_\rho(1),
\]
again with a harmless inversion of indices under alternate conventions [3]. Each displayed determinant has degree $d_\rho$, and its exponent is also $d_\rho$; hence $\sum_\rho d_\rho^2=|G|$. In modern structural language, $\Theta_G$ is the determinant of generic left multiplication on the regular module $\mathbb C[G]$, and the factorization follows because the regular representation contains each irreducible $V_\rho$ with multiplicity $d_\rho$. This modern explanation clarifies the insight behind the formation: scalar characters of an abelian group had to be replaced by trace characters of irreducible matrix constituents.

### Essential Role

The irreducible character made the classification and control of the group determinant’s factors tractable without retaining arbitrary matrix bases. Its defining trace has four features directly matched to the obstruction in the problem:

1. **Basis independence:** $\operatorname{tr}(S\rho(g)S^{-1})=\operatorname{tr}(\rho(g))$, so the function records an intrinsic constituent rather than a chosen matrix realization.
2. **Conjugacy invariance:** character values reduce data from individual group elements to conjugacy classes, the natural scalar domain for noncommutative group information.
3. **Additivity and orthogonality:** characters add under direct sums, while their orthogonality isolates irreducible constituents and computes their multiplicities. This replaces an uncontrolled polynomial factor search by a finite decomposition problem in the space of class functions.
4. **Retention of factor data:** the value $\chi(1)=d$ gives both the degree of the associated determinant factor and its multiplicity in $\Theta_G$. Over $\mathbb C$, an irreducible character determines its representation up to equivalence, and equivalent representations give the same polynomial $\det(\sum_g x_g\rho(g))$.

Thus the character did not turn every nonabelian factor into a linear factor; rather, it supplied the invariant scalar label and calculus for the irreducible matrix factors that linear characters could not see. The deeper structural viewpoint is that noncommutative symmetry decomposes into irreducible matrix blocks, while traces provide a basis-free scalar language for detecting and manipulating those blocks. This contribution is specific to the original determinant-factorization problem even though character theory subsequently became a general tool throughout representation theory.

## 3. Notes

An irreducible character should not be confused with a **linear character**. A linear character has degree one and is itself a homomorphism $G\to\mathbb C^\times$; a general irreducible character of degree greater than one is a trace and need not be multiplicative. The formula above uses complex representations; modular characters require different notions, notably Brauer characters, because representations over fields whose characteristic divides $|G|$ need not be semisimple.

## 4. Sources

[1] F. G. Frobenius, “Über Gruppencharaktere,” *Sitzungsberichte der Königlich Preussischen Akademie der Wissenschaften zu Berlin* (1896), 985–1021.

[2] Thomas Hawkins, “The Origins of the Theory of Group Characters,” *Archive for History of Exact Sciences* **7** (1971), 142–170, https://doi.org/10.1007/BF00357354.

[3] Charles W. Curtis and Irving Reiner, *Representation Theory of Finite Groups and Associative Algebras*, Interscience Publishers, 1962; see the treatments of characters, the regular representation, and the group determinant.
