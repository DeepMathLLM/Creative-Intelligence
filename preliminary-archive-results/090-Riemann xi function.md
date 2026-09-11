# Mathematical Object Origin Archive | Riemann Xi Function

## 1. Archive Information

- Standard Name: Riemann xi function
- Mathematical Field: Analytic Number Theory
- Abstract: The Riemann xi function is the entire, functionally symmetric completion of the Riemann zeta function. It was formed in the analytic study of how primes are distributed: its zeros are exactly the nontrivial zeta zeros that govern the fluctuating terms in explicit prime-counting formulas.

## 2. Core Record

### Precise Description

For \(s\in\mathbb C\), the Riemann xi function is
\[
\xi(s)=\frac12 s(s-1)\pi^{-s/2}\Gamma\!\left(\frac{s}{2}\right)\zeta(s),
\]
where the expression is understood by analytic continuation. The apparent singularities cancel, so \(\xi\) is an entire function of order one. It obeys
\[
\xi(s)=\xi(1-s),\qquad
\xi(\overline{s})=\overline{\xi(s)},
\]
and \(\xi(0)=\xi(1)=\tfrac12\). Its zeros, with multiplicity, are precisely the nontrivial zeros \(\rho\) of \(\zeta\), namely those in \(0<\operatorname{Re}\rho<1\). The zeta pole at \(s=1\), the corresponding pole at \(s=0\) of the completed zeta function, and the gamma-factor behavior at the trivial zeta zeros have all been canceled in forming \(\xi\) [2,3].

As an entire function of order one, \(\xi\) admits a Hadamard product, for example in canonical-product form
\[
\xi(s)=e^{A+Bs}\prod_{\rho}
\left(1-\frac{s}{\rho}\right)e^{s/\rho},
\]
with the product taken over its zeros using an appropriate convergence convention. The symmetry \(s\mapsto1-s\) organizes those zeros around the critical line \(\operatorname{Re}s=\tfrac12\) [2,4].

### Mathematical Context and Formation

The motivating problem was to determine the distribution of prime numbers, concretely the behavior of \(\pi(x)=\#\{p\le x:p\text{ prime}\}\), including the discrepancy between prime-counting functions and their smooth approximations. Euler's product
\[
\zeta(s)=\prod_p(1-p^{-s})^{-1}
\]
and its logarithmic derivative encode primes and prime powers, but initially only in the half-plane \(\operatorname{Re}s>1\):
\[
-\frac{\zeta'(s)}{\zeta(s)}
 =\sum_{n=1}^{\infty}\frac{\Lambda(n)}{n^s}.
\]
Elementary counting and this restricted Dirichlet-series identity did not reach the complex region whose singularities control the error in prime counting. Even after meromorphic continuation, bare \(\zeta(s)\) carries a pole at \(1\), trivial zeros, and a functional equation containing gamma and trigonometric factors. Thus its zero data are mixed with singularities forced by the continuation rather than solely with the nontrivial zeros relevant to prime-distribution fluctuations [1,2].

The decisive structural input is the theta transformation. If
\[
\theta(x)=\sum_{n\in\mathbb Z}e^{-\pi n^2x},
\qquad \theta(x)=x^{-1/2}\theta(1/x),
\]
then for \(\operatorname{Re}s>1\),
\[
\pi^{-s/2}\Gamma\!\left(\frac{s}{2}\right)\zeta(s)
=\frac12\int_0^\infty (\theta(x)-1)x^{s/2-1}\,dx.
\]
Splitting this Mellin integral at \(1\) and applying the theta transformation produces a meromorphic continuation symmetric under \(s\leftrightarrow1-s\), with only simple poles at \(0\) and \(1\). Multiplication by \(\tfrac12s(s-1)\) removes those two poles. The resulting \(\xi(s)\) is therefore entire, retains exactly the nontrivial zeta zeros, and expresses the functional equation in the transparent form \(\xi(s)=\xi(1-s)\) [1,2]. This completion was formed within Riemann's treatment of the number of primes below a given magnitude, rather than being a later object merely applied to prime counting [1].

### Essential Role

The xi function made the zero-controlled part of the prime-distribution problem amenable to the theory of entire functions. Its finite order and absence of poles permit Hadamard factorization directly through the nontrivial zeros. Logarithmic differentiation gives
\[
\frac{\xi'(s)}{\xi(s)}
=\frac1s+\frac1{s-1}-\frac12\log\pi
 +\frac12\frac{\Gamma'(s/2)}{\Gamma(s/2)}
 +\frac{\zeta'(s)}{\zeta(s)},
\]
so the prime-power Dirichlet series \(-\zeta'/\zeta\) can be compared with a sum over the zeros of an entire function. Contour inversion then converts this comparison into an explicit formula. For example, if \(x>1\) is not a prime power and \(\psi(x)=\sum_{n\le x}\Lambda(n)\), then, with the zero sum symmetrically interpreted,
\[
\psi(x)=x-\sum_{\rho}\frac{x^\rho}{\rho}
-\log(2\pi)-\frac12\log(1-x^{-2}).
\]
Here the main term comes from the zeta pole, the final displayed corrections come from the archimedean/trivial-zero factors, and the oscillatory discrepancy is carried by the nontrivial zeros \(\rho\), exactly the zeros retained by \(\xi\) [2,4].

Thus the definition addresses three linked obstacles at once: the gamma factor extends and symmetrizes the analytic setting supplied by the theta transformation; \(s(s-1)\) removes the remaining poles; and the resulting entire function isolates the nontrivial zero set for factorization. The location of those zeros then becomes a precise reformulation of the attainable error bounds in prime counting. In particular, the Riemann hypothesis is equivalently the assertion that every zero of \(\xi\) has real part \(\tfrac12\). The xi function did not itself prove the prime number theorem or the Riemann hypothesis; its direct contribution was to turn the previously entangled analytic data into a symmetric entire object whose zeros could be related systematically to prime-counting fluctuations [1,2,4].

## 3. Notes

A common modern convention writes \(\Xi(t)=\xi(\tfrac12+it)\). Then \(\Xi\) is an even entire function of \(t\) and is real for real \(t\). Older sources vary in their use of lower-case \(\xi\) and upper-case \(\Xi\); the object archived here is the standard modern \(s\)-variable function defined above.

The Riemann zeta function is a related but distinct object: it retains its pole, trivial zeros, Euler product, and Dirichlet series. The xi function is specifically its pole-free symmetric completion.

## 4. Sources

[1] B. Riemann, “Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse,” *Monatsberichte der Königlich Preussischen Akademie der Wissenschaften zu Berlin* (1859), 671–680; English translation in H. M. Edwards, *Riemann's Zeta Function*.

[2] H. M. Edwards, *Riemann's Zeta Function*, Dover Publications, 2001, especially Chapters 1–2.

[3] NIST Digital Library of Mathematical Functions, Chapter 25, “Zeta and Related Functions,” especially §§25.2, 25.4, and 25.10, https://dlmf.nist.gov/25.

[4] E. C. Titchmarsh, revised by D. R. Heath-Brown, *The Theory of the Riemann Zeta-Function*, 2nd ed., Oxford University Press, 1986, Chapters 2 and 3.
