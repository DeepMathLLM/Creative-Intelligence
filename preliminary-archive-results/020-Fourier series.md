# Mathematical Object Origin Archive | Fourier Series

## 1. Archive Information

- Standard Name: Fourier series
- Mathematical Field: Harmonic Analysis; Partial Differential Equations
- Abstract: A Fourier series encodes a periodic function, or a function on a finite interval after a suitable extension, by its coefficients against trigonometric modes. Its systematic formation was tied to the boundary-value problem of predicting temperature in a finite body from an arbitrary initial temperature profile: the modes solve the spatial eigenvalue problem, orthogonality extracts their amplitudes, and the heat equation evolves each amplitude independently.

## 2. Core Record

### Precise Description

Let \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\). For \(f\in L^1(\mathbb T)\), its Fourier coefficients are
\[
\widehat f(n)=\frac{1}{2\pi}\int_{-\pi}^{\pi} f(x)e^{-inx}\,dx,\qquad n\in\mathbb Z,
\]
and its Fourier series is the formal trigonometric expansion
\[
\sum_{n\in\mathbb Z}\widehat f(n)e^{inx}.
\]
Equivalently, for real-valued functions it may be written as a constant term plus sine and cosine terms. The series is an object determined by the coefficient sequence; writing it does not itself assert pointwise convergence to \(f\). For example, when \(f\in L^2(\mathbb T)\), its partial sums converge to \(f\) in \(L^2\), while pointwise convergence requires separate hypotheses and can fail for some integrable functions [2].

The form directly adapted to a rod \(0<x<L\) with zero endpoint temperatures is the Fourier sine series
\[
f(x)\sim \sum_{n=1}^{\infty} b_n\sin\!\left(\frac{n\pi x}{L}\right),
\qquad
b_n=\frac{2}{L}\int_0^L f(x)\sin\!\left(\frac{n\pi x}{L}\right)\,dx.
\]
It is the Fourier series of the odd \(2L\)-periodic extension of \(f\). The functions \(\sin(n\pi x/L)\) are mutually orthogonal eigenfunctions of the Dirichlet operator \(-d^2/dx^2\), with eigenvalues \((n\pi/L)^2\).

### Mathematical Context and Formation

The motivating problem is the one-dimensional initial-boundary-value problem for heat conduction in a homogeneous rod:
\[
\partial_tu=\kappa\partial_{xx}u\quad(0<x<L,\ t>0),\qquad
u(0,t)=u(L,t)=0,
\qquad u(x,0)=f(x).
\]
Here \(f\) is a prescribed initial temperature profile and the endpoint conditions model ends held at a reference temperature. Separation of variables, \(u(x,t)=X(x)T(t)\), reduces the equation to
\[
-X''=\lambda X,\qquad T'=-\kappa\lambda T.
\]
The boundary conditions select the discrete spatial modes \(X_n(x)=\sin(n\pi x/L)\), and each produces a separated solution
\[
e^{-\kappa(n\pi/L)^2t}\sin(n\pi x/L).
\]
This calculation by itself does not solve the stated problem: a single separated mode, or any fixed finite family of them, cannot represent a general initial profile \(f\). The exact obstruction is therefore not finding special solutions but reconciling the two-point boundary conditions and time evolution with arbitrary initial data.

Linearity suggests superposing all admissible modes. The decisive structural step is to treat a broad class of profiles as trigonometric expansions and to determine amplitudes by orthogonality. Multiplying
\(f(x)\sim\sum b_n\sin(n\pi x/L)\) by the \(m\)-th sine and integrating annihilates every other mode, giving the coefficient formula above. Fourier's heat theory made this passage from individual trigonometric solutions to expansions of general temperature data systematic; trigonometric series had precursors, so the claim is not that every ingredient originated there, but that the Fourier series in its modern problem-solving role was formed through this heat-conduction problem [1]. Later convergence theory supplied the distinctions among formal expansion, pointwise recovery, and norm convergence that a rigorous modern definition requires [2].

### Essential Role

The Fourier series makes the arbitrary-data step tractable. Substituting the sine coefficients of \(f\) gives
\[
u(x,t)=\sum_{n=1}^{\infty}b_n e^{-\kappa(n\pi/L)^2t}
\sin\!\left(\frac{n\pi x}{L}\right).
\]
For suitable classical data this is a classical solution; for \(f\in L^2(0,L)\), it defines the standard \(L^2\)-solution, attains the initial datum in \(L^2\) as \(t\downarrow0\), and is smooth for \(t>0\) [2][3]. Thus the coefficient formula solves the representation problem at \(t=0\), while the eigenvalue-dependent exponential factors solve the evolution problem for every mode.

Specific features of the object address specific obstacles. Orthogonality turns the recovery of infinitely many unknown amplitudes into independent integral formulas. Completeness in \(L^2(0,L)\) allows the expansion to accommodate arbitrary square-integrable profiles rather than only finite trigonometric combinations. The eigenfunction property diagonalizes the spatial second derivative:
\[
-\partial_{xx}\sin(n\pi x/L)=(n\pi/L)^2\sin(n\pi x/L),
\]
so the PDE becomes the uncoupled scalar equations
\(a_n'(t)=-\kappa(n\pi/L)^2a_n(t)\). The exponential damping also suppresses high frequencies more rapidly, explaining within the same representation why heat flow instantly smooths rough initial data for positive time.

Accordingly, the direct contribution of the Fourier series was not merely a convenient notation for periodic functions. It reformulated an arbitrary-profile boundary-value problem as spectral coordinates in which boundary conditions are built into the basis and the differential operator acts diagonally. The remaining analytic issue—what sense of convergence recovers \(f\)—became a precise problem about the series rather than an unresolved obstruction inside the heat equation.

## 3. Notes

A Fourier transform is the continuous-frequency analogue appropriate to noncompact domains and is a distinct object. A Fourier sine series is not a separate target here but the boundary-adapted form of a Fourier series. Different boundary conditions select different trigonometric subfamilies: for example, homogeneous Neumann conditions lead to cosine modes. The archive's formation claim concerns the systematic general expansion central to Fourier's heat theory, not the invention of all trigonometric expansions.

## 4. Sources

[1] Joseph Fourier, *Théorie analytique de la chaleur*, Firmin Didot, 1822, especially the preliminary discourse and chapters on trigonometric expansion and heat in a ring or solid.

[2] Elias M. Stein and Rami Shakarchi, *Fourier Analysis: An Introduction*, Princeton Lectures in Analysis I, Princeton University Press, 2003, Chapters 2–3.

[3] Lawrence C. Evans, *Partial Differential Equations*, 2nd ed., Graduate Studies in Mathematics 19, American Mathematical Society, 2010, Chapter 2.
