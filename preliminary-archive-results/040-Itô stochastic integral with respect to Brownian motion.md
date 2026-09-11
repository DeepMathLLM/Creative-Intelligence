# Mathematical Object Origin Archive | Itô stochastic integral with respect to Brownian motion

## 1. Archive Information

- Standard Name: Itô stochastic integral with respect to Brownian motion
- Mathematical Field: Probability Theory and Stochastic Processes
- Abstract: The Itô stochastic integral \(\int_0^t H_s\,dW_s\) integrates a nonanticipating random process against Brownian motion. It was formed to give rigorous meaning to the noise term in stochastic differential equations, where ordinary pathwise integration and the earlier deterministic-integrand Wiener integral were inadequate. Its construction from adapted left-endpoint sums and completion under an \(L^2\) isometry turns formal Brownian-driven differential equations into analyzable integral equations.

## 2. Core Record

### Precise Description

Let \((\Omega,\mathcal F,(\mathcal F_t)_{0\le t\le T},\mathbb P)\) be a filtered probability space and let \(W\) be an \((\mathcal F_t)\)-Brownian motion. For a simple predictable process
\[
H_t=\sum_{i=0}^{n-1}\xi_i\mathbf 1_{(t_i,t_{i+1}]}(t),
\qquad 0=t_0<\cdots<t_n=T,
\]
where each \(\xi_i\) is \(\mathcal F_{t_i}\)-measurable and square-integrable (with the products below square-integrable), define
\[
\int_0^T H_t\,dW_t
 :=\sum_{i=0}^{n-1}\xi_i\bigl(W_{t_{i+1}}-W_{t_i}\bigr).
\]
The coefficient on an interval is therefore determined before that interval's Brownian increment is observed. Independent Brownian increments then give the Itô isometry
\[
\mathbb E\!\left[\left|\int_0^T H_t\,dW_t\right|^2\right]
 =\mathbb E\!\left[\int_0^T |H_t|^2\,dt\right].
\]
Consequently the map extends uniquely by \(L^2(\Omega\times[0,T])\)-completion to predictable processes \(H\) satisfying
\[
\mathbb E\int_0^T |H_t|^2\,dt<\infty.
\]
For such \(H\), the process \(I_t=\int_0^tH_s\,dW_s\) has a continuous version and is a square-integrable martingale. The same construction is subsequently localized to wider classes of predictable integrands and generalized to suitable martingale or semimartingale integrators. The Brownian \(L^2\) construction above is the core object documented here [1][4].

### Mathematical Context and Formation

The motivating problem class was to construct and analyze diffusion processes specified formally by stochastic differential equations
\[
dX_t=b(t,X_t)\,dt+\sigma(t,X_t)\,dW_t,
\]
or, equivalently once the last term is defined,
\[
X_t=X_0+\int_0^t b(s,X_s)\,ds+\int_0^t\sigma(s,X_s)\,dW_s.
\]
Such equations were intended to describe Markov processes with continuous random motion and prescribed local drift and diffusion. The obstruction was concentrated in the expression involving \(dW_t\). Brownian paths are almost surely nowhere differentiable and have infinite total variation on every nontrivial interval, so \(dW_t/dt\) cannot be treated as an ordinary forcing function and the usual finite-variation Lebesgue–Stieltjes theory does not apply. Classical Riemann–Stieltjes integration likewise does not provide the required general integral for state-dependent integrands. Earlier Wiener integration could handle suitable deterministic functions of time, but \(\sigma(t,X_t)\) is random and depends on the evolving solution itself; this is precisely the case needed for a stochastic differential equation [1][2][3].

The decisive formation principle was to combine causality with mean-square geometry. On \((t_i,t_{i+1}]\), evaluate the random coefficient using only information in \(\mathcal F_{t_i}\), and pair it with the future increment \(W_{t_{i+1}}-W_{t_i}\). Adaptedness makes that coefficient independent of the new Brownian increment in the sense needed for cross terms to vanish. Thus the discrete sums have an exact \(L^2\) norm controlled by \(\mathbb E\int |H|^2dt\). Instead of seeking pathwise bounded variation, one takes the mean-square limit of these nonanticipating sums. The Itô isometry proves that the limit exists, is independent of the approximating simple processes, and remains stable under approximation. This mechanism enlarged stochastic integration from deterministic integrands to the random adapted integrands required by the diffusion equation [1][4].

### Essential Role

The Itô integral made the noise term \(\int_0^t\sigma(s,X_s)\,dW_s\) a well-defined random process, thereby reformulating the formal differential equation as a rigorous integral fixed-point problem. This was the exact part of the diffusion problem that ordinary differential-equation and Stieltjes methods could not supply. Under standard Lipschitz and growth assumptions, successive approximations can be compared using
\[
\mathbb E\left|\int_0^t
   \bigl(\sigma(s,X_s)-\sigma(s,Y_s)\bigr)\,dW_s\right|^2
=
\mathbb E\int_0^t
   |\sigma(s,X_s)-\sigma(s,Y_s)|^2\,ds,
\]
so estimates for random noise terms reduce to time-integral estimates. Together with corresponding estimates for the drift, this permits existence and uniqueness arguments for Brownian-driven stochastic differential equations [2][3][4].

Each defining feature addresses a specific obstacle. Predictability enforces nonanticipation and supplies the orthogonality of successive increments; left-endpoint evaluation selects a consistent limit for random integrands; and the \(L^2\) isometry replaces unavailable pathwise variation bounds with a complete Hilbert-space estimate. The construction also exposes the structural reason ordinary calculus fails: Brownian quadratic variation is nonzero. For example,
\[
\int_0^t W_s\,dW_s=\frac12\bigl(W_t^2-t\bigr),
\]
not \(W_t^2/2\). The correction term is encoded systematically by Itô's formula and connects a diffusion's stochastic integral equation to its second-order infinitesimal generator. Thus the object did more than assign a value to a formal integral: it identified nonanticipating \(L^2\) limits and quadratic variation as the correct calculus for the original diffusion problem [3][4].

## 3. Notes

The Itô integral should not be conflated with the earlier Wiener integral for deterministic integrands; the former admits random predictable integrands and is the construction needed for state-dependent stochastic equations. It also differs from the Stratonovich integral, whose symmetric discretization yields the ordinary-looking chain rule but includes a quadratic-covariation conversion term relative to the Itô integral. Extensions to general semimartingales preserve the nonanticipating character but require a broader construction than the Brownian \(L^2\) object recorded here.

## 4. Sources

[1] Kiyosi Itô, “Stochastic Integral,” *Proceedings of the Imperial Academy, Tokyo* **20** (1944), no. 8, 519–524. https://doi.org/10.3792/pia/1195572786

[2] Kiyosi Itô, “On a Stochastic Integral Equation,” *Proceedings of the Imperial Academy, Tokyo* **22** (1946), no. 2, 32–35. https://doi.org/10.3792/pja/1195572371

[3] Kiyosi Itô, “On Stochastic Differential Equations,” *Memoirs of the American Mathematical Society* **4** (1951), 1–51.

[4] Ioannis Karatzas and Steven E. Shreve, *Brownian Motion and Stochastic Calculus*, 2nd ed., Graduate Texts in Mathematics 113, Springer, 1991, Chapters 3 and 5.
