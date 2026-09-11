# Mathematical Object Origin Archive | H-measure

## 1. Archive Information

- Standard Name: H-measure (also called a microlocal defect measure)
- Mathematical Field: Partial Differential Equations; Functional Analysis; Homogenization
- Abstract: An H-measure is a positive matrix-valued Radon measure attached, after extraction of a subsequence, to an $L^2$-bounded sequence converging weakly to zero. It records where quadratic mass lost under weak convergence is located in physical space and in which asymptotic Fourier directions it oscillates or concentrates. The object was formed to make weak limits of quadratic expressions tractable in PDE-constrained sequences, notably the second-order correlations required in small-amplitude homogenization [1,2].

## 2. Core Record

### Precise Description

Let $\Omega\subset\mathbb R^d$ be open and let $u_n=(u_n^1,\ldots,u_n^m)$ be bounded in $L^2_{\mathrm{loc}}(\Omega;\mathbb C^m)$ with $u_n\rightharpoonup0$ weakly. After passing to a subsequence, there is an $m\times m$ Hermitian positive-semidefinite matrix $\mu=(\mu^{ij})$ of complex Radon measures on $\Omega\times S^{d-1}$ such that, for $\varphi_1,\varphi_2\in C_c(\Omega)$ and $\psi\in C(S^{d-1})$,

$$
\lim_{n\to\infty}\int_{\mathbb R^d}
 \widehat{\varphi_1u_n^i}(\xi)\,
 \overline{\widehat{\varphi_2u_n^j}(\xi)}\,
 \psi\!\left(\frac{\xi}{|\xi|}\right)\,d\xi
=
\int_{\Omega\times S^{d-1}}
 \varphi_1(x)\overline{\varphi_2(x)}\psi(\theta)
 \,d\mu^{ij}(x,\theta).
$$

Here the localized functions are extended by zero outside $\Omega$; the value of the multiplier at $\xi=0$ is immaterial. Positivity means that $\sum_{i,j}z_i\overline{z_j}\mu^{ij}$ is a nonnegative measure for every $z\in\mathbb C^m$. For a sequence with weak limit $u$, the H-measure is applied to $u_n-u$. It is generally subsequence-dependent.

The variables have distinct meanings: $x$ gives spatial location, while $\theta=\xi/|\xi|$ gives a direction at frequencies escaping to infinity. Thus the object deliberately forgets frequency magnitude and does not identify a characteristic length scale. Its total spatial marginal represents the local quadratic defect: with the Fourier normalization absorbed consistently into the definition, testing with $\psi=1$ recovers the weak limit of localized products $u_n^i\overline{u_n^j}$ beyond the product of their weak limits. In particular, $\mu=0$ is equivalent to $u_n\to0$ strongly in $L^2_{\mathrm{loc}}$ along the selected subsequence [1,2].

### Mathematical Context and Formation

The motivating problem class is to determine quadratic limits of weakly convergent fields that satisfy differential constraints. A representative instance occurs in small-amplitude homogenization. If an elliptic coefficient has the form $A_n=A_0+\eta B_n$ with rapidly varying $B_n\rightharpoonup B$ and small contrast $|\eta|\ll1$, the first-order term in an effective-coefficient or state expansion is controlled by weak limits, but the second-order term contains correlations between $B_n$ and corrector gradients. Both factors may converge only weakly, so their product is not determined by their weak limits. This second-order information is exactly what is needed to distinguish microstructures having the same volume fraction or macroscopic weak limit [1,4].

The elementary obstruction is already visible in $u_n(x)=a(x)e^{in k\cdot x}$: although $u_n\rightharpoonup0$, one has $|u_n|^2=|a|^2$. Ordinary weak convergence therefore erases the quadratic quantity. A spatial defect measure obtained from $|u_n|^2dx$ retains where the missing norm lies but not the direction $k/|k|$. That directional loss is decisive for PDE: a differential operator acts at high frequency through its principal symbol $p(x,\xi)$, and the admissible oscillations depend on the direction of $\xi$. Value-distribution descriptions such as ordinary Young measures likewise do not, by themselves, encode this coupling between spatial position, Fourier direction, and the symbol of the differential constraint. Hence neither the weak limit nor an undirected spatial energy defect supplied enough data for the relevant quadratic limits.

The forming insight was to probe the sequence simultaneously by multiplication in $x$ and by order-zero Fourier multipliers whose symbols depend only on $\xi/|\xi|$. For localized quadratic forms

$$
\bigl(\psi(D/|D|)(\varphi_1u_n^i),\,\varphi_2u_n^j\bigr)_{L^2},
$$

$L^2$ boundedness gives subsequential limits. The compactness of the commutator between such a multiplier and multiplication by a compactly supported function makes those limits depend, modulo compact errors invisible to a weakly null sequence, on a function of $(x,\theta)$. Positivity then turns the limiting functional into a Radon measure on $\Omega\times S^{d-1}$. Tartar introduced this construction as H-measures in connection with small-amplitude homogenization and propagation, while Gérard independently developed the equivalent microlocal-defect-measure formulation [1–3]. The measure is therefore not an arbitrary enlargement of weak convergence: its base variable, directional covariable, positivity, and quadratic character are precisely the pieces missing from the motivating limit problem.

### Essential Role

The H-measure makes the undetermined quadratic part of weak convergence explicit. If $A$ is an order-zero pseudodifferential operator with principal symbol $a_0(x,\theta)$, then, schematically and with component contractions understood,

$$
\lim_{n\to\infty}(Au_n,u_n)
=
\int_{\Omega\times S^{d-1}}a_0(x,\theta)\,d\mu(x,\theta).
$$

Thus a product that weak convergence alone cannot evaluate is replaced by a linear pairing against $\mu$. In small-amplitude homogenization this converts the second-order coefficient/corrector correlations into directional moments of the H-measure of the microstructure; effective tensors through quadratic order can consequently be described without assuming periodicity or resolving every microscopic scale [1,4]. This is the direct tractability gained: the missing second-order data become a compact measure-valued parameter rather than an uncontrolled product of two weak sequences.

Differential constraints become equally concrete through the localization principle. If a differential operator $P(x,D)$ of order $r$, with principal symbol $p_r(x,\xi)$, satisfies an appropriate strong compactness condition such as $P(x,D)u_n\to0$ in $H^{-r}_{\mathrm{loc}}$, then

$$
p_r(x,\theta)\,\mu(x,\theta)=0
$$

in the matrix-measure sense. Hence $\mu$ can live only in symbol directions and polarizations allowed by the PDE—for a scalar equation, on the characteristic set where $p_r(x,\theta)=0$. The direction variable in the definition is what permits this conclusion; an ordinary spatial defect measure could not be tested against the principal symbol. Quadratic forms that vanish, or have a sign, on the corresponding wave cone then inherit convergence or lower-semicontinuity properties, recasting compensated compactness as a support-and-polarization statement about the defect [1,3].

The deeper structural viewpoint is that failure of strong $L^2$ compactness is not merely an amount of missing norm. It has geometry in phase space, constrained by the PDE. H-measures separate the macroscopic weak limit from this directional quadratic defect and allow the principal symbol to act directly on the latter. Their role is limited but exact: they capture quadratic, high-frequency directional information, not the absolute oscillation scale and not arbitrary higher-order correlations.

## 3. Notes

“H-measure” and “microlocal defect measure” denote equivalent foundational constructions due independently to Tartar and Gérard; conventions for Fourier transforms, symbol classes, and whether the sphere or cosphere bundle is used vary. An H-measure is distinct from a semiclassical measure, which is tied to a prescribed small scale, and from a Young measure, which primarily records value-space oscillation statistics. Generalized or one-scale variants are required when frequency magnitude, a selected scale, or more general integrability must also be retained.

## 4. Sources

[1] Luc Tartar, “H-measures, a new approach for studying homogenisation, oscillations and concentration effects in partial differential equations,” *Proceedings of the Royal Society of Edinburgh, Section A* 115 (1990), no. 3–4, 193–230. https://doi.org/10.1017/S0308210500020606

[2] Patrick Gérard, “Microlocal defect measures,” *Communications in Partial Differential Equations* 16 (1991), no. 11, 1761–1794. https://doi.org/10.1080/03605309108820822

[3] Gilles A. Francfort, “An Introduction to H-measures and Their Applications,” lecture notes, 2006. http://www.gillesfrancfort.com/assets/files/H-measures%20copy.pdf

[4] Grégoire Allaire and Sergio Gutiérrez, “Optimal design in small amplitude homogenization,” *ESAIM: Mathematical Modelling and Numerical Analysis* 41 (2007), no. 3, 543–574. https://doi.org/10.1051/m2an:2007026
