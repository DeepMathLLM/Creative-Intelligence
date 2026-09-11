# Mathematical Object Origin Archive | Characteristic Function of a Probability Distribution

## 1. Archive Information

- Standard Name: Characteristic function of a probability distribution
- Mathematical Field: Probability Theory and Stochastic Processes
- Abstract: The characteristic function \(\varphi_\mu(t)=\int e^{i\langle t,x\rangle}\,\mu(dx)\) encodes a probability law by testing it against the bounded characters of the additive group \(\mathbb R^d\). It was formed to make the laws of sums and their limiting behavior tractable: convolution becomes multiplication, while uniqueness and continuity theorems permit passage back from transforms to probability laws.

## 2. Core Record

### Precise Description

For a Borel probability measure \(\mu\) on \(\mathbb R^d\), its **characteristic function** is
\[
\varphi_\mu(t)=\int_{\mathbb R^d}e^{i\langle t,x\rangle}\,\mu(dx),\qquad t\in\mathbb R^d.
\]
If \(X\) is an \(\mathbb R^d\)-valued random variable with law \(\mu\), the same object is written
\[
\varphi_X(t)=\mathbb E\!\left[e^{i\langle t,X\rangle}\right].
\]
Thus it is the Fourier–Stieltjes transform of the law, not of a chosen density. It exists for every probability law because \(|e^{i\langle t,x\rangle}|=1\). It satisfies \(\varphi_\mu(0)=1\), \(\varphi_\mu(-t)=\overline{\varphi_\mu(t)}\), continuity, and positive definiteness:
\[
\sum_{j,k=1}^m c_j\overline{c_k}\,\varphi_\mu(t_j-t_k)\ge 0.
\]
Conversely, Bochner's theorem identifies the continuous positive-definite functions on \(\mathbb R^d\) taking the value \(1\) at \(0\) as exactly the characteristic functions of probability measures. A characteristic function uniquely determines its probability law [1,2].

### Mathematical Context and Formation

The motivating problem class is to determine and compare the distributions of sums of random variables, especially repeated sums
\[
S_n=X_1+\cdots+X_n,
\]
and to prove that normalized sums converge to a limiting law. At the level of probability measures, addition produces convolution: if \(X\) and \(Y\) are independent with laws \(\mu\) and \(\nu\), then \(X+Y\) has law \(\mu*\nu\). Directly computing an \(n\)-fold convolution rapidly becomes unwieldy; moreover, laws need not possess densities, so density-based integral formulas do not provide a general method. Describing a law only through moments is also inadequate: relevant moments can fail to exist, and even an infinite moment sequence need not uniquely determine a law without additional hypotheses [1,2].

The decisive structural observation is to probe the law with the bounded additive characters \(x\mapsto e^{i\langle t,x\rangle}\). Boundedness makes every such probe integrable for every probability measure, while the identity
\[
e^{i\langle t,x+y\rangle}=e^{i\langle t,x\rangle}e^{i\langle t,y\rangle}
\]
matches the operation that causes the difficulty. Consequently,
\[
\varphi_{X+Y}(t)=\varphi_X(t)\varphi_Y(t)
\]
for independent \(X,Y\), so convolution of laws becomes ordinary pointwise multiplication. Taking all frequencies \(t\), rather than finitely many moments, retains the whole law by the uniqueness theorem. Lévy's continuity theorem supplies the complementary limiting principle: pointwise convergence of characteristic functions to a function continuous at \(0\) is equivalent to weak convergence to the probability law having that limiting characteristic function [1,3]. The characteristic function is therefore the object obtained by aligning Fourier analysis with the additive and limiting structure of the probability problem, rather than by assuming regularity such as the existence of a density.

### Essential Role

The characteristic function makes the convolution and limit stages of the sum problem tractable in one representation. For independent identically distributed variables,
\[
\varphi_{S_n}(t)=\varphi_X(t)^n,
\]
turning an \(n\)-fold convolution into a power. When \(X\) has mean \(m\) and variance \(\sigma^2\in(0,\infty)\), the local expansion
\[
\varphi_X(u)=1+imu-\tfrac12\mathbb E[X^2]u^2+o(u^2)
\]
can be combined with centering and scaling to give
\[
\varphi_{(S_n-nm)/(\sigma\sqrt n)}(t)
=\left(e^{-itm/(\sigma\sqrt n)}
\varphi_X\!\left(\frac{t}{\sigma\sqrt n}\right)\right)^n
\longrightarrow e^{-t^2/2}.
\]
Lévy's continuity theorem converts this pointwise transform limit into convergence in distribution to the standard normal law. Thus multiplication handles the repeated addition, the behavior near \(t=0\) extracts the scale governing the limit, and continuity plus uniqueness returns from the transform to a uniquely specified probability law [1–3].

This contribution is more specific than the generic claim that Fourier analysis is useful in probability. The definition uses bounded characters so it applies without densities or moments; its multiplicativity under independence is tailored to independent sums; and its injectivity and continuity theory prevent the transformed calculation from losing the original probabilistic meaning. It reformulates the hard operation—convolution of measures—as elementary algebra while preserving enough information to settle distributional limits.

## 3. Notes

A characteristic function should not be confused with an indicator function, for which “characteristic function” is an older synonym. It also differs from a moment-generating function \(\mathbb E[e^{\langle t,X\rangle}]\): the latter may be infinite away from \(t=0\), whereas the characteristic function always exists on real frequencies. Independence guarantees the factorization \(\varphi_{X+Y}=\varphi_X\varphi_Y\); without independence it cannot in general be inferred from the marginal characteristic functions, although particular dependent pairs may happen to satisfy it. Dependence is instead retained by the joint characteristic function. Transform methods may identify a law or prove convergence without yielding a simple closed formula for its probabilities.

## 4. Sources

[1] Patrick Billingsley, *Probability and Measure*, 3rd ed., Wiley, 1995, Section 26.

[2] William Feller, *An Introduction to Probability Theory and Its Applications*, Vol. II, 2nd ed., Wiley, 1971, Chapter XV.

[3] Olav Kallenberg, *Foundations of Modern Probability*, 2nd ed., Springer, 2002.
