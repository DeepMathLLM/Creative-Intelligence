# Mathematical Object Origin Archive | Lebesgue Integral

## 1. Archive Information

- Standard Name: Lebesgue integral
- Mathematical Field: Harmonic analysis, measure theory, and real analysis
- Abstract: The Lebesgue integral assigns an integral to a measurable function by measuring the sets on which the function takes specified ranges of values and then passing from measurable simple functions to general functions. It arose from the need to integrate bounded, highly discontinuous functions and to make integration stable under limiting processes, a need made concrete by sum-functions and coefficient formulas in Fourier-series problems.

## 2. Core Record

### Precise Description

Let \((X,\Sigma,\mu)\) be a measure space. If
\[
s=\sum_{j=1}^{m} a_j\mathbf 1_{E_j},\qquad a_j\ge 0,
\]
is a nonnegative measurable simple function, with pairwise disjoint \(E_j\in\Sigma\), define
\[
\int_X s\,d\mu=\sum_{j=1}^{m}a_j\mu(E_j),
\]
using the standard extended-arithmetic convention \(0\cdot\infty=0\). For a nonnegative measurable function \(f:X\to[0,\infty]\), define
\[
\int_X f\,d\mu
 =\sup\left\{\int_X s\,d\mu: s\text{ is nonnegative, measurable, simple, and }s\le f\right\}.
\]
For real measurable \(f\), put \(f^+=\max(f,0)\) and \(f^-=\max(-f,0)\). The function is Lebesgue integrable when
\(\int_X |f|\,d\mu<\infty\), and then
\[
\int_X f\,d\mu=\int_X f^+\,d\mu-\int_X f^-\,d\mu.
\]
Complex-valued functions are integrated through their real and imaginary parts. The classical Lebesgue integral on an interval is this construction with Lebesgue measure. The simple-function formulation is the modern measure-theoretic version of Lebesgue's range-based construction [1][2][3].

### Mathematical Context and Formation

A concrete problem was to give meaning to integrals of bounded discontinuous functions that occur in harmonic analysis. If an everywhere convergent trigonometric series has sum \(f\), its formal coefficient formulas require integrals such as
\[
\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\cos(nx)\,dx
\quad\text{and}\quad
\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\sin(nx)\,dx.
\]
Yet a pointwise limit of continuous trigonometric polynomials can have too many discontinuities to be Riemann integrable, so the expressions need not exist in the available Riemann sense. This was not merely a request to calculate an already defined quantity: the coefficient-recovery question itself could become ill-posed because the necessary integral was absent [2][4]. More generally, analysis needed an integral that remained compatible with controlled pointwise limits rather than only with uniform limits.

The obstruction lay in Riemann's use of partitions of the domain into intervals. On every interval, a densely oscillating function can have a large upper-lower discrepancy, no matter how short the interval is. For example, \(\mathbf 1_{\mathbb Q\cap[0,1]}\) has upper Darboux sum \(1\) and lower Darboux sum \(0\) for every partition, although the set on which its value is \(1\) is countable. Thus domain refinement does not distinguish pervasive oscillation occurring on a negligible set from oscillation occupying substantial size. Jordan content, suited to sets with sufficiently regular boundaries, likewise did not supply the countably additive set-size calculus required for arbitrary countable constructions.

The formative insight was to reverse what is grouped together. Instead of first cutting the \(x\)-axis and asking for the variation of \(f\) on each interval, one divides the range of \(f\) into narrow bands and measures the inverse-image sets on which its values fall in those bands. Borel's countable set constructions and measure supplied the necessary set-side mechanism; Lebesgue's construction joined those measured level sets to weighted sums, then obtained general measurable functions as limits of such simple approximants [1][2][4]. In modern form, countable additivity of \(\mu\) yields monotone convergence:
\[
0\le f_k\uparrow f\quad\Longrightarrow\quad
\int f_k\,d\mu\uparrow\int f\,d\mu.
\]
This is exactly the kind of limit compatibility that domain-partition integration lacked [3].

### Essential Role

The Lebesgue integral made the integral expressions in the motivating Fourier problem well-defined for every bounded measurable sum-function on a finite interval: such an \(f\) satisfies
\[
\int_{-\pi}^{\pi}|f|\,dx<\infty,
\]
and multiplication by \(\sin(nx)\) or \(\cos(nx)\) preserves integrability. This removes the preliminary obstruction that the coefficient integrals might not exist. It does not, by definition alone, prove that an arbitrary convergent trigonometric series has those integrals as its original coefficients; that identification is a further uniqueness and convergence theorem. The direct contribution is that the coefficient question is reformulated inside a stable integration theory rather than being undefined.

Three structural features produce this change. First, measurable level sets replace interval-wise oscillation as the elementary data, so irregular placement of discontinuities does not itself prevent integration. In particular,
\[
\int_0^1\mathbf 1_{\mathbb Q}(x)\,dx=0
\]
because the rationals have Lebesgue measure zero, although the function is discontinuous everywhere. Second, equality almost everywhere becomes the relevant equivalence: changing values on a null set leaves the integral unchanged. This separates analytically significant size from pointwise pathology. Third, approximation by simple functions, together with countable additivity, gives convergence principles such as monotone convergence and, under an integrable dominating function, dominated convergence [3]. Consequently, integrals can pass through broad classes of pointwise limits under explicit hypotheses, rather than requiring uniform convergence.

The deeper structural viewpoint is therefore that integration is not fundamentally a sum over thin vertical strips of the domain. It is a pairing of function values with a countably additive notion of the size of their inverse images. That viewpoint simultaneously enlarged the class of integrable functions and exposed the precise hypotheses under which limiting operations used in harmonic analysis are legitimate.

## 3. Notes

The Lebesgue integral is distinct from Lebesgue measure: the measure assigns sizes to measurable sets, while the integral extends the assignment \(\mathbf 1_E\mapsto\mu(E)\) from indicator functions to measurable functions. It also does not integrate every function or settle every limit interchange; measurability and hypotheses such as monotonicity or domination remain essential. On a compact interval, every Riemann-integrable function is Lebesgue integrable with the same value, but the converse fails.

## 4. Sources

[1] H. Lebesgue, “Sur une généralisation de l'intégrale définie,” *Comptes rendus de l'Académie des Sciences*, vol. 132 (1901), pp. 1025–1028.

[2] H. Lebesgue, “Intégrale, longueur, aire,” *Annali di Matematica Pura ed Applicata*, series 3, vol. 7 (1902), pp. 231–359, https://doi.org/10.1007/BF02420592.

[3] T. Tao, *An Introduction to Measure Theory*, Graduate Studies in Mathematics 126, American Mathematical Society, 2011, §§1.3–1.4.

[4] T. Hawkins, *Lebesgue's Theory of Integration: Its Origins and Development*, University of Wisconsin Press, 1970.
