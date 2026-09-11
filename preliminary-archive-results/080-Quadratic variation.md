# Mathematical Object Origin Archive | Quadratic Variation

## 1. Archive Information

- Standard Name: Quadratic variation
- Mathematical Field: Probability Theory and Stochastic Processes
- Abstract: Quadratic variation records the accumulated squares of a process's increments along increasingly fine time partitions. It isolates the nonvanishing second-order effect of Brownian and, more generally, semimartingale paths, thereby supplying the correction term that makes a differential calculus for such paths possible.

## 2. Core Record

### Precise Description

Let \(X=(X_t)_{t\ge 0}\) be a continuous semimartingale. For a partition
\[
\pi=\{0=t_0<t_1<\cdots<t_n=t\},
\]
form
\[
Q_t^{\pi}(X)=\sum_{i=0}^{n-1}\bigl(X_{t_{i+1}}-X_{t_i}\bigr)^2.
\]
As the mesh \(|\pi|\) tends to zero through deterministic partitions, these sums converge uniformly on compact time intervals in probability to a continuous increasing process \([X]=([X]_t)_{t\ge0}\), called the quadratic variation of \(X\). Equivalently, for a decomposition \(X=X_0+M+A\), where \(M\) is a continuous local martingale and \(A\) is a continuous finite-variation process,
\[
[X]=[M],
\]
so finite-variation motion contributes no quadratic variation. For standard Brownian motion \(B\),
\[
[B]_t=t\qquad\text{almost surely for all }t\ge0.
\]
For two continuous semimartingales, their quadratic covariation is obtained by polarization,
\[
[X,Y]_t=\frac14\bigl([X+Y]_t-[X-Y]_t\bigr).
\]
The present object is the one-process quantity \([X]\); quadratic covariation is noted only to situate it.

### Mathematical Context and Formation

The motivating problem class is to construct a calculus for stochastic trajectories such as Brownian motion: one wants to define integrals against the trajectory and obtain a change-of-variables formula for \(f(X_t)\), analogous to the fundamental theorem and chain rule for differentiable or finite-variation paths. Classical pathwise methods do not directly solve this problem. Brownian paths are almost surely nowhere differentiable and have infinite total variation on every nontrivial interval, so the usual finite-variation framework for Riemann–Stieltjes integration does not apply. Merely declaring infinitesimal increments to be negligible also loses a term that survives under refinement.

The obstruction becomes explicit by applying Taylor's formula on each subinterval:
\[
f(X_{t_{i+1}})-f(X_{t_i})
 =f'(X_{t_i})\Delta_iX+\frac12 f''(X_{t_i})(\Delta_iX)^2+r_i.
\]
For a sufficiently regular finite-variation path, the sum of the squared increments tends to zero, and the second-order contribution disappears in the classical chain rule. Brownian increments instead have size of order \(\sqrt{\Delta t}\); thus each square has order \(\Delta t\), and their accumulated sum approaches \(t\), not zero. Total variation sees only that the first absolute powers diverge and therefore does not retain the finite second-order quantity needed in the Taylor expansion.

This identifies the relevant structural insight: refine time partitions, discard the signs of increments by squaring them, and retain the limit of their accumulated second powers. The resulting quadratic-variation process measures precisely the order of path roughness that survives in the second-order Taylor terms. In this sense, it is formed by extracting from irregular trajectories the datum that classical first-order calculus suppresses but stochastic calculus requires.

### Essential Role

Quadratic variation makes the change-of-variables part of the motivating problem tractable. For a continuous semimartingale \(X\) and sufficiently smooth \(f\), Itô's formula reads
\[
f(X_t)=f(X_0)+\int_0^t f'(X_s)\,dX_s
       +\frac12\int_0^t f''(X_s)\,d[X]_s.
\]
The last integral is exactly the partition-limit of the accumulated second-order Taylor contributions. For Brownian motion it reduces to
\[
\frac12\int_0^t f''(B_s)\,ds
\]
because \([B]_s=s\). Thus quadratic variation neither makes a Brownian path differentiable nor converts it into a finite-variation integrator. Rather, its defining squared-increment limit bypasses those unavailable properties and replaces the failed classical chain rule with a rule that explicitly accounts for the surviving second-order effect.

This also separates the rough martingale component of a continuous semimartingale from its finite-variation component: \([X]=[M]\) in the decomposition \(X=X_0+M+A\). Consequently, estimates and identities for stochastic integrals can be organized by the increasing process \([M]\), which quantifies their accumulated fluctuation. The deeper structural viewpoint is that differential order is altered by stochastic scaling: for Brownian motion, \((dB)^2\) contributes at order \(dt\), while products involving finite-variation increments vanish at quadratic-variation order. Quadratic variation is the precise mathematical object encoding that statement, distinct from the Itô integral whose calculus it governs.

## 3. Notes

For càdlàg semimartingales the same partition-sum idea yields a quadratic variation that also records jumps; in particular, its jump satisfies \(\Delta[X]_t=(\Delta X_t)^2\). Predictable quadratic variation \(\langle M\rangle\), when defined for a local martingale, is a related but different object: it is the predictable compensator associated with \([M]\), not quadratic variation itself.

## 4. Sources

[1] Philip E. Protter, *Stochastic Integration and Differential Equations*, 2nd ed., Springer, 2005, Chapters II–III.

[2] Daniel Revuz and Marc Yor, *Continuous Martingales and Brownian Motion*, 3rd ed., Springer, 1999, Chapters I and IV.

[3] Ioannis Karatzas and Steven E. Shreve, *Brownian Motion and Stochastic Calculus*, 2nd ed., Springer, 1991, Chapters 2–3.
