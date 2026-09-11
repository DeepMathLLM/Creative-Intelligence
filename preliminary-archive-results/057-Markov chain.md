# Mathematical Object Origin Archive | Markov Chain

## 1. Archive Information

- Standard Name: Markov chain
- Mathematical Field: Probability Theory and Stochastic Processes
- Abstract: A Markov chain is a stochastic process whose conditional law of the next state, given the entire observed past, depends only on the present state. It formed as a controlled model of dependent random variables for the problem of extending laws of large numbers beyond independent trials: dependence is retained, but encoded locally by transition probabilities that can be iterated and analyzed.

## 2. Core Record

### Precise Description

Let \((\Omega,\mathcal F,\mathbb P)\) be a probability space and \((S,\mathcal S)\) a measurable state space. A discrete-time stochastic process \((X_n)_{n\ge 0}\) with values in \(S\) is a Markov chain if, for every \(n\ge 0\) and \(A\in\mathcal S\),
\[
\mathbb P(X_{n+1}\in A\mid X_0,\ldots,X_n)
=
\mathbb P(X_{n+1}\in A\mid X_n)
\quad\text{almost surely}.
\]
In the time-homogeneous case there is a single transition kernel \(K\) such that
\[
\mathbb P(X_{n+1}\in A\mid X_n)=K(X_n,A).
\]
An initial distribution \(\mu\) and \(K\) determine the finite-dimensional laws by
\[
\mathbb P(X_0\in dx_0,\ldots,X_n\in dx_n)
=\mu(dx_0)\prod_{r=1}^{n}K(x_{r-1},dx_r).
\]
For a finite or countable state space, \(K\) is represented by a stochastic matrix \(P=(p_{ij})\), where \(p_{ij}=\mathbb P(X_{n+1}=j\mid X_n=i)\), and \(m\)-step transition probabilities are entries of \(P^m\) [3].

### Mathematical Context and Formation

The motivating problem was to determine whether a law of large numbers could hold for genuinely dependent random variables. In the classical independent-trial setting, the joint law factors into one-step marginal laws, and variance estimates for a sum simplify because cross-covariances vanish. For arbitrary dependence neither simplification is available: a specification of one-variable distributions does not determine joint behavior, and correlations may persist strongly enough to prevent empirical averages from stabilizing. Thus merely deleting independence left too broad a class for a usable theorem.

Markov's 1906 work addressed this obstacle by considering variables “depending on each other” in a chain and proving a law-of-large-numbers conclusion for such linked variables [1]. The formative insight was to replace global independence by a local conditional rule: once the current variable is known, earlier variables supply no further information about the next one. This permits adjacent variables to be dependent while making the full joint law computable from an initial distribution and one-step transition probabilities. Markov first treated a two-state system with nondegenerate transition probabilities and then developed broader chained models; the connection of this work with the modern Markov chain is documented in [2].

The two-state homogeneous case displays why the new structure was adequate. Write
\[
P=\begin{pmatrix}1-a&a\\ b&1-b\end{pmatrix},\qquad 0<a,b<1.
\]
Its stationary distribution is
\[
\pi=\left(\frac{b}{a+b},\frac{a}{a+b}\right),
\]
and its second eigenvalue is \(\lambda=1-a-b\), with \(|\lambda|<1\). Iteration of the local rule gives \(P^m\to \mathbf 1\pi\), so the influence of a state \(m\) steps in the past decays geometrically. In stationarity, for \(Y_n=\mathbf 1_{\{X_n=1\}}\),
\[
\operatorname{Cov}(Y_0,Y_m)=\pi_1(1-\pi_1)\lambda^m.
\]
Consequently the variance of \(n^{-1}\sum_{r=1}^nY_r\) tends to zero, yielding convergence in probability of the empirical frequency to \(\pi_1\). This calculation identifies the exact replacement for independence: not zero covariance at every lag, but dependence controlled through powers of a transition rule.

### Essential Role

The Markov chain made the dependent-variable law-of-large-numbers problem tractable by locating all permitted dependence in a one-step kernel. The Markov property factorizes a path law into transition factors even though the random variables themselves are not independent. The semigroup relation for multi-step transitions—matrix powers in the finite-state case—then turns a difficult many-variable dependence calculation into iteration of one operator.

For the motivating two-state problem, the invariant vector of \(P\) supplies the limiting state frequencies, while the nontrivial eigenvalue controls loss of memory. Geometric decay of the corresponding correlations makes the accumulated covariance in a sample mean small enough for the variance to vanish. The object therefore bypassed the unavailable independent-product model without admitting arbitrary, analytically uncontrollable dependence. It established, constructively, that independence is sufficient but not necessary for a law of large numbers [1], [2].

The deeper structural viewpoint introduced by the object is that long-run probabilistic regularity can be governed by the dynamics of a transition operator: stationary distributions encode candidate averages, and recurrence or mixing properties determine whether those averages are reached. This is the direct conceptual enlargement forced by the original problem, rather than a later application of the chain.

## 3. Notes

The Markov property alone does not guarantee a law of large numbers. Reducibility, absorbing classes, periodicity, or lack of positive recurrence can alter or prevent convergence to a single deterministic stationary average. Appropriate irreducibility and recurrence or ergodicity hypotheses are therefore part of modern limit theorems [3]. A Markov chain is also not a sequence of independent variables: independence is the special case in which the transition law does not depend on the current state.

## 4. Sources

[1] A. A. Markov, “Extension of the Law of Large Numbers to Quantities Depending on Each Other” (1906), English reprint, *Journal Électronique d’Histoire des Probabilités et de la Statistique* 2, no. 1b (2006), Article 10. https://eudml.org/doc/128778

[2] G. P. Basharin, A. N. Langville, and V. A. Naumov, “The Life and Work of A. A. Markov,” *Linear Algebra and its Applications* 386 (2004), 3–26. https://doi.org/10.1016/j.laa.2003.12.041

[3] J. R. Norris, *Markov Chains*, Cambridge Series in Statistical and Probabilistic Mathematics, Cambridge University Press, 1997.
