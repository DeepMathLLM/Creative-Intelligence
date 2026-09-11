# Mathematical Object Origin Archive | Fredholm Determinant

## 1. Archive Information

- Standard Name: Fredholm determinant
- Mathematical Field: Functional Analysis
- Abstract: The Fredholm determinant is an infinite-dimensional analogue of a matrix determinant attached, in its original kernel form, to a linear integral equation of the second kind. It arose to decide solvability for all values of the equation's parameter and, away from its zeros, to furnish the resolvent and hence the solution.

## 2. Core Record

### Precise Description

Let
\[
(Au)(x)=\int_a^b K(x,y)u(y)\,dy
\]
for a continuous kernel \(K\) on \([a,b]^2\). The classical Fredholm determinant associated with \(I+zA\) is the entire function
\[
D(z)=1+\sum_{n=1}^{\infty}\frac{z^n}{n!}
\int_{[a,b]^n}
\det\!\bigl[K(x_i,x_j)\bigr]_{i,j=1}^{n}
\,dx_1\cdots dx_n.
\]
The determinant inside each integral is an ordinary \(n\times n\) determinant; thus the definition packages determinants of all finite orders into one scalar function. Under the classical continuous-kernel hypotheses, the series converges for every \(z\), and \(D(z)\neq0\) exactly when \(I+zA\) is invertible. In that case a companion series, the first Fredholm minor, divided by \(D(z)\), gives the kernel of the resolvent [1,2].

In modern operator language, if \(T\) is trace class on a separable Hilbert space, then
\[
\det(I+zT)=\prod_j(1+z\lambda_j(T)),
\]
where nonzero eigenvalues are repeated according to algebraic multiplicity. Near \(z=0\), equivalently,
\[
\det(I+zT)=\exp\!\left(\sum_{m=1}^{\infty}
\frac{(-1)^{m+1}z^m}{m}\operatorname{tr}(T^m)\right).
\]
This operator determinant is entire in \(z\), and it agrees with the integral series when both formulations' hypotheses apply [2,3]. A continuous kernel always yields a compact integral operator, but not necessarily a trace-class operator, so the classical kernel formulation and the modern trace-class formulation should not be identified without the additional hypotheses.

### Mathematical Context and Formation

The motivating problem class was to solve, for a prescribed continuous \(f\) and kernel \(K\), the parameter-dependent equation
\[
u(x)+z\int_a^bK(x,y)u(y)\,dy=f(x),
\qquad\text{or}\qquad (I+zA)u=f,
\]
and to identify precisely the exceptional values of \(z\) for which uniqueness or existence fails [1,2]. Such integral equations arose, in particular, when boundary-value problems were reformulated as equations for an unknown boundary or source density [1].

For a degenerate kernel \(K(x,y)=\sum_{r=1}^N p_r(x)q_r(y)\), the problem reduces to a finite linear system: an ordinary determinant detects singular parameter values, while Cramer's rule supplies a quotient formula for the solution. General continuous kernels do not reduce exactly to finitely many coefficients. Direct successive substitution produces a Neumann series, but its elementary norm estimate guarantees convergence only when \(|z|\lVert A\rVert<1\); it therefore does not by itself describe all parameter values or isolate the exceptional ones. The missing ingredient was a convergent infinite-order replacement for the finite system's determinant and minors.

Fredholm's construction retained the finite-dimensional algebraic mechanism rather than attempting unrestricted iteration: finite kernel approximations suggested forming determinants from sampled kernel values, integrating them, and summing over every order with the normalization \(1/n!\). This led to \(D(z)\) and the corresponding Fredholm minors [1,2]. The formation is thus mathematically tied to a specific obstacle: extending determinant-based solvability and Cramer-type formulas from finite-rank equations to integral operators without restricting the parameter to the local convergence region of the Neumann series.

### Essential Role

The determinant made the parameter obstruction explicit. For the continuous-kernel equation above, \(D(z)\neq0\) implies that the equation has one solution for every \(f\); the quotient of the first Fredholm minor by \(D(z)\) is the resolvent kernel, so the solution can be written by a single integral formula rather than only as a locally convergent iteration [1,2]. When \(D(z)=0\), the parameter is exceptional: the homogeneous equation has nonzero solutions, and solvability of the inhomogeneous equation is governed by compatibility with solutions of the adjoint homogeneous equation, the content of the Fredholm alternative [4].

Specific features of the object accomplish this. The finite determinants impose the same alternating multilinear cancellations that detect linear dependence in matrix problems; integration removes dependence on a chosen discretization; summation over all orders incorporates arbitrarily high finite-rank information; and the factorial normalization supports convergence to an analytic function. Consequently, zeros of one scalar analytic object encode loss of invertibility, while its associated minors encode the inverse where it exists. This did more than give a formula: it reformulated solvability of an infinite-dimensional equation as a finite-dimensional-looking dichotomy between regular parameters and determinant zeros, exposing the discrete nature of the obstruction for compact integral operators.

## 3. Notes

The Fredholm determinant is distinct from the Fredholm alternative: the determinant is the scalar analytic object, whereas the alternative is a solvability theorem. It is also distinct from a Fredholm minor, which is a numerator used in the resolvent formula. For Hilbert–Schmidt operators that are not trace class, regularized determinants such as \(\det_2(I+T)\) are later extensions and are not the object documented here [3].

## 4. Sources

[1] I. Fredholm, “Sur une classe d’équations fonctionnelles,” *Acta Mathematica* **27** (1903), 365–390. https://doi.org/10.1007/BF02421317

[2] F. Bornemann, “On the Numerical Evaluation of Fredholm Determinants,” *Mathematics of Computation* **79** (2010), 871–915. https://doi.org/10.1090/S0025-5718-09-02280-7

[3] B. Simon, *Trace Ideals and Their Applications*, 2nd ed., Mathematical Surveys and Monographs 120, American Mathematical Society, 2005.

[4] R. Kress, *Linear Integral Equations*, 3rd ed., Applied Mathematical Sciences 82, Springer, 2014.
