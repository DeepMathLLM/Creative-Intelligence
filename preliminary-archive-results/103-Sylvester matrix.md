# Mathematical Object Origin Archive | Sylvester Matrix

## 1. Archive Information

- Standard Name: Sylvester matrix
- Mathematical Field: Commutative Algebra; Algebraic Geometry
- Abstract: The Sylvester matrix is the square coefficient matrix of the bounded-degree map \((u,v)\mapsto uf+vg\) associated with two univariate polynomials. It was formed for the elimination problem of deciding, directly from polynomial coefficients, whether two equations have a common root. Its singularity converts that nonlinear existential condition into one determinant equation, the vanishing of the resultant.

## 2. Core Record

### Precise Description

Let \(R\) be a commutative ring and let
\[
f(x)=a_mx^m+\cdots+a_0,\qquad g(x)=b_nx^n+\cdots+b_0
\]
have fixed positive degrees \(m\) and \(n\). Write \(R[x]_{<r}\) for the free \(R\)-module of polynomials of degree less than \(r\). Multiplication by \(f\) and \(g\) defines an \(R\)-linear map
\[
\Phi_{f,g}:R[x]_{<n}\oplus R[x]_{<m}\longrightarrow R[x]_{<m+n},
\qquad (u,v)\longmapsto uf+vg.
\]
Both source and target have rank \(m+n\). The **Sylvester matrix** \(S(f,g)\) is the matrix of this map in monomial bases. For example, if the multipliers are ordered as
\[
x^{n-1},\ldots,1\quad\text{and}\quad x^{m-1},\ldots,1
\]
and the target basis as \(x^{m+n-1},\ldots,1\), its columns are the coefficient vectors of
\[
x^{n-1}f,\ldots,f,\;x^{m-1}g,\ldots,g.
\]
The frequently printed version places these vectors in rows; it is the transpose and has the same determinant. Other row or block orders can change only the conventional sign.

With the convention above,
\[
\operatorname{Res}_x(f,g):=\det S(f,g)
\]
is the resultant. If \(R=k\) is a field, then
\[
\det S(f,g)=0
\quad\Longleftrightarrow\quad
\gcd(f,g)\ne 1
\quad\Longleftrightarrow\quad
f\text{ and }g\text{ have a common root in }\overline{k}.
\]
Indeed, a common divisor \(d\) gives a nonzero bounded-degree relation
\((g/d)f-(f/d)g=0\). Conversely, a nonzero relation \(uf+vg=0\) within the stated degree bounds cannot exist when \(f\) and \(g\) are coprime: Euclid's lemma would force \(f\mid v\), despite \(\deg v<m\). Over a splitting field, if
\(f=a_m\prod_{i=1}^m(x-\alpha_i)\) and
\(g=b_n\prod_{j=1}^n(x-\beta_j)\), then
\[
\det S(f,g)=a_m^n b_n^m
\prod_{i=1}^m\prod_{j=1}^n(\alpha_i-\beta_j),
\]
which displays the same vanishing criterion [1,2].

### Mathematical Context and Formation

The motivating problem class is **elimination from two polynomial equations**: given \(f(x)=0\) and \(g(x)=0\), determine a condition involving only their coefficients that is necessary and sufficient for the unknown \(x\) to take a common value. In a parameterized system \(F(x,y)=G(x,y)=0\), the corresponding task is to eliminate \(x\) and obtain an equation in the remaining parameter \(y\). This is more specific than separately solving the two equations: the desired output is one uniform algebraic condition for arbitrary prescribed degrees [1,2].

The difficulty is that “there exists \(\alpha\) with \(f(\alpha)=g(\alpha)=0\)” is a nonlinear statement about an unknown lying in an algebraic extension, whereas the available input consists only of coefficients. Explicit root expressions are neither uniform nor required by the problem. Repeated substitution is degree-dependent, and a symbolic Euclidean algorithm introduces divisions and case distinctions when leading coefficients or remainders vanish. Although the gcd criterion characterizes the answer abstractly, it does not by itself present the requested single polynomial eliminant in the input coefficients.

The formative insight is to replace the hidden root by a bounded polynomial syzygy. A common factor exists exactly when there are nonzero \(u,v\), with \(\deg u<n\) and \(\deg v<m\), satisfying \(uf+vg=0\). Equating the \(m+n\) coefficients of this identity gives \(m+n\) homogeneous linear equations in the \(m+n\) coefficients of \(u\) and \(v\). The shifts of the coefficient lists of \(f\) and \(g\) are precisely the columns (or, conventionally, rows) of the Sylvester matrix. Thus a common-root problem forms a square linear system, and the condition for a nonzero syzygy is its determinant's vanishing. This is the mathematical route from elimination to the matrix, rather than merely a later application of an unrelated array [2,3].

### Essential Role

The Sylvester matrix makes the coefficient-level elimination condition tractable. Its shifted blocks record every coefficient of every permitted multiple \(x^if\) and \(x^jg\); the degree bounds make the resulting map square; and singularity detects exactly when these multiples have a nontrivial linear dependence. Consequently, the common-root question is reformulated as
\[
\operatorname{rank}S(f,g)<m+n,
\]
or equivalently as the single coefficient-polynomial equation \(\det S(f,g)=0\). No roots need to be constructed, and no division or branch choice enters the determinant [1,2].

For \(F,G\in k[y][x]\), the same construction over the coefficient ring \(k[y]\) produces \(\det S_x(F,G)\in k[y]\). Every affine common solution \((x_0,y_0)\), subject to the fixed-degree formulation under specialization, forces this polynomial to vanish at \(y_0\). The matrix therefore performs the central step of eliminating \(x\), after which candidate parameter values can be examined in one variable. Degree drops can add projected points at infinity or extraneous specialized candidates, so this statement is deliberately a necessary projection condition without extra hypotheses.

The deeper structural change is that incidence of roots is represented by rank failure of a canonical multiplication map. The determinant called the resultant is the scalar equation extracted from that map, but it is the Sylvester matrix that exposes why the equation exists: common factors are equivalent to bounded syzygies, and bounded syzygies are equivalent to loss of rank.

## 3. Notes

The Sylvester matrix and the resultant should not be conflated: the matrix is the coefficient representation of \(\Phi_{f,g}\), while the resultant is its determinant. Likewise, a subresultant matrix is a related truncation used to recover more information about gcd degree; it is not the object archived here. Over a general commutative ring, the determinant is still defined, but the field-level equivalences with gcds and roots require appropriate hypotheses. Fixed degrees also matter: padding a polynomial with a zero leading coefficient changes the matrix problem and may force its determinant to vanish.

## 4. Sources

[1] I. M. Gelfand, M. M. Kapranov, and A. V. Zelevinsky, *Discriminants, Resultants, and Multidimensional Determinants*, Birkhäuser, 1994, Chapter 1.

[2] David A. Cox, John Little, and Donal O'Shea, *Using Algebraic Geometry*, 2nd ed., Graduate Texts in Mathematics 185, Springer, 2005, Chapter 3.

[3] David A. Cox, *Elimination Theory*, CBMS Regional Conference Series in Mathematics 134, American Mathematical Society, 2024, Chapter 1, https://www.ams.org/bookstore/pspdf/cbms-134-prev.pdf.
