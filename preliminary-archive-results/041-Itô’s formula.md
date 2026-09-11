# Mathematical Object Origin Archive | Itô’s formula

## 1. Archive Information

- Standard Name: Itô’s formula
- Mathematical Field: Probability Theory and Stochastic Processes
- Abstract: Itô’s formula is the change-of-variables rule for smooth functions of continuous semimartingales. It was formed within the problem class of constructing and analyzing stochastic differential equations: ordinary first-order calculus cannot transform a Brownian-driven process correctly because squared stochastic increments accumulate rather than vanish. The formula retains their limit as quadratic covariation and thereby gives the transformed process’s exact drift and local-martingale parts.

## 2. Core Record

### Precise Description

Let \(X=(X^1,\ldots,X^d)\) be a continuous semimartingale on a filtered probability space, and let \(f\in C^2(\mathbb R^d)\). Thus each coordinate may be written
\[
X^i_t=X^i_0+A^i_t+M^i_t,
\]
where \(A^i\) has finite variation and \(M^i\) is a continuous local martingale. Itô’s formula states that, almost surely, for every \(t\geq 0\),
\[
f(X_t)=f(X_0)
 +\sum_{i=1}^d\int_0^t \partial_i f(X_s)\,dX^i_s
 +\frac12\sum_{i,j=1}^d\int_0^t
 \partial_{ij}f(X_s)\,d[X^i,X^j]_s .
\]
Here the integral against \(X^i=A^i+M^i\) is the sum of the finite-variation integral against \(A^i\) and the Itô integral against \(M^i\), while \([X^i,X^j]=[M^i,M^j]\) is quadratic covariation. This continuous-semimartingale form is a standard modern statement of the formula [4].

In particular, if \(W\) is an \(m\)-dimensional Brownian motion and
\[
dX_t=b(t,X_t)\,dt+\sigma(t,X_t)\,dW_t,
\]
then
\[
df(X_t)=
\left(b\cdot\nabla f+\frac12\operatorname{Tr}\!\left(\sigma\sigma^{\mathsf T}D^2f\right)\right)(t,X_t)\,dt
+\nabla f(X_t)\,\sigma(t,X_t)\,dW_t.
\]
The second-order term is therefore part of the stochastic change-of-variables rule, not an approximation error.

### Mathematical Context and Formation

The concrete problem class was to construct Markov processes by stochastic differential equations and then determine how their local equations behave under nonlinear functions or changes of coordinates. Itô described his broader program as unifying the pathwise, independent-increment viewpoint of Lévy processes with Kolmogorov’s Markov-process viewpoint, treating a Lévy process, in a suitable local sense, as a tangent model for a Markov process [3]. Once stochastic integrals and stochastic differential equations had been introduced [2], this program required a rule that could answer a basic question: if \(X\) is given by a stochastic integral equation, what equation is satisfied by \(f(X)\)?

The ordinary chain rule could not answer that question. Brownian sample paths are almost surely nowhere differentiable and have unbounded variation, so \(dW_t\) cannot be handled as an ordinary differential or by the usual Riemann–Stieltjes calculus. More decisively, over a time interval of length \(\Delta t\), a Brownian increment has size of order \(\sqrt{\Delta t}\). Consequently, the first-order Taylor rule discards terms \((\Delta W)^2\) that are individually small but whose sums over a partition are of order one: for Brownian motion, \(\sum(\Delta W)^2\) converges to \(t\). In several dimensions, the corresponding products converge to quadratic covariations.

The formation of Itô’s formula joins two ideas that resolve this obstacle. The stochastic integral supplies a rigorous limit for the linear Taylor terms with nonanticipating integrands, while a second-order Taylor expansion retains the quadratic increment terms. In the limit, the latter become the covariation integrals in the displayed formula. Itô’s 1951 paper gave the formula in detail and in a more general form than an earlier outline [1]. Thus the object was not obtained by merely copying the classical chain rule: it was the corrected chain rule forced by the scaling and quadratic variation of stochastic paths.

### Essential Role

Itô’s formula made the nonlinear transformation step in stochastic differential equations tractable. Before the correction was identified, an equation for \(X\) did not yield a valid equation for \(f(X)\) by ordinary differential rules. The formula supplies that equation and, specifically, its semimartingale decomposition: the first derivatives transform the finite-variation and stochastic-integral parts, while the Hessian paired with quadratic covariation contributes the additional finite-variation term.

For a diffusion, this identifies the operator
\[
Lf=b\cdot\nabla f+\frac12\operatorname{Tr}(\sigma\sigma^{\mathsf T}D^2f)
\]
as the drift of \(f(X_t)\), leaving \(f(X_t)-f(X_0)-\int_0^t Lf(X_s)\,ds\) as a local martingale. Hence local stochastic dynamics can be translated into equations for smooth observables and into the differential operator governing the associated Markov process. This is the precise part of the motivating problem that the formula reformulates: nonlinear path transformation becomes an exact calculation rather than an invalid formal manipulation.

The elementary case \(f(x)=x^2\), \(X=W\), isolates the mechanism:
\[
W_t^2=2\int_0^t W_s\,dW_s+t.
\]
The classical chain rule would omit \(t\), contradicting, for example, \(\mathbb E[W_t^2]=t\), because the Itô integral has mean zero under the usual integrability conditions. The correction term records exactly the accumulated squared increments. This second-order response to first-order random forcing is the structural viewpoint introduced by the formula.

## 3. Notes

Itô’s formula is distinct from the Itô stochastic integral. The integral defines the linear stochastic term, whereas the formula is a change-of-variables theorem built from that integral together with quadratic covariation. The archive states the continuous-semimartingale version; semimartingales with jumps require additional jump terms. In Stratonovich notation a first-order-looking chain rule is recovered by moving the corresponding covariation correction into the definition of the integral, so it is not the same formula under unchanged integration conventions.

## 4. Sources

[1] Kiyosi Itô, “On a Formula Concerning Stochastic Differentials,” *Nagoya Mathematical Journal* **3** (1951), 55–65. https://doi.org/10.1017/S0027763000012216

[2] Kiyosi Itô, “Stochastic Integral,” *Proceedings of the Imperial Academy* **20** (1944), 519–524. https://doi.org/10.3792/pia/1195572786

[3] Kiyosi Itô, “Memoirs of My Research on Stochastic Analysis,” in *Stochastic Analysis and Applications*, Abel Symposium 2, Springer (2007), 1–5. Preprint: https://abelsymposium.no/symp2005/preprints/ito.pdf

[4] Francesco Russo and Pierre Vallois, “Elements of Stochastic Calculus via Regularisation,” arXiv:math/0603224, especially Proposition 13 for the continuous-semimartingale formula. https://arxiv.org/abs/math/0603224
