# Mathematical Object Origin Archive | Hardy–Littlewood Singular Series for Waring's Problem

## 1. Archive Information

- Standard Name: Hardy–Littlewood singular series for Waring's problem
- Mathematical Field: Analytic Number Theory
- Abstract: The Hardy–Littlewood singular series is the arithmetic factor in the circle-method asymptotic for representations of an integer as a sum of fixed powers. It was formed to collect, in one convergent object, the contributions from neighborhoods of all rational frequencies and thereby account for congruence effects that a real-volume heuristic misses [1,2].

## 2. Core Record

### Precise Description

Fix integers \(k\ge 2\), \(s\ge 1\), and \(n\ge 1\), and write \(e(t)=e^{2\pi i t}\). For \(q\ge 1\) and \(a\in\mathbb Z\), define the complete \(k\)-th-power exponential sum
\[
S_k(q,a)=\sum_{r\bmod q} e\!\left(\frac{a r^k}{q}\right).
\]
The singular series attached to the equation
\[
x_1^k+\cdots+x_s^k=n
\]
is
\[
\mathfrak S_{s,k}(n)
 =\sum_{q=1}^{\infty} A_{s,k}(q;n),
\qquad
A_{s,k}(q;n)
 =q^{-s}\!\sum_{\substack{a\bmod q\\(a,q)=1}}
 S_k(q,a)^s e\!\left(-\frac{an}{q}\right).
\]
Convergence is not automatic for every \((s,k)\); it is established in the ranges in which the relevant circle-method theorem is applied [2]. When the series converges absolutely, the Chinese remainder theorem makes \(A_{s,k}(q;n)\) multiplicative in \(q\), so
\[
\mathfrak S_{s,k}(n)=\prod_p \sigma_p(n),
\qquad
\sigma_p(n)=\sum_{h=0}^{\infty} A_{s,k}(p^h;n).
\]
This Euler product has a direct local interpretation. If
\[
M_p(h;n)=\#\bigl\{(x_1,\ldots,x_s)\bmod p^h:
 x_1^k+\cdots+x_s^k\equiv n\pmod {p^h}\bigr\},
\]
then character orthogonality gives
\[
p^{-h(s-1)}M_p(h;n)=\sum_{j=0}^{h}A_{s,k}(p^j;n).
\]
Consequently, whenever the limit and Euler product are justified,
\[
\sigma_p(n)=\lim_{h\to\infty}p^{-h(s-1)}M_p(h;n),
\]
so the singular series is a product of normalized \(p\)-adic solution densities rather than an unexplained correction constant.

### Mathematical Context and Formation

The motivating problem is the asymptotic form of Waring's problem: for fixed \(k\) and sufficiently large \(s\), estimate the number \(R_{s,k}(n)\) of representations of a large integer \(n\) as \(x_1^k+\cdots+x_s^k\), with an estimate strong enough to imply existence. With \(P=\lfloor n^{1/k}\rfloor\) and
\[
f(\alpha)=\sum_{1\le x\le P}e(\alpha x^k),
\]
Fourier orthogonality gives the exact identity
\[
R_{s,k}(n)=\int_0^1 f(\alpha)^s e(-n\alpha)\,d\alpha.
\]
The identity alone does not expose a main term. A continuous scaling argument near \(\alpha=0\) predicts its real-size factor, of order \(n^{s/k-1}\), but is inadequate arithmetically: the phase \(\alpha x^k\) also becomes highly organized whenever \(\alpha\) is close to a reduced rational \(a/q\) of small denominator. Moreover, solvability can depend on congruences modulo every prime power, so a single real integral cannot distinguish an admissible integer from one excluded by local arithmetic.

The decisive circle-method insight is therefore to treat all such rational neighborhoods as major arcs rather than regard only \(0\) as the source of the main term. Near \(\alpha=a/q+\beta\), separating \(x\) into residue classes modulo \(q\) yields the approximation
\[
f(a/q+\beta)\approx q^{-1}S_k(q,a)v(\beta),
\qquad
v(\beta)=\int_0^P e(\beta t^k)\,dt.
\]
After this approximation is raised to the \(s\)-th power and inserted into the representation integral, its dependence on \(\beta\) produces the real singular integral, while the coefficients from all reduced \(a/q\) produce exactly the terms \(A_{s,k}(q;n)\). Summing over denominators forms \(\mathfrak S_{s,k}(n)\). Thus the singular series arose from the need to assemble infinitely many rational-frequency main contributions without losing the congruence information carried by their complete exponential sums; this is the structure used in Hardy and Littlewood's treatment of Waring's problem [1].

### Essential Role

The singular series makes the arithmetic part of the major-arc calculation tractable. Each factor \(S_k(q,a)\) records how \(k\)-th powers are distributed modulo \(q\), the twist \(e(-an/q)\) selects the target integer, and the normalization \(q^{-s}\) puts contributions from different moduli on the scale needed for summation. Instead of analyzing every rational peak independently, one obtains a single coefficient multiplying the real main term.

In a range where the major-arc approximation is uniform, the minor-arc integral is smaller, and the series converges with suitable control, this separation yields an asymptotic of the form
\[
R_{s,k}(n)
 =\frac{\Gamma(1+1/k)^s}{\Gamma(s/k)}
   \mathfrak S_{s,k}(n)n^{s/k-1}
   +o\!\left(n^{s/k-1}\right)
\]
(with the precise counting convention reflected in the real factor) [2]. The Euler-product description then reformulates the potentially opaque issue of whether the main coefficient vanishes as a family of local density questions. A congruence obstruction is visible through a vanishing local factor; under the usual nonsingularity and sufficiently-many-variables hypotheses, local solvability supplies positive local densities and hence the positive arithmetic coefficient needed to turn the asymptotic into a representation theorem.

Its direct contribution is therefore not the minor-arc cancellation itself. Rather, it overcomes the failure of a purely real heuristic by retaining and coherently combining all modular biases in the major-arc main term. It also introduces the structural local-to-global viewpoint that the expected number of integral representations is the real density multiplied by the product of all \(p\)-adic densities.

## 3. Notes

The singular series should not be confused with the singular integral: the former is the non-Archimedean arithmetic factor built from congruences, while the latter is the Archimedean factor obtained from the continuous model. Absolute convergence, positivity, and uniform bounds for \(\mathfrak S_{s,k}(n)\) require hypotheses and are not consequences of the formal definition alone. “Singular series” also names analogous arithmetic factors for other additive Diophantine equations; this archive concerns the Waring form specifically.

## 4. Sources

[1] G. H. Hardy and J. E. Littlewood, “Some Problems of ‘Partitio Numerorum’; IV: The Singular Series in Waring's Problem and the Value of the Number \(G(k)\),” *Mathematische Zeitschrift* **12** (1922), 161–188. https://doi.org/10.1007/BF01482074

[2] R. C. Vaughan, *The Hardy–Littlewood Method*, 2nd ed., Cambridge Tracts in Mathematics 125, Cambridge University Press, 1997.
