# Mathematical Object Origin Archive | Kolmogorov–Sinai Entropy

## 1. Archive Information

- Standard Name: Kolmogorov–Sinai entropy
- Mathematical Field: Ergodic Theory; Dynamical Systems
- Abstract: Kolmogorov–Sinai entropy is an extended nonnegative real-valued invariant of a probability-preserving transformation. It was formed to address the metric-isomorphism problem for measure-preserving dynamical systems: in particular, to obtain a numerical obstruction proving that Bernoulli shifts with different information-production rates cannot be measurably conjugate. Its definition converts the Shannon information in finite orbit observations into an asymptotic rate and then removes dependence on the chosen observation by taking a supremum over all finite measurable partitions.

## 2. Core Record

### Precise Description

Let \((X,\mathcal B,\mu)\) be a probability space and let \(T:X\to X\) be a measurable, measure-preserving transformation. For a finite measurable partition \(\alpha=\{A_1,\ldots,A_r\}\), define its Shannon entropy by
\[
H_\mu(\alpha)=-\sum_{i=1}^r \mu(A_i)\log \mu(A_i),
\]
with \(0\log 0=0\). The common refinement \(\alpha\vee\beta\) consists, modulo null sets, of the non-null intersections \(A\cap B\). The partition
\[
\alpha_0^{n-1}=\bigvee_{j=0}^{n-1}T^{-j}\alpha
\]
records the length-\(n\) names of points observed through \(\alpha\). The entropy rate relative to \(\alpha\) is
\[
h_\mu(T,\alpha)=\lim_{n\to\infty}\frac{1}{n}H_\mu\!\left(\alpha_0^{n-1}\right).
\]
The limit exists because the block entropies form a subadditive sequence. The Kolmogorov–Sinai entropy is
\[
h_\mu(T)=\sup_{\alpha}h_\mu(T,\alpha),
\]
where the supremum ranges over finite measurable partitions; its value lies in \([0,\infty]\). The base of the logarithm fixes the unit but not the invariant's qualitative content [2][3][5].

A measure-theoretic isomorphism of probability-preserving systems transports finite partitions, preserves their atom measures and all their iterated joins, and therefore preserves \(h_\mu(T)\). If \(\alpha\) is a finite generating partition, the Kolmogorov–Sinai generator theorem gives \(h_\mu(T)=h_\mu(T,\alpha)\), making the supremum computable from that one partition [3][5].

### Mathematical Context and Formation

The motivating problem was to decide when two measure-preserving transformations are isomorphic modulo null sets. A central concrete test case was the family of Bernoulli shifts. For the uniform \(k\)-symbol two-sided Bernoulli shift
\[
\sigma:(\{1,\ldots,k\}^{\mathbb Z},u_k^{\mathbb Z})\longrightarrow(\{1,\ldots,k\}^{\mathbb Z},u_k^{\mathbb Z}),
\qquad (\sigma x)_j=x_{j+1},
\]
the problem included proving, for example, that the two-symbol and three-symbol shifts are not measurably isomorphic [1][2]. Coarse dynamical properties did not resolve this: both systems are ergodic and strongly mixing. Moreover, an isomorphism is allowed to reorganize the measurable phase space in a highly non-coordinate fashion, so the visible alphabet size is not itself an invariant. Shannon entropy measured the uncertainty of a probability distribution or finite observation, but the entropy of one chosen partition depended on that choice and therefore did not yet characterize the transformation [4].

The decisive construction was to regard a finite partition \(\alpha\) as an observation of the state and to follow that observation through time. The join \(\bigvee_{j=0}^{n-1}T^{-j}\alpha\) records all distinguishable length-\(n\) observation histories. Its Shannon entropy measures their aggregate information, while division by \(n\) and passage to the limit extract information produced per iterate rather than information in a particular finite window. Taking the supremum over every finite measurable partition then removes dependence on a privileged observation scheme: any measurable conjugacy carries the entire family of observation schemes on one system to the corresponding family on the other. Kolmogorov introduced dynamical entropy in 1958, and the 1959 formulations of entropy per unit time and entropy via finite partitions established the durable invariant now called Kolmogorov–Sinai entropy [1][2][3].

### Essential Role

For a Bernoulli shift with symbol probabilities \(p=(p_1,\ldots,p_k)\), let \(\alpha\) be the partition according to the zeroth coordinate. Independence makes the \(n\)-coordinate join satisfy
\[
H\!\left(\bigvee_{j=0}^{n-1}\sigma^{-j}\alpha\right)
=n\left(-\sum_{i=1}^k p_i\log p_i\right).
\]
Since the coordinate partition is generating, the generator theorem yields
\[
h(\sigma)=-\sum_{i=1}^k p_i\log p_i.
\]
Consequently the uniform two-symbol and three-symbol shifts have entropies \(\log 2\) and \(\log 3\), respectively, and cannot be measurably isomorphic [1][2][3]. Thus the object made a specific previously inaccessible step tractable: it replaced the search over arbitrary measurable conjugacies by computation of a scalar invariant whose inequality is a rigorous obstruction to conjugacy.

Each layer of the definition addresses one part of that difficulty. Temporal joins retain correlations and accumulated distinctions that a one-time partition misses; normalization produces a rate stable under extending the observation window; and the supremum over all finite partitions makes the rate intrinsic rather than coordinate-dependent. The resulting structural viewpoint treats a deterministic measure-preserving map as an information source and defines the supremal asymptotic information rate detected by finite measurable observations; this supremum need not be attained by any single finite partition. This direct role is an obstruction to isomorphism, not a complete classification: equal Kolmogorov–Sinai entropy does not imply isomorphism for general measure-preserving systems. The later theorem that entropy completely classifies Bernoulli shifts up to measure-theoretic isomorphism is a stronger subsequent result, not part of the invariant's original direct contribution.

## 3. Notes

Kolmogorov–Sinai entropy is also called metric entropy or measure-theoretic entropy. It depends on the invariant probability measure and should not be confused with topological entropy, which is defined from the topology of a continuous dynamical system rather than from a selected invariant measure. The value \(0\) does not mean that the system is dynamically trivial; it means only that its finite measurable observations have sublinear Shannon-information growth.

## 4. Sources

[1] A. N. Kolmogorov, “A New Metric Invariant of Transitive Dynamical Systems and Automorphisms of Lebesgue Spaces,” *Doklady Akademii Nauk SSSR* 119 (1958), 861–864.

[2] A. N. Kolmogorov, “Entropy per Unit Time as a Metric Invariant of Automorphisms,” *Doklady Akademii Nauk SSSR* 124 (1959), 754–755.

[3] Ya. G. Sinai, “On the Concept of Entropy of a Dynamical System,” *Doklady Akademii Nauk SSSR* 124 (1959), 768–771.

[4] C. E. Shannon, “A Mathematical Theory of Communication,” *Bell System Technical Journal* 27 (1948), 379–423 and 623–656.

[5] Peter Walters, *An Introduction to Ergodic Theory*, Graduate Texts in Mathematics 79, Springer, 1982, Chapter 4.
