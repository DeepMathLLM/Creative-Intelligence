# Mathematical Object Origin Archive | Stable Distribution

## 1. Archive Information

- Standard Name: Stable distribution
- Mathematical Field: Probability Theory and Stochastic Processes
- Abstract: A stable distribution is a probability law whose shape is preserved, up to positive rescaling and translation, when independent random variables with that law are added. It is the intrinsic object singled out by the problem of classifying all nondegenerate distributional limits of affine-normalized sums of independent identically distributed random variables when finite variance is not assumed.

## 2. Core Record

### Precise Description

A nondegenerate probability distribution on \(\mathbb{R}\), represented by a random variable \(X\), is **stable** if, for independent copies \(X_1,X_2\) of \(X\) and every \(a,b>0\), there exist \(c>0\) and \(m\in\mathbb{R}\) such that
\[
aX_1+bX_2\;\overset{d}{=}\;cX+m.
\]
It is **strictly stable** if \(m\) can always be taken to be zero. For every nondegenerate stable law there is a unique stability index \(\alpha\in(0,2]\) for which
\[
c^\alpha=a^\alpha+b^\alpha.
\]
Consequently, for independent copies \(X_1,\ldots,X_n\),
\[
X_1+\cdots+X_n\;\overset{d}{=}\;n^{1/\alpha}X+m_n
\]
for suitable centering constants \(m_n\). Thus stability is not mere closure of a named family under convolution: the sum remains of the same location-scale type as the original law [1].

Stable laws are commonly parameterized by an index \(0<\alpha\le 2\), a skewness parameter \(-1\le\beta\le1\), a positive scale, and a location parameter. The case \(\alpha=2\) is Gaussian. Non-Gaussian stable laws have \(\alpha<2\) and infinite variance; the Cauchy and one-sided Lévy laws are familiar special cases. Most stable laws are specified most naturally through their characteristic functions rather than elementary density formulas [1].

### Mathematical Context and Formation

The motivating problem class is precise: determine which nondegenerate laws \(Z\) can occur in
\[
a_n(X_1+\cdots+X_n)-b_n\;\xrightarrow{d}\;Z,
\]
where \(X_1,X_2,\ldots\) are independent and identically distributed, \(a_n>0\), and \(b_n\in\mathbb{R}\). The classical central limit theorem answers this under a finite-variance hypothesis: centering by the mean and scaling on the order of \(n^{-1/2}\) produce a Gaussian limit. Once finite variance is removed, that method no longer controls the sum. The variance may be infinite, \(n^{1/2}\) need not be the correct scale, the mean may not exist, and asymmetric heavy tails may survive normalization. Simply allowing arbitrary \(a_n\) and \(b_n\) leaves an apparently unconstrained search over possible limits.

The decisive insight comes from the internal structure of the sum. A long sum can be divided into independent blocks. If normalized sums converge to \(Z\), then two suitably sized blocks converge to independent copies \(Z_1,Z_2\) of \(Z\), while their union is another normalized sum with the same limiting type. Compatibility of these two descriptions forces positive linear combinations \(aZ_1+bZ_2\) to have the same distributional shape as \(Z\), apart from scale and translation. This is exactly the stability relation. In this way, associativity of addition and the freedom to renormalize do not merely suggest examples; they form the object that any nondegenerate limit must be.

The generalized central limit theorem makes the connection exact: a nondegenerate real law occurs as a weak limit of affine-normalized sums of i.i.d. random variables if and only if it is stable [1][2]. Structurally, stable distributions may therefore be viewed as the fixed shapes of the operation “convolve independent copies and then recenter and rescale.” This fixed-point wording is an interpretive synthesis of the defining relation, whereas the limit classification is an established theorem.

### Essential Role

The stable distribution resolves the candidate-classification part of the motivating problem. Instead of attempting to compute a new limiting density for every infinite-variance summand law, one first knows that any nondegenerate limit must lie in a single rigid class characterized by invariance under addition. The defining relation is precisely what makes the blocking argument consistent: convolution changes only location and scale, not distributional shape.

Its stability index records the normalization geometry. Repeated addition changes scale by \(n^{1/\alpha}\), so normalized sums use a scale of order \(n^{-1/\alpha}\) in the basic stable case rather than the Gaussian order \(n^{-1/2}\). Skewness and translation accommodate imbalanced tails and necessary centering, while characteristic functions turn convolution into multiplication and make the stability equation analytically tractable. These features retain the exceptional-jump behavior that variance-based arguments discard or cannot express.

The object also supplies a deeper structural viewpoint: the Gaussian law is not an isolated universal limit but the \(\alpha=2\) endpoint of the stable class; non-Gaussian \(\alpha<2\) laws are the other possible fixed shapes when finite variance is absent. Stability does not, by itself, decide whether a specified summand distribution converges to a given stable law. That separate domain-of-attraction problem requires conditions on tail decay, tail balance, and the norming constants [1][2]. The direct achievement of the object is the classification and organization of possible limits, not every convergence criterion or later application.

## 3. Notes

“Stable” here means sum-stable, not max-stable, and “strictly stable” excludes the translation term in the defining identity. Several incompatible parameterization conventions are used for stable characteristic functions, especially at \(\alpha=1\); the invariant addition property avoids that notational ambiguity. Every stable law is infinitely divisible, but infinite divisibility alone is weaker than stability.

## 4. Sources

[1] John P. Nolan, *Univariate Stable Distributions: Models for Heavy Tailed Data*, Springer Series in Operations Research and Financial Engineering, Springer, 2020, Chapters 1 and 3, https://doi.org/10.1007/978-3-030-52915-4.

[2] B. V. Gnedenko and A. N. Kolmogorov, *Limit Distributions for Sums of Independent Random Variables*, translated by K. L. Chung, Addison-Wesley, 1954, especially the theory of stable laws and domains of attraction.
