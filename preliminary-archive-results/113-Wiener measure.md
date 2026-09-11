# Mathematical Object Origin Archive | Wiener Measure

## 1. Archive Information

- Standard Name: Wiener measure
- Mathematical Field: Probability Theory and Stochastic Processes
- Abstract: Wiener measure is the probability law on a space of continuous paths that makes the coordinate path a standard Brownian motion. It was formed to solve the problem of assigning countably additive probabilities not merely to positions at finitely many times, but to events and functionals depending on an entire Brownian trajectory.

## 2. Core Record

### Precise Description

Fix a time horizon \(T>0\) and a dimension \(d\ge 1\), and let
\[
C_0([0,T];\mathbb R^d)=\{\omega\in C([0,T];\mathbb R^d):\omega(0)=0\}
\]
with the uniform topology and its Borel \(\sigma\)-algebra. Standard Wiener measure \(\mu_T\) is the unique Borel probability measure on this space for which the coordinate maps \(X_t(\omega)=\omega(t)\) have independent Gaussian increments with the Brownian normalization. Explicitly, if
\(0=t_0<t_1<\cdots<t_n\le T\) and \(A_1,\ldots,A_n\) are Borel subsets of \(\mathbb R^d\), then
\[
\mu_T\!\left(\bigcap_{i=1}^n
 \{\omega:X_{t_i}(\omega)-X_{t_{i-1}}(\omega)\in A_i\}\right)
=
\prod_{i=1}^n\int_{A_i}
\frac{\exp\!\left(-\frac{|x|^2}{2(t_i-t_{i-1})}\right)}
{[2\pi(t_i-t_{i-1})]^{d/2}}\,dx.
\]
Equivalently, the coordinate process is centered Gaussian and
\[
\mathbb E_{\mu_T}[X_s^jX_t^k]=\delta_{jk}\min\{s,t\}.
\]
Thus the definition combines two kinds of structure: prescribed finite-dimensional Gaussian laws and concentration of the resulting law on continuous paths. The latter is substantive; compatible distributions at finitely many times do not, by themselves, express continuity of a sample path. Modern constructions obtain existence by extending the consistent cylinder probabilities and proving, from increment estimates, that the law has a continuous version or is carried by continuous paths [3].

### Mathematical Context and Formation

The motivating problem was to turn the Brownian-motion model into a rigorous probability theory of whole trajectories. The model supplied Gaussian transition densities—equivalently, the heat kernel after a choice of diffusion normalization—for a particle's displacement over each time interval. These densities answer questions involving finitely many observations \(B_{t_1},\ldots,B_{t_n}\), but many natural Brownian questions concern a complete path: whether it crosses a level, its maximum on an interval, or the value of a functional such as \(\int_0^T F(B_t)\,dt\). Ordinary finite-dimensional integration could not assign a coherent probability or average to all such path events and functionals.

The exact obstruction was therefore not the Gaussian formula itself, but its passage to an infinite-dimensional, countably additive law with the required regularity. Cylinder probabilities had to agree whenever observation times were inserted or removed; they then had to extend beyond cylinder events; and the extended law had to describe continuous trajectories rather than arbitrary functions on an uncountable time set. There is no finite-dimensional Lebesgue-volume construction that can simply be transferred to this path space.

Wiener's work on Brownian movement and averages of functionals addressed this obstruction directly [1]. The formative insight was to regard a trajectory as the variable of integration: prescribe the Gaussian probabilities of finitely sampled coordinates and use limiting control to define averages of functionals on the function space. In *Differential-Space*, Wiener developed this construction into the object now called Wiener measure [2]. In modern measure-theoretic language, consistency handles the finite-dimensional specifications, while Gaussian increment bounds supply the tightness or continuity control needed to realize the law on \(C_0([0,T];\mathbb R^d)\) [3]. This modern description clarifies the mathematical mechanism but is not a claim that Wiener used the later Kolmogorov-extension terminology.

### Essential Role

Wiener measure made the missing path-space step tractable. Its cylinder-set prescription retains exactly the known Gaussian transition law and independence of disjoint-time increments. Countable additivity then permits limits of increasingly refined finite-time events, while support on continuous functions turns statements about crossing, extrema, and other global path properties into measurable questions about subsets or functionals of one fixed space. Under \(\mu_T\), the canonical coordinate map is itself a Brownian motion, so a separate informal notion of a “random curve” is unnecessary.

The object consequently reformulated the original problem: instead of trying to choose a typical path or put a nonexistent uniform volume on function space, one studies the nonuniform Gaussian probability measure \(\mu_T\). A path property holds almost surely precisely when its corresponding measurable subset has Wiener measure one, and the expected value of a path functional \(G\) is the ordinary measure-theoretic integral \(\int G(\omega)\,d\mu_T(\omega)\) when defined. This did not smooth Brownian paths—indeed their roughness remains—but it provided the rigorous framework in which that roughness and other whole-trajectory phenomena could be stated and proved. The deeper structural viewpoint introduced here is that a continuous stochastic process can be represented by a probability measure on a function space, with time evaluations recovered as coordinate random variables.

## 3. Notes

Wiener measure is a measure, whereas a Wiener process (standard Brownian motion) is a stochastic process having that measure as its law; the canonical process on Wiener space is the coordinate family \(X_t(\omega)=\omega(t)\). The triple \((C_0([0,T];\mathbb R^d),\mathcal B,\mu_T)\) is commonly called classical Wiener space. Different diffusion conventions replace covariance \(\min(s,t)I_d\) by a constant multiple. The account of formation above is a mathematical reconstruction in modern language; the primary sources use the functional-integration framework available at the time.

## 4. Sources

[1] Norbert Wiener, “The Average of an Analytic Functional and the Brownian Movement,” *Proceedings of the National Academy of Sciences of the United States of America* 7 (1921), 294–298.

[2] Norbert Wiener, “Differential-Space,” *Journal of Mathematics and Physics* 2, nos. 1–4 (1923), 131–174, https://doi.org/10.1002/sapm192321131.

[3] Michael E. Taylor, “Wiener Measure and Brownian Motion,” Chapter 16 in *Measure Theory and Integration*, online chapter, https://mtaylor.web.unc.edu/wp-content/uploads/sites/16915/2018/04/taylor2-chap16.pdf.
