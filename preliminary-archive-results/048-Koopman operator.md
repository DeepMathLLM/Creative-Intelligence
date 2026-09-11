# Mathematical Object Origin Archive | Koopman Operator

## 1. Archive Information

- Standard Name: Koopman operator
- Mathematical Field: Dynamical Systems; Ergodic Theory; Functional Analysis
- Abstract: The Koopman operator represents a measure-preserving transformation or flow by its pullback action on scalar observables. It was formed to recast nonlinear, measure-preserving dynamics—initially Hamiltonian dynamics—as linear unitary evolution on a function space, so that invariant quantities, time averages, correlations, and, in the invertible case, spectral behavior could be studied with Hilbert-space methods.

## 2. Core Record

### Precise Description

Let \((X,\Sigma,\mu)\) be a probability space and let \(T:X\to X\) be a measurable, measure-preserving transformation. The **Koopman operator** associated with \(T\) is the composition operator
\[
U_T:L^2(X,\mu)\longrightarrow L^2(X,\mu),\qquad (U_Tf)(x)=f(Tx).
\]
Measure preservation, \(\mu(T^{-1}A)=\mu(A)\), ensures that composition is well-defined on equivalence classes modulo null sets and gives
\[
\|U_Tf\|_2^2=\int_X |f\circ T|^2\,d\mu=\int_X|f|^2\,d\mu.
\]
Thus \(U_T\) is a linear isometry. If \(T\) is invertible modulo null sets with a measure-preserving inverse, then \(U_T\) is unitary and \(U_T^{-1}=U_{T^{-1}}\). Iteration is represented exactly: \(U_T^n f=f\circ T^n\).

For a measure-preserving flow \((\Phi^t)_{t\in\mathbb R}\), the corresponding family
\[
U^t f=f\circ\Phi^t
\]
is a one-parameter group of isometries, and it is unitary when the flow is invertible modulo null sets. Under standard measurable-continuity hypotheses it is strongly continuous on \(L^2\), so it has an infinitesimal generator. In a smooth setting that generator acts formally on suitable observables as the derivative along the vector field of the flow.

The definition is linear in \(f\) even when \(T\) or \(\Phi^t\) is nonlinear on state space. On bounded observables it also retains the identities \(U_T(fg)=(U_Tf)(U_Tg)\), \(U_T\overline f=\overline{U_Tf}\), and \(U_T1=1\); hence it is not an arbitrary linearization but the pullback representation of the original dynamics.

### Mathematical Context and Formation

The motivating problem class was the analysis of long-time behavior in measure-preserving dynamics, especially Hamiltonian systems: how can one characterize invariant quantities, ergodicity, time averages, and the periodic or continuous components visible in correlations without explicitly solving every nonlinear trajectory? A Hamiltonian flow acts naturally on phase-space points, but that point evolution is generally nonlinear. Trajectory equations and geometric phase-space methods describe the state motion, yet by themselves they do not provide a linear normal operator on a fixed Hilbert space to which orthogonality, projection, and spectral decomposition can be applied. Linearizing the state equation near an orbit addresses only local perturbations and does not represent the global dynamics.

The formative insight was to change what is evolved. Instead of asking the flow to act linearly on states, let it act contravariantly on every scalar observable by composition. An invariant measure supplies the fixed inner product
\[
\langle f,g\rangle=\int_X f\overline g\,d\mu,
\]
and measure preservation makes the pullback an isometry; invertibility makes it unitary. The dynamical composition law then becomes the operator group law. Koopman's 1931 formulation associated Hamiltonian systems with unitary transformations in Hilbert space [1], and Koopman and von Neumann's subsequent treatment placed spectral types directly into the study of dynamical systems [2]. Thus the operator was not introduced merely as a later computational device: it answered the structural problem of bringing global, measure-preserving nonlinear evolution within linear Hilbert-space analysis.

### Essential Role

The Koopman operator made the statistical and invariant part of the motivating problem tractable by turning dynamical questions into statements about one linear isometry or, for invertible measure-preserving dynamics, one unitary operator. An observable is invariant exactly when \(U_Tf=f\). On a probability space, ergodicity is therefore equivalent to the fixed subspace of \(U_T\) consisting only of almost-everywhere constant functions. Likewise, the finite-time average of an observable becomes
\[
\frac1N\sum_{n=0}^{N-1} f\circ T^n
 =\frac1N\sum_{n=0}^{N-1}U_T^n f.
\]
The Hilbert-space mean ergodic theorem identifies the \(L^2\)-limit of these averages as the orthogonal projection onto the fixed subspace; in the ergodic case this is the constant \(\int_X f\,d\mu\) [3]. This converts a long-orbit averaging question into a projection theorem.

Correlations are similarly operator matrix coefficients, for example \(\langle U_T^n f,g\rangle\). When \(T\) is invertible modulo null sets, \(U_T\) is unitary, and its eigenfunctions and projection-valued spectral measure organize persistent frequencies and continuous spectral behavior without requiring a global coordinate solution of the nonlinear equations. Linearity permits superposition and Hilbert-space methods; unitarity in the invertible case supports the normal-operator spectral theorem; and the composition identity ensures that operator powers represent the exact—not locally approximated—dynamics. For a noninvertible measure-preserving transformation, \(U_T\) remains an isometry, but one must not assume that it is normal or that it has a projection-valued spectral measure on the unit circle; spectral treatment then requires the theory of isometries, a unitary dilation, or an appropriate semispectral formulation.

The difficulty was therefore bypassed rather than removed: nonlinear state evolution was lifted to an infinite-dimensional linear action on observables. The multiplicative identities retained by \(U_T\), together with its action on the full observable algebra, preserve information about the underlying map that an arbitrary linear state approximation would discard. This introduced a structural viewpoint in which invariants, averages, and, in the unitary case, spectral components are properties of the pullback representation of the dynamics, while not claiming that diagonalizing a Koopman operator automatically yields explicit trajectories.

## 3. Notes

Some authors use the opposite time convention \(f\mapsto f\circ T^{-1}\) when \(T\) is invertible. The Koopman operator acts on observables and should be distinguished from the Perron–Frobenius or transfer operator, which acts on densities or measures and is dual to the Koopman action under an appropriate pairing. For non-measure-preserving maps, composition operators can still be defined on suitable function spaces, but isometry and unitarity no longer follow from the basic construction.

## 4. Sources

[1] B. O. Koopman, “Hamiltonian Systems and Transformation in Hilbert Space,” *Proceedings of the National Academy of Sciences* 17 (1931), 315–318, https://doi.org/10.1073/pnas.17.5.315.

[2] B. O. Koopman and J. von Neumann, “Dynamical Systems of Continuous Spectra,” *Proceedings of the National Academy of Sciences* 18 (1932), 255–263, https://doi.org/10.1073/pnas.18.3.255.

[3] Peter Walters, *An Introduction to Ergodic Theory*, Graduate Texts in Mathematics 79, Springer, 1982, especially the chapters on measure-preserving transformations and ergodic theorems.
