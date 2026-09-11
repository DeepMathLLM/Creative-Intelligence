# Mathematical Object Origin Archive | Viscosity Solution

## 1. Archive Information

- Standard Name: Viscosity solution
- Mathematical Field: Partial Differential Equations
- Abstract: A viscosity solution is a generalized solution of a nonlinear first- or second-order partial differential equation whose differential inequalities are tested against smooth functions touching the candidate from above or below. It was formed to make Hamilton–Jacobi equations well posed after classical differentiability breaks down, while retaining the selection imposed by vanishing-viscosity approximation and supporting comparison-based uniqueness.

## 2. Core Record

### Precise Description

Let \(\Omega\subset \mathbb{R}^n\) be open and consider
\[
F(x,u,Du,D^2u)=0,
\qquad
F:\Omega\times\mathbb{R}\times\mathbb{R}^n\times\mathbb{S}^n\to\mathbb{R},
\]
where \(\mathbb S^n\) denotes the symmetric \(n\times n\) matrices. An upper-semicontinuous function \(u\) is a viscosity subsolution if, whenever \(\phi\in C^2(\Omega)\) and \(u-\phi\) has a local maximum at \(x_0\),
\[
F\bigl(x_0,u(x_0),D\phi(x_0),D^2\phi(x_0)\bigr)\le 0.
\]
A lower-semicontinuous function \(u\) is a viscosity supersolution if, whenever \(u-\phi\) has a local minimum at \(x_0\), the reverse inequality holds. A continuous function is a viscosity solution if it is both. Equivalent formulations use second-order superjets and subjets. For a first-order Hamilton–Jacobi equation
\[
u_t+H(x,t,D_xu)=0,
\]
the same definition is made in space-time with \(C^1\) test functions and the corresponding inequality for \(\phi_t+H(x,t,D_x\phi)\). Boundary and initial data are imposed in a formulation appropriate to the problem; the interior definition alone does not guarantee existence or uniqueness [2].

The definition is meaningful at a corner of \(u\): it never assigns a derivative to \(u\) there. Instead, it reads the derivatives of every smooth function that touches the graph locally from the relevant side. If \(u\) is smooth, choosing suitable touching functions recovers the classical equation, so the generalized notion is consistent with classical solutions [2].

### Mathematical Context and Formation

The motivating problem class was the Cauchy and boundary-value theory for nonlinear Hamilton–Jacobi equations, including
\[
u_t+H(x,t,D_xu)=0,
\qquad u(x,0)=g(x).
\]
Even with smooth data, characteristic curves can meet. The gradient then develops discontinuities and the solution develops corners, so a global classical \(C^1\) solution may not exist. Merely requiring the equation almost everywhere does not resolve the problem: it forgets what should happen at the nondifferentiable points and can admit incompatible continuations. For example, on \((-1,1)\), both \(u(x)=1-|x|\) and \(v(x)=|x|-1\) satisfy \(|w'|=1\) almost everywhere and vanish at \(x=\pm1\), but only the distance function \(u(x)=1-|x|\) is the viscosity solution of the Dirichlet problem. At the interior minimum of \(v\), the constant test function touching from below has derivative zero and violates the supersolution inequality \(|\phi'|-1\ge0\).

A standard regularization replaces the first-order equation by a parabolic one,
\[
u_t^\varepsilon+H(x,t,D_xu^\varepsilon)=\varepsilon\Delta u^\varepsilon,
\]
and lets \(\varepsilon\downarrow0\). The regularized solutions are smooth enough for classical differential arguments, but their limit need not be differentiable. An integration-by-parts weak formulation, effective for divergence-form equations, is not intrinsic for a general nonlinear nondivergence expression \(H(Du)\), and an almost-everywhere formulation does not preserve the regularization's uniqueness selection. The decisive insight was to encode the one-sided differential information surviving the limit by smooth comparison functions: a function touching from above yields the subsolution inequality, while one touching from below yields the supersolution inequality. The name “viscosity solution” records this connection with vanishing viscosity. Crandall and Lions developed this solution object for Hamilton–Jacobi equations in 1983 [1]; its systematic second-order formulation is presented in [2].

Thus the formation of the object was not simply a weakening of differentiability. It combined three requirements forced by the motivating problem: agreement with classical solutions where derivatives exist, stability under limits of regularized solutions, and an order-sensitive formulation strong enough to support comparison and hence select at most one admissible solution.

### Essential Role

For Hamilton–Jacobi problems, the viscosity solution makes the post-characteristic-crossing regime tractable. Its touching-test definition replaces unavailable pointwise derivatives without discarding information at corners. The two one-sided conditions distinguish admissible from inadmissible cusps: in the eikonal example above, the supersolution test at the downward cusp rules out \(|x|-1\), something the almost-everywhere equation cannot do.

The same local order structure is what enters comparison arguments. Under the standard structural hypotheses on \(F\) (such as continuity and proper degenerate ellipticity, together with suitable domain and boundary assumptions), one proves that every viscosity subsolution lies below every viscosity supersolution. This yields uniqueness once existence is obtained. The definition is also stable under locally uniform limits—and, in the semicontinuous framework, under appropriate half-relaxed limits—so limits of vanishing-viscosity regularizations or consistent monotone approximations remain solutions of the limiting equation [2]. These are not incidental later benefits: stability supplies existence through approximation, while comparison supplies uniqueness, directly repairing the two failures of the naive generalized formulations.

The deeper structural change was to reformulate a nonlinear PDE as a local comparison property rather than as an identity requiring derivatives of the unknown. This made nonsmoothness part of the solution concept while preserving the equation's directional and order information. It also separated the definition from particular formulas for characteristics, allowing the same mechanism to cover fully nonlinear degenerate elliptic equations, though such second-order scope is a subsequent generalization of the original Hamilton–Jacobi setting [2].

## 3. Notes

“Viscosity” here does not mean that the limiting equation contains physical viscosity, nor does it assert that every viscosity solution is obtained from one fixed viscous regularization. The term reflects the vanishing-viscosity selection mechanism. Viscosity solutions are also distinct from distributional solutions: neither notion contains the other without additional hypotheses, because their test procedures encode different structures. Comparison, existence, and boundary attainment require hypotheses beyond the bare definition.

## 4. Sources

[1] Michael G. Crandall and Pierre-Louis Lions, “Viscosity Solutions of Hamilton-Jacobi Equations,” *Transactions of the American Mathematical Society* **277** (1983), no. 1, 1–42. https://doi.org/10.1090/S0002-9947-1983-0690039-8

[2] Michael G. Crandall, Hitoshi Ishii, and Pierre-Louis Lions, “User’s Guide to Viscosity Solutions of Second Order Partial Differential Equations,” *Bulletin of the American Mathematical Society* **27** (1992), no. 1, 1–67. https://doi.org/10.1090/S0273-0979-1992-00266-5
