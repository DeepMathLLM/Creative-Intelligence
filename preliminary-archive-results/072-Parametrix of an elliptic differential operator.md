# Mathematical Object Origin Archive | Parametrix of an Elliptic Differential Operator

## 1. Archive Information

- Standard Name: Parametrix of an elliptic differential operator
- Mathematical Field: Partial Differential Equations
- Abstract: A parametrix is an approximate inverse to a differential operator whose failure to be an exact inverse is more regular than the original problem. It was formed to address the construction and local solution of variable-coefficient elliptic equations, where the translation-invariant fundamental-solution method for constant coefficients no longer applies. Freezing the principal coefficients captures the required diagonal singularity, while the resulting weaker error can be corrected by an integral equation. In modern pseudodifferential language, an elliptic parametrix inverts the principal symbol and is an inverse modulo smoothing operators.

## 2. Core Record

### Precise Description

Let \(M\) be a smooth manifold, let \(E,F\to M\) be vector bundles, and let
\[
L:C^\infty(M;E)\longrightarrow C^\infty(M;F)
\]
be an elliptic differential operator of order \(m\). A two-sided parametrix for \(L\) is an operator \(Q\), normally chosen as a properly supported pseudodifferential operator of order \(-m\), such that
\[
LQ=I-R_1,\qquad QL=I-R_2,
\]
where \(R_1\) and \(R_2\) are smoothing operators. Locally, a smoothing operator sends distributions to smooth functions and has a smooth Schwartz kernel. If only one identity holds, \(Q\) is respectively a right or left parametrix. Thus a parametrix need not solve \(Lu=f\) exactly; it reproduces an inverse up to an error that contains no singularities [2].

For a scalar second-order uniformly elliptic operator on a domain in \(\mathbb R^n\),
\[
L=\sum_{i,j=1}^n a^{ij}(x)\partial_i\partial_j+
  \sum_{i=1}^n b^i(x)\partial_i+c(x),
\]
a classical Levi parametrix is first represented by a kernel. For each source point \(y\), freeze the principal coefficients and set
\[
L_y=\sum_{i,j=1}^n a^{ij}(y)\partial_i\partial_j.
\]
If \(\Gamma_y(x-y)\) is a fundamental solution of \(L_y\), then, after localization by a cutoff, \(P(x,y)=\Gamma_y(x-y)\) is a first parametrix kernel. In the distributional sense,
\[
L_xP(x,y)=\delta_y(x)+K(x,y),
\]
where \(K\) is the error kernel produced by \(a^{ij}(x)-a^{ij}(y)\), the lower-order terms, and the cutoff. Under suitable coefficient regularity, the integral operator defined by \(K\) is more regular, or locally small in an appropriate norm, so that correcting \(P\) reduces to solving an equation of the form \((I+K)\phi=f\) [1].

### Mathematical Context and Formation

The motivating problem class was to solve
\[
Lu=f
\]
locally, and in particular to construct a fundamental solution or Green-type kernel, for elliptic operators whose coefficients vary with position. For a constant-coefficient operator \(L(D)\), translation invariance turns the problem into division by its symbol under the Fourier transform, and an exact fundamental solution can be used by convolution. When the coefficients are \(a^{ij}(x)\), Fourier transformation does not diagonalize \(L\): multiplication by the coefficients becomes interaction between frequencies, and no single convolution kernel can invert the operator. Directly demanding an exact variable-coefficient fundamental solution therefore places the unknown singular kernel at the beginning of the argument rather than producing it [1].

The decisive insight was that the hardest part of the inverse problem is local and is governed by the principal coefficients at the singular point. Freezing those coefficients at \(y\) gives the constant-coefficient operator \(L_y\), whose fundamental solution has the correct leading singularity. This approximation is not merely formal. For \(n\ge 3\), a second-order elliptic fundamental solution has leading size \(|x-y|^{2-n}\), so its second derivatives have size \(|x-y|^{-n}\). If the principal coefficients are Lipschitz, then
\[
a^{ij}(x)-a^{ij}(y)=O(|x-y|),
\]
and their product with those second derivatives is of size \(|x-y|^{1-n}\), which is locally integrable. The coefficient difference therefore cancels one degree of the otherwise nonintegrable diagonal singularity. Lower-order terms are also less singular. The analogous logarithmic behavior in dimension two leads to the same qualitative improvement [1].

Consequently, applying \(L\) to the frozen-coefficient kernel produces the identity plus an integral error of lower singular strength. On a sufficiently small neighborhood that error can be treated by a convergent Neumann-series correction, or by a related Fredholm integral argument. The object needed between the explicit but inexact frozen kernel and the inaccessible exact inverse is precisely the parametrix: an approximate fundamental solution with a controlled remainder. This is the mathematical formation embodied in the classical parametrix method associated with E. E. Levi [1].

The pseudodifferential construction expresses the same mechanism algebraically in phase space. If \(p_m(x,\xi)\) is the elliptic principal symbol of \(L\), then \(p_m(x,\xi)\) is invertible for \(\xi\ne0\). One starts with a symbol \(q_{-m}=p_m^{-1}\) away from the zero section. Composition gives an identity plus a symbol of lower order; recursively chosen lower-order terms remove successive defects, and an asymptotic sum leaves a remainder in \(\Psi^{-\infty}\). Quantization of that symbol gives \(Q\) with \(LQ-I\) and \(QL-I\) smoothing [2].

### Essential Role

For the original variable-coefficient problem, the parametrix made the singular part of inversion explicit without presupposing an exact fundamental solution. Its frozen-coefficient kernel imported the known singular model at each source point; the vanishing coefficient difference \(a(x)-a(y)\) weakened the error at the diagonal; and the definition allowed that weaker error to remain temporarily. The difficult PDE inversion was thereby split into two tractable tasks: construct the universal local singular model, then invert an operator of the form \(I+K\), where \(K\) is less singular and can be made small locally. Correcting the parametrix yields an actual local inverse or fundamental solution when the relevant convergence hypotheses hold [1].

The allowance of a regularizing remainder is essential, not incidental. Exact inversion can be obstructed globally by a nonzero kernel or cokernel, whereas inversion modulo smoothing ignores precisely the part irrelevant to local singular behavior. From
\[
QL=I-R_2
\]
one has
\[
u=Q(Lu)+R_2u.
\]
Because \(Q\) gains \(m\) derivatives and \(R_2u\) is smooth, regularity of \(Lu\) forces the corresponding elliptic regularity of \(u\). Thus the same structure that repaired the construction of a variable-coefficient inverse also isolated the deeper principle that ellipticity controls singularities through the invertibility of the principal symbol [2]. On a compact manifold the smoothing remainders are compact on the relevant Sobolev spaces, so the parametrix also converts global inversion into a finite-dimensional Fredholm obstruction; this is a structural consequence of the object rather than the original local motivation [2].

## 3. Notes

- A fundamental solution is an exact distributional kernel for which \(L_xE(x,y)=\delta_y(x)\); a parametrix satisfies this only up to a more regular error. The correction step may turn a parametrix into a fundamental solution, but the two objects should not be identified.
- “Parametrix” can mean the classical approximate fundamental-solution kernel or the associated integral operator. In modern analysis it most often means a left or right inverse modulo smoothing operators [1].
- The formation account above is a mathematical reconstruction connecting the motivating inverse problem to the defining structure. The attribution to Levi is limited to the classical parametrix method reported in [1]; no claim is made that every modern pseudodifferential formulation occurred at the same stage.

## 4. Sources

[1] Encyclopedia of Mathematics, “Parametrix method,” https://encyclopediaofmath.org/wiki/Parametrix_method (accessed 2025-02-25).

[2] Semyon Dyatlov, “Pseudodifferential Operators and Elliptic Regularity,” lecture notes, 2010, https://math.mit.edu/~dyatlov/files/2010/psdoer.pdf.
