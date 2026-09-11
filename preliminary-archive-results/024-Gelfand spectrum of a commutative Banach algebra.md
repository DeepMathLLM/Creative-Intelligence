# Mathematical Object Origin Archive | Gelfand spectrum of a commutative Banach algebra

## 1. Archive Information

- Standard Name: Gelfand spectrum of a commutative Banach algebra
- Mathematical Field: Functional Analysis; Harmonic Analysis
- Abstract: The Gelfand spectrum packages all scalar-valued multiplicative tests on a commutative complex Banach algebra into a compact space. It was formed within the theory of normed rings to make the algebraic problems of invertibility and element spectra tractable; in the convolution algebra \(\ell^1(\mathbb Z)\), it turns Wiener's inverse-closedness problem for absolutely convergent Fourier series into a complete nonvanishing criterion.

## 2. Core Record

### Precise Description

Let \(A\) be a nonzero, unital, commutative complex Banach algebra. Its **Gelfand spectrum** (also called its character space or maximal ideal space) is
\[
\Delta(A)=\{\varphi:A\to\mathbb C:\varphi\text{ is nonzero, complex-linear, and }\varphi(ab)=\varphi(a)\varphi(b)\}.
\]
Every such character is automatically continuous, satisfies \(\varphi(1)=1\), and has norm one. The Gelfand topology on \(\Delta(A)\) is the relative weak-* topology inherited from \(A^*\); equivalently, it is the weakest topology making every evaluation \(\varphi\mapsto\varphi(a)\), \(a\in A\), continuous. With this topology \(\Delta(A)\) is a nonempty compact Hausdorff space [2, 4].

The map \(\varphi\mapsto\ker\varphi\) is a bijection from \(\Delta(A)\) to the maximal ideals of \(A\). Indeed, maximal ideals are closed, and for each maximal ideal \(M\), the quotient \(A/M\) is a complex Banach division algebra, hence isomorphic to \(\mathbb C\) by the Gelfand--Mazur theorem. For \(a\in A\), its Gelfand transform is the continuous function
\[
\widehat a:\Delta(A)\to\mathbb C,\qquad \widehat a(\varphi)=\varphi(a).
\]
It satisfies
\[
\sigma_A(a)=\{\varphi(a):\varphi\in\Delta(A)\}=\widehat a(\Delta(A)),
\qquad
a\in A^\times\Longleftrightarrow 0\notin\widehat a(\Delta(A)).
\]
Thus the Gelfand spectrum of the algebra is distinct from, but simultaneously parametrizes, the scalar spectrum \(\sigma_A(a)\) of every individual element [2, 4].

### Mathematical Context and Formation

A concrete motivating problem is Wiener's inversion problem for absolutely convergent Fourier series. Give \(A=\ell^1(\mathbb Z)\) convolution multiplication,
\[
(a*b)_n=\sum_{k\in\mathbb Z}a_kb_{n-k},
\]
with identity \(\delta_0\). For \(a\in A\), define
\[
F_a(z)=\sum_{n\in\mathbb Z}a_nz^n,\qquad z\in\mathbb T.
\]
The problem asks whether the pointwise condition \(F_a(z)\neq0\) for every \(z\in\mathbb T\) forces \(a\) to possess a convolution inverse \(b\in\ell^1(\mathbb Z)\), equivalently whether \(1/F_a\) again has an absolutely convergent Fourier series. Necessity is immediate from \(F_{a*b}=F_aF_b\), but sufficiency is not: the Fourier transforms of \(\ell^1\)-sequences form a proper subalgebra of \(C(\mathbb T)\), so pointwise division in \(C(\mathbb T)\) does not by itself show that the reciprocal remains in that smaller algebra. Neumann-series arguments settle only special norm-small perturbations of the identity and do not cover arbitrary nowhere-zero \(F_a\) [3].

The decisive algebraic insight is that noninvertibility is detected by maximal ideals. If \(a\) is not invertible, the proper ideal \(Aa\) lies in a maximal ideal \(M\); the analytic completeness of a complex Banach algebra and the Gelfand--Mazur theorem identify \(A/M\) with \(\mathbb C\), turning the quotient map into a character that vanishes at \(a\). Conversely, a character cannot vanish on an invertible element. Gathering every such character into \(\Delta(A)\), rather than selecting ad hoc evaluations separately for each element, therefore yields a single space carrying all scalar obstructions to invertibility. Equipping it with the weak-* topology makes every algebra element a continuous function on that space. This is the mathematical formation embodied in Gelfand's normed-ring theory [1, 2].

For \(A=\ell^1(\mathbb Z)\), the construction recovers exactly the circle that appears in Fourier analysis. A character \(\varphi\) is determined by \(u=\varphi(\delta_1)\); since \(\varphi(\delta_n)=u^n\) for all \(n\in\mathbb Z\) and \(\varphi\) is bounded, one must have \(|u|=1\). Conversely, each \(u\in\mathbb T\) defines
\[
\varphi_u(a)=\sum_{n\in\mathbb Z}a_nu^n.
\]
Hence \(\Delta(\ell^1(\mathbb Z))\cong\mathbb T\), and the Gelfand transform is precisely the Fourier-series transform \(a\mapsto F_a\). The abstract maximal-ideal construction is therefore not an unrelated later application: in this model it isolates the exact evaluations needed by the inversion problem.

### Essential Role

The Gelfand spectrum makes the hard direction of the inversion problem tractable by replacing an internal nonlinear existence question,
\[
a*b=\delta_0\quad\text{for some }b\in\ell^1(\mathbb Z),
\]
with the family of scalar tests
\[
\varphi_u(a)=F_a(u)\neq0\quad\text{for every }u\in\mathbb T.
\]
Its completeness as an obstruction set is the crucial feature: if all characters are nonzero on \(a\) yet \(a\) were noninvertible, a maximal ideal containing \(Aa\) would supply a missing character that vanishes on \(a\), a contradiction. Thus
\[
F_a\text{ nowhere zero on }\mathbb T
\Longleftrightarrow a\in\ell^1(\mathbb Z)^\times,
\]
and the inverse belongs to \(\ell^1(\mathbb Z)\); this is the Banach-algebra mechanism behind Wiener's \(1/f\) theorem [2, 3].

More generally, the same structure solves the well-defined problem class of determining spectra and invertibility in unital commutative complex Banach algebras: \(\sigma_A(a)\) becomes the range of the ordinary continuous function \(\widehat a\) on \(\Delta(A)\). Maximal-ideal completeness supplies all obstructions, multiplicativity turns products and inverses into pointwise operations, and the weak-* topology organizes the tests into a compact function space. The deeper structural change is to regard an abstract commutative Banach algebra as an algebra of functions on its own generalized points, rather than to handle each inverse equation by a separate analytic construction.

## 3. Notes

The Gelfand transform need not be injective or surjective for a general commutative Banach algebra: its kernel is the Jacobson radical, and its image need not equal \(C(\Delta(A))\). For a unital commutative \(C^*\)-algebra, stronger hypotheses yield the isometric Gelfand--Naimark representation \(A\cong C(\Delta(A))\), but that stronger theorem is not part of the object's role in the original inversion problem. For a nonunital commutative Banach algebra, the character space is locally compact rather than necessarily compact, and one may use unitization; the present archive fixes the unital case to state the inversion mechanism without that additional convention.

## 4. Sources

[1] I. Gelfand, “Normierte Ringe,” *Recueil Mathématique (Matematicheskii Sbornik), Nouvelle Série* **9(51)**, no. 1 (1941), 3–24. https://www.mathnet.ru/eng/sm6046

[2] I. M. Gelfand, D. A. Raikov, and G. E. Shilov, *Commutative Normed Rings*, translated by D. E. Brown, Chelsea Publishing, 1964.

[3] Yitzhak Katznelson, *An Introduction to Harmonic Analysis*, 3rd ed., Cambridge University Press, 2004, discussion of Wiener's theorem on absolutely convergent Fourier series.

[4] Christian Remling, “Commutative Banach Algebras,” lecture notes, especially the maximal ideal space and Gelfand transform. https://math.ou.edu/~cremling/teaching/lecturenotes/fa-new/ln8.pdf
