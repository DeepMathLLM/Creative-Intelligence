# Mathematical Object Origin Archive | Kružkov Entropy Solution

## 1. Archive Information

- Standard Name: Kružkov entropy solution
- Mathematical Field: Partial Differential Equations
- Abstract: A Kružkov entropy solution is the admissible weak solution concept for the Cauchy problem for a scalar conservation law. It supplements distributional conservation with a one-parameter family of inequalities indexed by constant states. Those inequalities exclude nonphysical weak shocks and, through an $L^1$ comparison argument, restore uniqueness and stability after classical solutions form discontinuities.

## 2. Core Record

### Precise Description

Consider the scalar Cauchy problem
\[
\partial_t u+\operatorname{div}_x f(u)=0
    \quad\text{in }\mathbb{R}^d\times(0,\infty),
    \qquad u(x,0)=u_0(x),
\]
where, in a standard formulation, $f:\mathbb{R}\to\mathbb{R}^d$ is $C^1$ and $u_0\in L^\infty(\mathbb{R}^d)$. A bounded measurable function $u$ is a **Kružkov entropy solution** if it is a distributional weak solution, has initial trace $u_0$ in $L^1_{\mathrm{loc}}$, and for every constant $k\in\mathbb{R}$ satisfies
\[
\partial_t |u-k|
 +\operatorname{div}_x\!\left(
   \operatorname{sgn}(u-k)\bigl(f(u)-f(k)\bigr)
 \right)\le 0
\]
in the sense of distributions [1,2]. Equivalently, for every nonnegative
$\varphi\in C_c^\infty(\mathbb{R}^d\times[0,\infty))$,
\[
\begin{aligned}
&\int_0^\infty\!\int_{\mathbb{R}^d}
 \left[
 |u-k|\,\partial_t\varphi
 +\operatorname{sgn}(u-k)\bigl(f(u)-f(k)\bigr)\cdot\nabla_x\varphi
 \right]dx\,dt\\
&\hspace{35mm}+\int_{\mathbb{R}^d}|u_0-k|\,\varphi(x,0)\,dx\ge 0.
\end{aligned}
\]
The pairs
\[
\eta_k(z)=|z-k|,
\qquad
q_k(z)=\operatorname{sgn}(z-k)\bigl(f(z)-f(k)\bigr)
\]
are the Kružkov entropy--entropy-flux pairs. The definition is an inequality rather than an additional conservation identity: entropy may be dissipated across shocks.

### Mathematical Context and Formation

The motivating problem is the global Cauchy problem for nonlinear scalar conservation laws after shock formation. The method of characteristics can construct a classical solution only while characteristics do not intersect. For a nonlinear flux, different characteristic speeds can cause intersection in finite time, at which point the gradient becomes unbounded and a discontinuity forms. Requiring a classical solution then gives no global object.

Passing to distributional weak solutions admits discontinuities and preserves the conservation law, but it loses uniqueness. The obstruction is already explicit for Burgers' equation
\[
u_t+\left(\frac{u^2}{2}\right)_x=0.
\]
For Riemann data $u_0=u_L$ on $x<0$ and $u_0=u_R$ on $x>0$ with $u_L<u_R$, both the centered rarefaction and the discontinuous expansion shock moving at the Rankine--Hugoniot speed $(u_L+u_R)/2$ satisfy the weak conservation identity. The identity determines the speed of a jump but does not determine whether characteristics should enter or emerge from it; hence it cannot reject the expansion shock.

The relevant insight is to retain, in weak form, the inequalities obeyed by regularized solutions. For the viscous approximation
\[
\partial_tu^\varepsilon+\operatorname{div}f(u^\varepsilon)
   =\varepsilon\Delta u^\varepsilon,
\]
a smooth convex function $\eta$ and the associated flux $q$, defined by
$q'(z)=\eta'(z)f'(z)$, obey
\[
\partial_t\eta(u^\varepsilon)+\operatorname{div}q(u^\varepsilon)
\le \varepsilon\Delta\eta(u^\varepsilon).
\]
The nonpositive defect $-\varepsilon\eta''(u^\varepsilon)|\nabla u^\varepsilon|^2$ is what changes an equality into an inequality. In the vanishing-viscosity limit this yields entropy inequalities that express admissibility even when derivatives of $u$ no longer exist classically. Kružkov's decisive scalar formulation uses the nonsmooth convex family $|u-k|$ for every constant state $k$ [1]. This family is rich enough to compare two merely bounded solutions directly, while avoiding a definition that depends on retaining a particular viscous approximating sequence. Thus the object was formed to solve a precise gap between existence and well-posedness: weak solutions survived shocks, but did not select a unique continuation.

### Essential Role

The Kružkov inequalities make the uniqueness portion of the scalar Cauchy problem tractable. Applying the inequalities for one solution $u$ with level $k=v(y,s)$ and for another solution $v$ with level $k=u(x,t)$, then regularizing and doubling the space-time variables, produces a distributional comparison inequality of Kato type. Under the usual integrability hypotheses it gives the contraction estimate
\[
\|u(t)-v(t)\|_{L^1(\mathbb{R}^d)}
\le
\|u_0-v_0\|_{L^1(\mathbb{R}^d)}.
\]
Consequently equal initial data give equal entropy solutions; nearby data remain controlled; and the solution evolution has a canonical, stable continuation through shock formation [1,2].

This result depends on the specific structure of the object. The parameter $k$ supplies every constant comparison state, the absolute value measures exactly the $L^1$ separation, and the signed flux difference matches that separation to the nonlinear conservation flux. Together these features convert shock admissibility from a jump-by-jump geometric rule into an inequality valid for arbitrary bounded weak solutions, including solutions without well-defined shock curves. In the Burgers Riemann problem, the entropy inequalities retain the rarefaction and exclude the expansion shock, resolving the concrete nonuniqueness left by the Rankine--Hugoniot condition.

Existence and selection also fit the same structure: limits produced by vanishing viscosity satisfy the inequalities, while $L^1$ contraction shows that any two such limits must coincide. The direct achievement is therefore not merely permission to use discontinuous solutions. It is the closure of the global scalar theory into a well-posed admissible solution class, with entropy dissipation providing the missing directionality at shocks.

## 3. Notes

“Kružkov entropy solution” here refers to scalar conservation laws with sufficiently regular flux. Entropy solutions for systems, conservation laws with discontinuous or spatially dependent flux, and boundary-value problems require additional entropy or boundary admissibility structures; the scalar Kružkov condition should not be asserted unchanged as a complete theory in those settings. The spelling “Kruzhkov” is a common transliteration of “Kružkov.”

## 4. Sources

[1] S. N. Kružkov, “First Order Quasilinear Equations in Several Independent Variables,” *Mathematics of the USSR-Sbornik* **10** (1970), 217–243. https://doi.org/10.1070/SM1970v010n02ABEH002156

[2] C. M. Dafermos, *Hyperbolic Conservation Laws in Continuum Physics*, 4th ed., Grundlehren der mathematischen Wissenschaften 325, Springer, 2016. https://doi.org/10.1007/978-3-662-49451-6
