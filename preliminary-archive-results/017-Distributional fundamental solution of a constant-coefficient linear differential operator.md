# Mathematical Object Origin Archive | Distributional Fundamental Solution of a Constant-Coefficient Linear Differential Operator

## 1. Archive Information

- Standard Name: Distributional fundamental solution of a constant-coefficient linear differential operator
- Mathematical Field: Partial Differential Equations; Distribution Theory
- Abstract: This object is a distributional point-source response for a translation-invariant linear differential operator. It systematizes earlier operator-specific singular kernels from potential theory and related equations: the global identity \(P(D)E=\delta_0\) records the full singular contribution at the pole, while convolution with \(E\) turns the problem \(P(D)u=f\) into the superposition of translated point responses.

## 2. Core Record

### Precise Description

Let
\[
P(D)=\sum_{|\alpha|\le m}a_\alpha D^\alpha
\]
be a nonzero scalar linear differential operator with constant coefficients on \(\mathbb R^n\). A **distributional fundamental solution** for \(P(D)\) is a distribution \(E\in\mathcal D'(\mathbb R^n)\) such that
\[
P(D)E=\delta_0,
\]
where \(\delta_0\) is the Dirac distribution at the origin [2,3].

For \(f\in C_c^\infty(\mathbb R^n)\), the convolution \(u=E*f\) is defined, and constant coefficients give
\[
P(D)u=(P(D)E)*f=\delta_0*f=f.
\]
The same mechanism applies to other data when the convolution is defined. A fundamental solution is generally nonunique: if \(P(D)H=0\), then \(E+H\) is also a fundamental solution. Every nonzero constant-coefficient scalar differential operator has a distributional fundamental solution, by the Malgrange--Ehrenpreis theorem [3].

The defining equation is the distributional counterpart of classical singular normalizations. For example, take \(\Delta=\sum_j\partial_j^2\) on \(\mathbb R^n\), \(n\ge 3\). The standard radial Laplace kernel \(\Phi\) is harmonic on \(\mathbb R^n\setminus\{0\}\), has the prescribed \(|x|^{2-n}\) singular form, and is normalized by
\[
\int_{\partial B_r(0)}\partial_\nu\Phi\,dS=1.
\]
Green's identity then gives \(\Delta\Phi=\delta_0\) distributionally [1,2]. Radiality, or an equivalent restriction on the admissible singular part, matters here: total flux alone fixes only the monopole coefficient and does not exclude higher multipole singularities. Other classical equations encode the pole by suitable jump, initial-impulse, or integral identities rather than by this elliptic flux normalization.

### Mathematical Context and Formation

The motivating problem class is to solve
\[
P(D)u=f
\]
on Euclidean space for many forcing terms \(f\). The model case is Poisson's equation: a source concentrated near a point produces a field that is harmonic away from that point but singular at it. In its radially symmetric prototype, potential theory isolates a singular kernel \(\Phi\), prescribes its \(|x|^{2-n}\) singular form, normalizes its monopole strength by unit flux, and uses Green-type identities to represent the response to a distributed source. Thus point-source kernels did not depend on modern distribution theory for their first mathematical characterization; they could be specified by an equation off the pole together with sufficiently detailed singular and integral data [1].

That classical formulation nevertheless exposes the general difficulty. The equation is homogeneous at every ordinary point where the kernel is defined, so the source is carried entirely by behavior at the excluded pole. Ordinary pointwise differentiation cannot state one global equation that includes that contribution. Moreover, scalar flux records only monopole strength and is adapted to divergence-form elliptic prototypes; analogous jump formulas depend on the particular operator. For a general polynomial operator \(P(D)\), especially one with characteristic directions or higher-order singularities, there is no single pointwise normalization of the classical flux type. Operator-specific kernels therefore supplied important prototypes but not a uniform language for recording every singular term left by differentiation or for manipulating all such kernels algebraically.

The formation of the **distributional** fundamental solution consists in retaining the point-source idea while replacing operator-specific singular normalizations by the global identity \(P(D)E=\delta_0\). The Dirac distribution represents a unit source exactly, and distributional derivatives preserve all terms concentrated at the singularity instead of losing them when the pole is deleted. Translation invariance makes the response at \(y\) equal to \(E(\mathord{\cdot}-y)\), and linear superposition becomes convolution. This is a later unification and extension of classical singular kernels, not the origin of the Laplace, heat, or wave kernels themselves. It turns their common point-source structure into one object attached to a constant-coefficient operator [2,3].

### Essential Role

The object makes the forcing-dependent part of the inversion problem tractable. Once one distribution \(E\) satisfying \(P(D)E=\delta_0\) has been constructed, a solution for each compactly supported smooth \(f\) is obtained by the fixed operation \(u=E*f\), rather than by solving a new differential equation from the beginning. Three features of the definition produce this result: the Dirac distribution encodes exact unit-source normalization; constant coefficients make differentiation commute with translation and convolution; and convolution superposes the translated responses with weights \(f(y)\). The singularity is thereby incorporated into the equation rather than hidden in a deleted point and a separate limiting condition.

At a structural level, the fundamental solution separates inversion into two tasks: determine the operator's singular response once, then assemble the response prescribed by the data. The distributional formulation also makes nonuniqueness transparent, since two choices differ by a homogeneous solution. It does not, however, settle every part of a boundary-value problem. On a domain with prescribed boundary data, \(E*f\) generally requires a homogeneous correction, or replacement by a boundary-adapted Green function. For variable-coefficient operators the point response is normally a two-point kernel \(E(x,y)\), and one may initially construct only a parametrix whose error is smoother. Convolution may also be undefined for unrestricted pairs of distributions. These qualifications distinguish the fundamental solution's direct role in whole-space, translation-invariant inversion from broader applications of singular kernels.

## 3. Notes

A **Green function** is ordinarily adapted to a specified domain and boundary condition, whereas the object archived here is attached to a whole-space constant-coefficient operator. A **parametrix** is an approximate inverse, satisfying the fundamental-solution identity only modulo a controlled error. The classical singular kernels for the Laplace, heat, and wave equations are prototypes of fundamental solutions; writing their source equations with Dirac distributions is their modern unified formulation, not a claim that the kernels were first discovered through distribution theory.

## 4. Sources

[1] Lawrence C. Evans, *Partial Differential Equations*, 2nd ed., Graduate Studies in Mathematics 19, American Mathematical Society, 2010, Chapter 2.

[2] Gerald B. Folland, *Introduction to Partial Differential Equations*, 2nd ed., Princeton University Press, 1995, chapters on distributions and fundamental solutions.

[3] Lars Hörmander, *The Analysis of Linear Partial Differential Operators I: Distribution Theory and Fourier Analysis*, 2nd ed., Springer, 1990, chapters on distributions and constant-coefficient operators.
