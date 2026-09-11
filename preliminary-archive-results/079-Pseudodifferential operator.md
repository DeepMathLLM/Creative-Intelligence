# Mathematical Object Origin Archive | Pseudodifferential Operator

## 1. Archive Information

- Standard Name: Pseudodifferential operator
- Mathematical Field: Partial Differential Equations
- Abstract: A pseudodifferential operator is a Fourier-type operator whose multiplier may depend smoothly on position and need not be polynomial in frequency. The object was formed to construct approximate inverses, or parametrices, for variable-coefficient elliptic differential operators: ordinary Fourier multipliers invert constant-coefficient operators, whereas differential operators do not contain the negative-order, nonpolynomial operators required in the variable-coefficient case. Symbol estimates and an asymptotic composition calculus make that inverse construction rigorous modulo smoothing errors.

## 2. Core Record

### Precise Description

Let \(U\subset\mathbb R^n\) be open and write \(\langle\xi\rangle=(1+|\xi|^2)^{1/2}\). A symbol of order \(m\), in the standard class \(S^m_{1,0}(U\times\mathbb R^n)\), is a function \(a\in C^\infty(U\times\mathbb R^n)\) such that for every compact \(K\Subset U\) and all multi-indices \(\alpha,\beta\),
\[
 |\partial_x^\alpha\partial_\xi^\beta a(x,\xi)|
 \le C_{K,\alpha,\beta}\langle\xi\rangle^{m-|\beta|},
 \qquad x\in K.
\]
Its Kohn–Nirenberg quantization is
\[
 \operatorname{Op}(a)u(x)
   =(2\pi)^{-n}\int_{\mathbb R^n}e^{ix\cdot\xi}a(x,\xi)\widehat u(\xi)\,d\xi,
 \qquad u\in C_c^\infty(U),
\]
interpreted locally, or equivalently by the corresponding oscillatory kernel with phase \((x-y)\cdot\xi\). An operator locally of this form, up to an operator with a smooth Schwartz kernel, is a pseudodifferential operator of order \(m\), written \(A\in\Psi^m(U)\). Proper support is imposed when one needs unrestricted composition on an open set. On a smooth manifold the definition is made in coordinate charts and patched; the class is invariant under coordinate changes.

A differential operator \(P=\sum_{|\alpha|\le m}a_\alpha(x)D^\alpha\) is the special case whose symbol \(p(x,\xi)=\sum a_\alpha(x)\xi^\alpha\) is polynomial in \(\xi\). Thus pseudodifferential operators enlarge differential operators by allowing nonpolynomial frequency dependence and negative or nonintegral orders while preserving controlled differentiation in \(x\) and \(\xi\). In the classical subclass, symbols have asymptotic homogeneous expansions. Its leading homogeneous term is the principal symbol. A classical operator of order \(m\) is elliptic where that term is invertible for \(\xi\ne0\); in a nonhomogeneous formulation this is expressed by a lower bound \(|a(x,\xi)|\ge c\langle\xi\rangle^m\) for large \(|\xi|\), locally in \(x\).

### Mathematical Context and Formation

The motivating problem class is local inversion and regularity for variable-coefficient elliptic equations
\[
 Pu=f,
 \qquad
 P=\sum_{|\alpha|\le m}a_\alpha(x)D^\alpha.
\]
For a constant-coefficient operator, Fourier transformation changes differentiation into multiplication: \(\widehat{Pu}(\xi)=p(\xi)\widehat u(\xi)\). Away from the zeros of \(p\), one is therefore led to divide by \(p(\xi)\); a cutoff version of \(1/p(\xi)\) gives a Fourier multiplier of order \(-m\). For variable coefficients, however, Fourier transformation does not diagonalize \(P\): multiplication by \(a_\alpha(x)\) becomes convolution in frequency. Pointwise division by a single function of \(\xi\) is no longer an inverse construction.

Neither of the immediate available classes resolves this obstruction. Differential operators describe \(P\), but their symbols are polynomial in \(\xi\), while even the leading candidate for an inverse is \(p_m(x,\xi)^{-1}\), a nonpolynomial symbol of order \(-m\). Translation-invariant Fourier multipliers allow nonpolynomial functions of \(\xi\), but cannot track the spatial variation of \(p_m(x,\xi)\). Freezing coefficients supplies only a first approximation: composing that approximation with \(P\) produces lower-order errors involving derivatives of the coefficients, and no finite polynomial construction cancels the resulting sequence of errors.

The decisive enlargement was to retain the Fourier oscillation but allow a controlled symbol \(a(x,\xi)\) depending on both position and frequency. The derivative bounds defining \(S^m_{1,0}\) make these operators stable under composition, with a symbol determined asymptotically by derivatives in \(\xi\) of one factor and derivatives in \(x\) of the other. Starting from a cutoff reciprocal of the elliptic principal symbol, one can then cancel the composition error order by order. Asymptotic summation turns the formal sequence of corrections into one genuine symbol, while the uncancelled remainder has order \(-\infty\) and hence is smoothing. The modern pseudodifferential calculus systematized in the work of Kohn and Nirenberg and Hörmander was shaped around precisely this parametrix and regularity problem for variable-coefficient differential equations [1][2].

### Essential Role

Let \(P\in\Psi^m\) be elliptic, initially a differential operator, with principal symbol \(p_m(x,\xi)\). Choose a high-frequency cutoff \(\chi\) and begin with
\[
 q_{-m}(x,\xi)=\frac{\chi(x,\xi)}{p_m(x,\xi)}.
\]
The pseudodifferential composition formula expands the symbol of \(\operatorname{Op}(q)P\) in terms of products \(\partial_\xi^\alpha q\,\partial_x^\alpha p\). It exposes the error after the leading reciprocal as a symbol of successively lower orders. Corrections \(q_{-m-1},q_{-m-2},\ldots\) can therefore be chosen recursively to cancel those orders, and symbolic asymptotic summation produces \(q\in S^{-m}\). For \(Q=\operatorname{Op}(q)\), one obtains locally, or globally for properly supported operators,
\[
 QP=I-R,
 \qquad
 PQ=I-S,
 \qquad R,S\in\Psi^{-\infty}.
\]
This \(Q\) is a parametrix. The construction is possible because the object simultaneously admits the nonpolynomial reciprocal \(p_m^{-1}\), records position dependence, and has a composition law fine enough to remove every finite-order error. Those are exactly the features missing from differential operators and constant-coefficient multipliers.

The regularity part of the motivating problem then becomes transparent. If \(u\) is a distribution and \(Pu\) is locally smooth, the localized identity
\[
 u=Q(Pu)+Ru
\]
shows that \(u\) is locally smooth, because pseudodifferential operators preserve smoothness and \(R\) is smoothing. More quantitatively, since an order \(-m\) operator maps \(H^s_{\mathrm{loc}}\) to \(H^{s+m}_{\mathrm{loc}}\),
\[
 Pu\in H^s_{\mathrm{loc}}\quad\Longrightarrow\quad u\in H^{s+m}_{\mathrm{loc}}
\]
for elliptic \(P\), with the usual localized estimate. Thus the calculus does not merely assert elliptic regularity; it manufactures the approximate inverse that recovers the missing derivatives. Exact inversion may still fail because of kernels, cokernels, boundary conditions, or global geometry, but these obstructions are separated from the local high-frequency difficulty: modulo smoothing terms, ellipticity is invertibility of the principal symbol on nonzero cotangent directions. This cotangent-space viewpoint is the deeper structural reformulation introduced by the object.

## 3. Notes

A pseudodifferential operator is not the same object as its symbol: quantization conventions can change lower-order terms, while the principal symbol is invariant in the appropriate quotient. A parametrix is a particular pseudodifferential operator attached to an elliptic operator, not a synonym for the whole class. Not every pseudodifferential operator is elliptic. The standard interior calculus described here also does not by itself encode boundary conditions; elliptic boundary problems require additional boundary calculi.

## 4. Sources

[1] J. J. Kohn and L. Nirenberg, “An Algebra of Pseudo-Differential Operators,” *Communications on Pure and Applied Mathematics* 18 (1965), 269–305.

[2] Lars Hörmander, *The Analysis of Linear Partial Differential Operators III: Pseudo-Differential Operators*, Springer, 1985.

[3] Michael E. Taylor, *Pseudodifferential Operators*, Princeton University Press, 1981.
