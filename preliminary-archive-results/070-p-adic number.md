# Mathematical Object Origin Archive | p-adic Number

## 1. Archive Information

- Standard Name: p-adic number
- Mathematical Field: Algebraic Number Theory
- Abstract: For a fixed prime \(p\), a p-adic number is an element of the field \(\mathbb{Q}_p\), obtained by completing \(\mathbb{Q}\) for the absolute value that measures divisibility by \(p\). The object gives a single exact home for compatible arithmetic information modulo \(p, p^2, p^3,\ldots\). It formed around the problem of passing coherently from finite congruence solutions and factorizations to an exact local solution or factorization at the prime \(p\).

## 2. Core Record

### Precise Description

Fix a prime \(p\). For \(x\in\mathbb{Q}^{\times}\), write \(x=p^m a/b\) with \(p\nmid ab\), and define
\[
v_p(x)=m,\qquad |x|_p=p^{-v_p(x)},
\]
with \(|0|_p=0\). This non-Archimedean absolute value satisfies
\[
|x+y|_p\leq \max\{|x|_p,|y|_p\}.
\]
The field \(\mathbb{Q}_p\) is the metric completion of \(\mathbb{Q}\) with respect to \(d_p(x,y)=|x-y|_p\); its elements are the p-adic numbers. Its valuation ring is
\[
\mathbb{Z}_p=\{x\in\mathbb{Q}_p:|x|_p\leq 1\},
\]
the ring of p-adic integers. There is a canonical ring isomorphism
\[
\mathbb{Z}_p\cong \varprojlim_n \mathbb{Z}/p^n\mathbb{Z},
\]
where the transition maps are reduction modulo lower powers. Thus a p-adic integer is equivalently a compatible sequence \((a_n)_{n\geq 1}\) satisfying \(a_{n+1}\equiv a_n\pmod{p^n}\). Every nonzero \(x\in\mathbb{Q}_p\) has a unique convergent expansion
\[
x=\sum_{k=m}^{\infty}a_kp^k,
\qquad m\in\mathbb{Z},\quad a_k\in\{0,1,\ldots,p-1\},\quad a_m\neq 0.
\]
These completion, compatible-residue, and digit-expansion descriptions express the same object in modern terms [2,3].

### Mathematical Context and Formation

The motivating problem class was local arithmetic at a fixed prime: given a polynomial equation or factorization with integral coefficients, how can information modulo \(p\) be refined through \(p^2,p^3,\ldots\), and when does a compatible sequence of finite refinements amount to one exact algebraic solution? A residue class modulo one power \(p^n\) carries only finite precision. Treating every quotient \(\mathbb{Z}/p^n\mathbb{Z}\) separately does not itself turn an unbounded tower of compatible approximations into an element of a field on which addition, multiplication, limits, and polynomial evaluation can be performed at infinite precision. The ordinary real metric is also mismatched to this arithmetic refinement: two integers differing by a high power of \(p\) are very close for congruence purposes but need not be close in the usual absolute value.

Hensel's formation of p-adic numbers exploited the analogy between arithmetic at a prime and algebraic-function theory at a point. Just as powers of a local parameter organize a power-series expansion, increasing powers of \(p\) can organize successively finer congruence data. Hensel first presented the construction through such prime-based series in his program for algebraic number theory [1]. The modern valuation and completion language used above was a later precise reformulation of that organizing idea [2]. It makes divisibility into proximity: if \(x,y\in\mathbb{Z}_p\), then
\[
x\equiv y\pmod{p^n}\quad\Longleftrightarrow\quad |x-y|_p\leq p^{-n}.
\]
Consequently, increasingly accurate compatible congruence approximations form a Cauchy sequence and have an exact p-adic limit.

For a concrete instance, consider \(f(X)=X^2-7\) at \(p=3\). The class \(1\pmod 3\) is a root of \(f\), and \(f'(1)=2\not\equiv0\pmod3\). Successively solving the equation modulo \(3^2,3^3,\ldots\) therefore produces one compatible chain above that class. No fixed residue ring contains the entire chain, and its ordinary real representatives need not approach a real number. In \(\mathbb{Z}_3\), however, the chain is one exact root of \(X^2-7\). This example represents the finite-to-infinite passage for which the object is designed; it does not assert that the p-adic root is a rational or integral root [2,4].

### Essential Role

The p-adic number makes the limiting step in congruence problems an internal algebraic operation rather than an informal succession of modular calculations. Completeness ensures that a sequence stabilized modulo every prescribed \(p^n\) converges, while the ultrametric ensures that agreement to higher \(p\)-power precision means greater closeness. Since field operations and polynomial evaluation are continuous in this metric, compatible approximate arithmetic can be passed to an exact limit.

For polynomial equations, this mechanism is captured by the simple-root form of Hensel's lemma: if \(f\in\mathbb{Z}_p[X]\), \(a_1\in\mathbb{Z}/p\mathbb{Z}\),
\[
f(a_1)\equiv0\pmod p,\qquad f'(a_1)\not\equiv0\pmod p,
\]
then \(a_1\) lifts uniquely to \(a\in\mathbb{Z}_p\) with \(f(a)=0\) [2,4]. Thus the object directly overcomes the gap between roots known at finitely many modular precisions and an exact root carrying all compatible precisions at once. Parallel lifting statements for coprime polynomial factors make local factorization tractable in the same way.

The deeper structural viewpoint is local rather than merely computational: \(\mathbb{Q}_p\) isolates arithmetic controlled by one prime, as the real completion isolates the usual absolute value. It allows a global equation over \(\mathbb{Q}\) or \(\mathbb{Z}\) to be tested and analyzed one completion at a time. This contribution has a strict limitation: a rational or integral solution yields a solution in every relevant completion, but p-adic solvability, even for every \(p\), is not in general sufficient for a global solution. The p-adic object reformulates and solves the coherence problem for local congruence data; it does not by itself solve the global Diophantine problem.

## 3. Notes

The p-adic number should not be conflated with the p-adic integer. The latter is an element of the compact open subring \(\mathbb{Z}_p\), whereas
\[
\mathbb{Q}_p=\bigcup_{r\geq0}p^{-r}\mathbb{Z}_p
\]
and may contain expansions with finitely many negative powers of \(p\). Nor is a p-adic expansion a divergent real series being assigned an arbitrary value: convergence is taken in the explicitly defined p-adic metric. Hensel's original series presentation and the modern completion/inverse-limit presentations belong to different stages of formulation, although they encode the same local arithmetic object [1,2].

## 4. Sources

[1] Kurt Hensel, “Über eine neue Begründung der Theorie der algebraischen Zahlen,” *Jahresbericht der Deutschen Mathematiker-Vereinigung* **6** (1897), 83–88, https://eudml.org/doc/144593.

[2] Fernando Q. Gouvêa, *p-adic Numbers: An Introduction*, 2nd ed., Universitext, Springer, 1997.

[3] Neal Koblitz, *p-adic Numbers, p-adic Analysis, and Zeta-Functions*, 2nd ed., Graduate Texts in Mathematics 58, Springer, 1984.

[4] Keith Conrad, “Hensel’s Lemma,” expository notes, https://kconrad.math.uconn.edu/blurbs/gradnumthy/hensel.pdf.
