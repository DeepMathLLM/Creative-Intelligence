# Mathematical Object Origin Archive | Dirichlet Green Function for the Laplacian

## 1. Archive Information

- Standard Name: Dirichlet Green function for the Laplacian
- Mathematical Field: Partial Differential Equations; Potential Theory
- Abstract: The Dirichlet Green function is a domain-dependent two-point kernel that represents the response of the Laplacian to a unit point source while already satisfying homogeneous Dirichlet boundary conditions. It was formed to address the electrostatic and potential-theoretic problem of recovering a potential from interior sources and prescribed boundary values: the free-space point-source potential handled the source but not the boundary, whereas a harmonic correction made the point-source response compatible with the boundary. Superposition and Green's identity then convert the original boundary-value problem into explicit volume and boundary integrals.

## 2. Core Record

### Precise Description

Let \(\Omega\subset\mathbb{R}^n\) be a bounded domain with boundary regular enough for the classical statements below. The Dirichlet Green function for \(-\Delta\) is a function
\[
G_\Omega:(\Omega\times\Omega)\setminus\{(x,x):x\in\Omega\}\longrightarrow\mathbb{R}
\]
such that, for every fixed \(x\in\Omega\),
\[
-\Delta_yG_\Omega(x,y)=\delta_x(y)\quad\text{in }\mathcal D'(\Omega),
\qquad G_\Omega(x,y)=0\quad\text{for }y\in\partial\Omega.
\]
Away from \(y=x\), it is harmonic in \(y\), and it has the same singularity at \(x\) as the free-space fundamental solution \(\Phi(x-y)\) of \(-\Delta\). Equivalently, when the relevant Dirichlet problem is solvable,
\[
G_\Omega(x,y)=\Phi(x-y)-h_x(y),
\]
where \(h_x\) is harmonic in \(\Omega\) and has boundary values \(h_x(y)=\Phi(x-y)\) on \(\partial\Omega\). Thus the subtraction preserves the point-source singularity but cancels its boundary trace [2]. Under standard regularity assumptions the kernel is symmetric, \(G_\Omega(x,y)=G_\Omega(y,x)\), and positive for \(-\Delta\).

If \(u\) solves
\[
-\Delta u=f\quad\text{in }\Omega,\qquad u=g\quad\text{on }\partial\Omega,
\]
then Green's identity gives, for sufficiently regular data and boundary,
\[
u(x)=\int_\Omega G_\Omega(x,y)f(y)\,dy
      -\int_{\partial\Omega}g(y)\,\partial_{\nu_y}G_\Omega(x,y)\,dS_y.
\]
The boundary kernel \(P_\Omega(x,y)=-\partial_{\nu_y}G_\Omega(x,y)\) is the associated Poisson kernel. These formulas also admit weak or distributional versions, but the necessary hypotheses depend on the domain and function spaces.

### Mathematical Context and Formation

The motivating problem class was the determination of a potential inside a bounded region from an interior charge distribution and prescribed values of the potential on the enclosing surface. In modern notation this is the Poisson--Dirichlet problem above; the source-free case is the Dirichlet problem for Laplace's equation. It is the mathematical form of an electrostatic question treated in Green's 1828 essay: relate charge, potential, and boundary data by identities derived from the divergence theorem [1].

Two ingredients available in free space did not by themselves solve the bounded-domain problem. First, the fundamental solution \(\Phi(x-y)\) gives the potential created by a point source, and integrating it against \(f(y)\) gives a particular solution of \(-\Delta u=f\). But this Newtonian or logarithmic potential is insensitive to the shape of \(\partial\Omega\) and generally has the wrong boundary values. Second, Green's identity relates interior Laplacians to boundary values and normal derivatives, but using a generic comparison function leaves boundary terms involving unknown data such as \(\partial_\nu u\). Consequently it is not yet a formula determined solely by the prescribed source \(f\) and Dirichlet data \(g\).

The forming insight was to tailor the point-source potential to the domain before superposing sources. For each pole \(x\), one subtracts from \(\Phi(x-\cdot)\) the harmonic function with the same boundary trace. The resulting kernel retains exactly the singularity required to extract \(u(x)\) in Green's identity, while vanishing on the boundary. This particular pairing of a universal singular part with a geometry-dependent harmonic correction is the Dirichlet Green function. Green's original treatment predates the Dirac delta and modern distribution theory, so the equation \(-\Delta G=\delta\) is a later precise formulation of the point-pole construction rather than Green's own notation [1][3].

### Essential Role

The object makes tractable the simultaneous presence of an arbitrary interior source and a fixed boundary geometry. Its delta singularity is normalized so that Green's identity selects the single value \(u(x)\); its zero boundary trace eliminates the term containing the unknown normal derivative \(\partial_\nu u\); and its remaining normal derivative depends only on \(\Omega\), thereby converting the prescribed boundary value \(g\) into the boundary integral shown above. For homogeneous boundary data, the inverse of the Dirichlet Laplacian is represented directly by
\[
(-\Delta_D)^{-1}f(x)=\int_\Omega G_\Omega(x,y)f(y)\,dy
\]
whenever this classical inverse and integral representation are defined.

Thus the central obstacle was not merely solving a linear equation with a source: it was reconciling the universal point-source solution with a particular boundary. The harmonic correction absorbs that geometric constraint once and for all. Thereafter linear superposition handles every admissible \(f\), while \(-\partial_\nu G\) handles every admissible Dirichlet datum \(g\). The construction also reformulates the boundary-value problem structurally: the solution operator is a two-point kernel, decomposed into a universal local singularity and a regular part carrying global information about the domain. This is its direct contribution to the motivating problem, distinct from later uses of Green functions in spectral theory, parabolic equations, quantum theory, and other settings.

## 3. Notes

- A free-space fundamental solution depends only on \(x-y\) and has no boundary condition; a Dirichlet Green function depends on the domain and incorporates its boundary condition. They are therefore related but not synonymous.
- “Green function” is also used for kernels associated with other operators and with Neumann, Robin, initial, or radiation conditions. This archive concerns only the Dirichlet Green function for the Laplacian.
- The Poisson kernel is derived from this Green function by an outward normal derivative at the boundary; it is not the archived object itself.
- Existence and boundary regularity are not automatic for every domain in every classical sense. The definition and representation should be interpreted in the appropriate classical, weak, or potential-theoretic framework.

## 4. Sources

[1] George Green, *An Essay on the Application of Mathematical Analysis to the Theories of Electricity and Magnetism*, Nottingham: T. Wheelhouse, 1828.

[2] Lawrence C. Evans, *Partial Differential Equations*, 2nd ed., Graduate Studies in Mathematics 19, American Mathematical Society, 2010, Chapter 2, section on Green's functions for Laplace's equation.

[3] I. Stakgold and M. Holst, *Green's Functions and Boundary Value Problems*, 3rd ed., Pure and Applied Mathematics 99, Wiley, 2011, Chapters 1--2.
