# Mathematical Object Origin Archive | Lévy Measure

## 1. Archive Information

- Standard Name: Lévy measure
- Mathematical Field: Probability Theory and Stochastic Processes
- Abstract: A Lévy measure is the measure that records the size-dependent intensity of the jump component of an infinitely divisible distribution or Lévy process. It arose within the problem of characterizing all probability laws that possess convolution roots of every order. Its integrability condition permits infinitely many small jumps while making their compensated characteristic exponent well defined, thereby supplying the non-Gaussian part of the Lévy–Khintchine classification.

## 2. Core Record

### Precise Description

A **Lévy measure** on \(\mathbb{R}^d\) is a Borel measure \(\nu\) on \(\mathbb{R}^d\setminus\{0\}\) satisfying
\[
\int_{\mathbb{R}^d\setminus\{0\}} (1\wedge \|x\|^2)\,\nu(dx)<\infty.
\]
Equivalently, it has finite mass outside every neighborhood of the origin, while its mass near the origin may be infinite but must have finite second-moment weight. If it is regarded as a measure on all of \(\mathbb{R}^d\), one also imposes \(\nu(\{0\})=0\).

Its defining classification role is expressed by the Lévy–Khintchine formula. A probability law \(\mu\) on \(\mathbb{R}^d\) is infinitely divisible if and only if, for a fixed truncation convention, there are \(\gamma\in\mathbb{R}^d\), a symmetric positive-semidefinite matrix \(Q\), and a Lévy measure \(\nu\) such that
\[
\widehat\mu(u)
=
\exp\!\left(
 i\langle \gamma,u\rangle
 -\frac12\langle u,Qu\rangle
 +\int_{\mathbb{R}^d\setminus\{0\}}
 \left(e^{i\langle u,x\rangle}-1-i\langle u,x\rangle\mathbf 1_{\{\|x\|\le 1\}}\right)\nu(dx)
\right).
\]
For this truncation, the triplet \((\gamma,Q,\nu)\) is unique; in particular, \(\nu\) is intrinsic, whereas changing the truncation function changes the drift parameter but not the Lévy measure [1,2]. For a Lévy process \((X_t)_{t\ge0}\), the same exponent is multiplied by \(t\). Moreover, if \(B\subset\mathbb{R}^d\setminus\{0\}\) is Borel and bounded away from \(0\), then the number \(N_t(B)\) of jumps up to time \(t\) with sizes in \(B\) is Poisson with mean \(t\nu(B)\). Thus \(\nu\) is literally the jump-intensity measure away from the accumulation point \(0\) [2].

### Mathematical Context and Formation

The motivating problem was to characterize the possible laws of sums whose subdivision can be continued indefinitely. Concretely, a probability measure \(\mu\) is infinitely divisible when, for every \(n\ge1\), one can find a probability measure \(\mu_n\) with \(\mu=\mu_n^{*n}\). These are precisely the one-time marginal laws that can occur in weakly continuous convolution semigroups, and hence in Lévy processes. The problem is not merely to exhibit examples, but to give necessary and sufficient structural data for every such law [1,2].

Passing to characteristic functions turns convolution roots into an exponent: \(\widehat\mu(u)=e^{\Psi(u)}\). The difficulty is to determine which exponents \(\Psi\) are admissible. Drift and Gaussian covariance describe deterministic and continuous fluctuation components, but do not describe discontinuous limits. A finite compound-Poisson model adds a finite measure of jump sizes and contributes \(\int(e^{i\langle u,x\rangle}-1)\,\nu(dx)\). That finite-measure description is still inadequate: limits of triangular arrays and increment laws can contain infinitely many small jumps in every finite time interval, so the relevant jump-size measure can have \(\nu(\mathbb{R}^d\setminus\{0\})=\infty\).

The decisive formulation is to retain local finiteness away from zero but weaken finiteness near zero to
\(\int_{\|x\|\le1}\|x\|^2\nu(dx)<\infty\), while compensating the linear contribution of small jumps. Indeed,
\[
e^{i\langle u,x\rangle}-1-i\langle u,x\rangle=O(\|x\|^2)
\quad(x\to0),
\]
so the Lévy-measure condition makes the compensated integral finite even when \(\nu\) has infinite mass near \(0\). The remaining finite mass for \(\|x\|>1\) handles large jumps as an ordinary Poisson component. This pairing of a measure with a precise integrability condition and a compensation term is what turns a collection of finite-jump approximations into a stable object capable of describing all jump limits. It is the measure component in the Lévy–Khintchine representation developed in the classification of infinitely divisible laws [1,3].

### Essential Role

The Lévy measure makes the jump part of the classification problem tractable. Before it is introduced, the requirement of convolution roots at every scale is global and implicit: it does not reveal what non-Gaussian mechanisms can produce the law. The Lévy measure replaces that condition, for the discontinuous component, by concrete data indexed by jump size. Its finite mass away from zero yields finitely many jumps larger than any fixed threshold, while its weighted integrability near zero permits an infinite cloud of small jumps. The subtraction of the linear term in the exponent neutralizes the otherwise divergent first-order contribution of that cloud.

These features do more than provide notation. They establish both directions of the structural result: every infinitely divisible law has a uniquely determined jump measure, and every measure satisfying the Lévy integrability condition contributes a valid jump exponent which, together with drift and Gaussian covariance, determines an infinitely divisible law [1,2]. Consequently, questions about possible convolution limits can be reformulated as questions about convergence and decomposition of measures on jump sizes. The object also separates three mathematically distinct mechanisms—drift, Gaussian fluctuation, and jumps—without forcing the jump component to have finite activity or finite moments. This separation is the Lévy measure's direct contribution to the motivating classification, rather than merely a later application.

## 3. Notes

A Lévy measure is generally not a probability measure and need not be finite. When \(\nu\) is finite, its jump component is compound Poisson; when \(\nu\) is infinite near zero, infinitely many small jumps may occur on compact time intervals. The cutoff \(\mathbf 1_{\{\|x\|\le1\}}\) is conventional: other admissible truncation functions alter the displayed drift \(\gamma\), not \(\nu\). The Lévy measure alone does not determine an arbitrary infinitely divisible law because the drift and Gaussian covariance must also be specified.

## 4. Sources

[1] Ken-iti Sato, *Lévy Processes and Infinitely Divisible Distributions*, Cambridge Studies in Advanced Mathematics 68, Cambridge University Press, 1999, especially Theorem 8.1.

[2] David Applebaum, *Lévy Processes and Stochastic Calculus*, 2nd ed., Cambridge Studies in Advanced Mathematics 116, Cambridge University Press, 2009, Chapters 1–2.

[3] A. Khintchine, “Zur Theorie der unbeschränkt teilbaren Verteilungsgesetze,” *Matematicheskii Sbornik* N.S. 2(44), no. 1 (1937), 79–119, https://www.mathnet.ru/eng/sm5562.
