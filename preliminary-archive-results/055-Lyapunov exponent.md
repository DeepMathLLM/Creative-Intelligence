# Mathematical Object Origin Archive | Lyapunov Exponent

## 1. Archive Information

- Standard Name: Lyapunov exponent
- Mathematical Field: Dynamical Systems
- Abstract: A Lyapunov exponent is the asymptotic exponential growth rate of an infinitesimal perturbation transported along a trajectory. It was formed to address the stability-of-motion problem when the linearized dynamics vary along the motion, so that eigenvalues of one fixed linear map cannot describe long-time perturbation growth.

## 2. Core Record

### Precise Description

Let \(T:X\to X\) be a discrete-time dynamical system and let \(A\) be a finite-dimensional linear cocycle over \(T\). Thus
\[
A^{(n)}(x)=A(T^{n-1}x)\cdots A(Tx)A(x),
\qquad
A^{(n+m)}(x)=A^{(n)}(T^m x)A^{(m)}(x).
\]
For a nonzero vector \(v\), its upper Lyapunov exponent at \(x\) is
\[
\overline\lambda(x,v)=\limsup_{n\to\infty}
\frac{1}{n}\log\frac{\|A^{(n)}(x)v\|}{\|v\|}.
\]
When the corresponding limit exists, its value
\[
\lambda(x,v)=\lim_{n\to\infty}
\frac{1}{n}\log\frac{\|A^{(n)}(x)v\|}{\|v\|}
\]
is the Lyapunov exponent of \(v\). For a differentiable map \(T:M\to M\), the relevant cocycle is \(A^{(n)}(x)=D(T^n)_x\). For a differentiable flow \(\varphi^t\), the continuous-time definition replaces \(n\) by \(t\) and uses \(D\varphi_x^t\).

The quotient by elapsed time records exponential order: \(\|A^{(n)}v\|\approx e^{n\lambda}\|v\|\) at that order. In finite dimensions the value is unchanged on replacing the norm by an equivalent norm; derivative cocycles on a compact manifold consequently give the same exponents for any two continuous Riemannian metrics. Under the hypotheses of the multiplicative ergodic theorem—typically an invariant probability measure and suitable logarithmic integrability of the cocycle (and of its inverse in the invertible formulation)—there are, almost everywhere, finitely many exponents and a measurable invariant splitting or filtration into directions having those rates [2].

### Mathematical Context and Formation

The motivating problem is the stability of a motion governed by a differential equation or iterated map: if its initial state is changed slightly, does the resulting displacement shrink, remain comparable, or grow as time becomes large? Along a reference solution \(x(t)\) of \(\dot x=F(t,x)\), the first-order displacement \(\xi(t)\) satisfies the variational equation
\[
\dot\xi(t)=D_xF(t,x(t))\xi(t),
\qquad \xi(t)=\Phi(t)\xi(0).
\]
Thus the stability question already requires understanding long products, or a time-ordered evolution, of linear maps whose coefficients change along the trajectory. This is the mathematical setting of Lyapunov's general stability problem [1].

For a constant-coefficient linearization at an equilibrium, eigenvalues of one matrix provide exponential rates. That method is inadequate along a general nonstationary motion: the matrices at different times need not commute, their eigendirections can rotate, and the eigenvalues of the instantaneous matrix do not in general determine the growth of its time-ordered product. The unnormalized size \(\|\Phi(t)v\|\) also mixes initial scale, bounded coordinate effects, and the long-time rate that stability analysis seeks.

The decisive construction is to measure the evolution actually accumulated by the perturbation rather than diagonalize each instantaneous linearization. Successive evolution multiplies amplitudes, so taking a logarithm converts multiplicative growth into an additive quantity; dividing by elapsed time extracts the average exponential rate. Passing to a limit, or first to a limsup when convergence is unavailable, produces the Lyapunov characteristic exponent. In this way the object is formed directly from the obstruction in the stability problem: a varying, generally noncommutative linearized evolution must be assigned a coordinate-robust long-time rate [1].

### Essential Role

The Lyapunov exponent makes the asymptotic-growth part of the stability problem tractable. Instead of requiring a simultaneous diagonalization of all linearizations, it assigns a scalar rate to each perturbation direction using the full cocycle product. Positive, negative, and zero values distinguish exponential expansion, exponential contraction, and behavior not decided at exponential scale. The logarithm and time normalization discard fixed rescalings and bounded changes of coordinates: such factors contribute only \(O(1/t)\) to the measured rate. These features address precisely the two obstacles above—multiplicative, noncommuting evolution and dependence on incidental scale.

The collection of directional exponents further reveals that stability is not merely a yes-or-no property of a trajectory: different tangent directions may have different asymptotic rates. The multiplicative ergodic theorem makes this viewpoint structurally effective by supplying, under its hypotheses, invariant measurable subspaces or a filtration on which the rates are well defined [2]. The largest exponent then identifies the fastest exponential first-order growth, while the associated splitting locates the responsible directions.

This contribution is narrower than a complete nonlinear stability criterion. Linearization must still be related to finite perturbations, a zero exponent is inconclusive at exponential order, and nonuniform estimates may require additional hypotheses. The object's direct achievement is therefore the reformulation and measurement of long-time infinitesimal growth along a varying motion, not an unconditional solution of every nonlinear stability question.

## 3. Notes

A Lyapunov exponent is distinct from a Lyapunov function. A Lyapunov function is a scalar function on state space whose monotonicity can prove stability without solving the motion; an exponent is an asymptotic rate extracted from the linearized evolution along a motion. “Lyapunov spectrum” denotes the collection of exponents, whereas the archived object is one such exponent. The limsup-defined upper exponent exists as an extended real number even when no true limiting exponent exists.

## 4. Sources

[1] A. M. Lyapunov, *The General Problem of the Stability of Motion* (1892); English translation, *International Journal of Control* 55 (1992), 531–773.

[2] V. I. Oseledets, “A multiplicative ergodic theorem. Lyapunov characteristic numbers for dynamical systems,” *Transactions of the Moscow Mathematical Society* 19 (1968), 197–231.
