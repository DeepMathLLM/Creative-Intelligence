# Mathematical Object Origin Archive | Poisson Kernel for the Unit Disk

## 1. Archive Information

- Standard Name: Poisson kernel for the unit disk
- Mathematical Field: Harmonic Analysis; Complex Analysis; Partial Differential Equations
- Abstract: The Poisson kernel is the positive, normalized convolution kernel that extends boundary data on the unit circle to a harmonic function in the disk. Its structure arises by solving the disk Dirichlet problem mode by mode and summing the radial factors attached to the boundary Fourier modes.

## 2. Core Record

### Precise Description

Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\) and \(\mathbb T=\partial\mathbb D\). For \(0\le r<1\), the Poisson kernel for the unit disk is
\[
P_r(\theta)=\frac{1-r^2}{1-2r\cos\theta+r^2}
           =\sum_{n\in\mathbb Z}r^{|n|}e^{in\theta}
           =1+2\sum_{n=1}^{\infty}r^n\cos(n\theta).
\]
Equivalently, for \(z\in\mathbb D\) and \(\zeta\in\mathbb T\),
\[
P(z,\zeta)=\frac{1-|z|^2}{|\zeta-z|^2},
\qquad P(re^{i\theta},e^{i\varphi})=P_r(\theta-\varphi).
\]
For integrable boundary data \(f\in L^1(\mathbb T)\), its Poisson integral is
\[
(\mathcal Pf)(re^{i\theta})=
\frac{1}{2\pi}\int_{-\pi}^{\pi}P_r(\theta-\varphi)f(e^{i\varphi})\,d\varphi.
\]
For each \(r<1\), \(P_r\) is positive and has normalized mass
\[
\frac{1}{2\pi}\int_{-\pi}^{\pi}P_r(\theta)\,d\theta=1.
\]
Moreover, \(P_r\) concentrates at \(\theta=0\) as \(r\uparrow1\), so the family is an approximate identity on \(\mathbb T\). The function \(\mathcal Pf\) is harmonic in \(\mathbb D\). If \(f\) is continuous, \(\mathcal Pf\) extends continuously to \(\overline{\mathbb D}\) with boundary values \(f\); for \(L^p\) data, the corresponding boundary convergence holds in the standard \(L^p\) and almost-everywhere senses under their usual hypotheses [1,2].

### Mathematical Context and Formation

The motivating problem is the Dirichlet problem on the disk: given a real continuous function \(f\) on \(\mathbb T\), construct a function \(u\in C(\overline{\mathbb D})\) harmonic on \(\mathbb D\) and satisfying \(u|_{\mathbb T}=f\). The mean-value property and maximum principle explain rigidity and give uniqueness once a solution exists, but neither by itself converts arbitrary boundary data into a harmonic interior function. Direct use of a holomorphic power series is also too restrictive: the boundary Fourier data of a holomorphic function contain only nonnegative frequencies, whereas a general real boundary function has both positive and negative frequencies.

Separation into angular Fourier modes reveals the required mechanism. For boundary mode \(e^{in\theta}\), regularity at the center excludes the singular radial solution and selects the harmonic extension
\[
e^{in\theta}\longmapsto r^{|n|}e^{in\theta}.
\]
Thus, if \(\widehat f(n)\) denotes the \(n\)-th Fourier coefficient, the formally forced extension is
\[
u(re^{i\theta})=\sum_{n\in\mathbb Z}\widehat f(n)r^{|n|}e^{in\theta}.
\]
The obstacle is that a continuous function's Fourier series need not converge pointwise on the boundary, so this formal mode-by-mode expression is not by itself a robust existence argument. Summing the multipliers \(r^{|n|}\) produces the closed positive kernel \(P_r\). Replacing potentially badly behaved boundary partial sums by convolution with \(P_r\) turns the formal separated solution into a well-defined integral. Positivity, unit mass, and concentration near zero then prove convergence to continuous boundary data without assuming pointwise convergence of its Fourier series. In this precise sense, the Poisson kernel packages the compatible radial evolution of every Fourier mode into the object needed to solve the boundary-value problem [1,2].

### Essential Role

The kernel makes the existence part of the disk Dirichlet problem tractable. Harmonicity follows because the Fourier coefficient of \(P_r*f\) at frequency \(n\) is \(r^{|n|}\widehat f(n)\), exactly the nonsingular harmonic radial factor for that mode. Attainment of the boundary values follows from a different, equally essential part of the same structure: \(P_r\ge0\), its normalized integral is one, and its mass outside every fixed neighborhood of zero tends to zero as \(r\uparrow1\). Consequently, \(P_r*f\to f\) uniformly for continuous \(f\). The maximum principle then supplies uniqueness, completing the solution.

This contribution is more specific than the generic statement that the Poisson kernel is useful in harmonic analysis. It converts a global boundary prescription into a weighted average whose weights are simultaneously harmonic in the interior variable and localized near the corresponding boundary point. It thereby reconciles two requirements that were separate in the original problem: satisfying Laplace's equation at every interior point and recovering arbitrary continuous data at the boundary. The Fourier expansion explains the spectral mechanism, while positivity and normalization provide a convergence argument independent of ordinary Fourier partial-sum convergence. The resulting structural viewpoint is that harmonic extension is a family of smoothing operators \(f\mapsto P_r*f\) that approaches the identity as the interior point approaches the boundary.

## 3. Notes

The Poisson kernel is not the same object as a Green function. For the disk, it can be obtained from the outward normal derivative of the Dirichlet Green function at the boundary, but it acts directly as a density for harmonic extension of boundary data. The term also has domain-dependent versions; this archive concerns the standard unit-disk kernel above.

## 4. Sources

[1] Sheldon Axler, Paul Bourdon, and Wade Ramey, *Harmonic Function Theory*, 2nd ed., Springer, 2001, chapters on the Poisson kernel and the Dirichlet problem.

[2] Elias M. Stein and Rami Shakarchi, *Fourier Analysis: An Introduction*, Princeton Lectures in Analysis I, Princeton University Press, 2003, discussions of the Poisson kernel and approximate identities.
