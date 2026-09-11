# Mathematical Object Origin Archive | Bakry–Émery curvature-dimension condition

## 1. Archive Information

- Standard Name: Bakry–Émery curvature-dimension condition
- Mathematical Field: Probability Theory and Stochastic Processes; geometric analysis
- Abstract: The Bakry–Émery curvature-dimension condition, denoted \(CD(\rho,N)\), is a pointwise inequality for the first and second carré du champ forms of a diffusion generator. It arose as a locally checkable criterion for the concrete problem of proving hypercontractivity of Markov diffusion semigroups, replacing a difficult global operator-norm question by an infinitesimal inequality that abstracts the curvature and dimension terms in the Bochner formula.

## 2. Core Record

### Precise Description

Let \(L\) be the generator of a Markov diffusion semigroup \((P_t)_{t\ge 0}\), acting on a suitable algebra \(\mathcal A\) of test functions and satisfying the diffusion chain rule. Its carré du champ is
\[
\Gamma(f,g)=\frac12\bigl(L(fg)-fLg-gLf\bigr),
\qquad \Gamma(f)=\Gamma(f,f),
\]
and its iterated carré du champ is
\[
\Gamma_2(f,g)=\frac12\bigl(L\Gamma(f,g)-\Gamma(f,Lg)-\Gamma(g,Lf)\bigr),
\qquad \Gamma_2(f)=\Gamma_2(f,f).
\]
For \(\rho\in\mathbb R\) and \(N\in[1,\infty]\), the generator satisfies the Bakry–Émery curvature-dimension condition \(CD(\rho,N)\) when, pointwise for every admissible \(f\),
\[
\Gamma_2(f)\ge \rho\,\Gamma(f)+\frac1N(Lf)^2,
\]
where \(1/\infty=0\). Thus \(CD(\rho,\infty)\) is the \(\Gamma_2\)-criterion \(\Gamma_2\ge \rho\Gamma\) [1,2].

For the Laplace–Beltrami generator \(L=\Delta\) on an \(n\)-dimensional Riemannian manifold,
\[
\Gamma(f)=|\nabla f|^2,
\qquad
\Gamma_2(f)=\|\operatorname{Hess}f\|^2+\operatorname{Ric}(\nabla f,\nabla f).
\]
Consequently, the lower Ricci bound \(\operatorname{Ric}\ge \rho g\), together with \(\|\operatorname{Hess}f\|^2\ge (\Delta f)^2/n\), gives \(CD(\rho,n)\). This model explains the two terms in the abstract condition: \(\rho\) acts as a curvature lower bound and \(N\) as an upper dimension parameter [2].

### Mathematical Context and Formation

The motivating problem was to decide when a diffusion Markov semigroup is hypercontractive: given an invariant probability measure \(\mu\) and \(p>1\), one seeks times \(t>0\) and exponents \(q(t)>p\) for which
\[
\|P_t f\|_{L^{q(t)}(\mu)}\le \|f\|_{L^p(\mu)}.
\]
This is a global, nonlinear norm-improvement property. Gross's logarithmic Sobolev theory had related hypercontractivity to a logarithmic Sobolev inequality, but that reformulation still left a global integral inequality to be verified for each diffusion [3]. Direct estimates of transition kernels or of changing \(L^p\)-norms were strongly dependent on the particular process and did not supply a uniform criterion expressed in the generator itself.

Bakry and Émery's formation of the condition used the observation that the generator already contains an algebraic substitute for a squared gradient, namely \(\Gamma\). Differentiating this energy under the semigroup introduces exactly the second-order expression \(\Gamma_2\). On a manifold, the Bochner identity decomposes that expression into a nonnegative Hessian term and a Ricci-curvature term; the trace inequality for the Hessian contributes the dimension-dependent quantity \((Lf)^2/N\). The resulting inequality
\(\Gamma_2\ge \rho\Gamma+(Lf)^2/N\) therefore retains precisely the pieces of the geometric computation needed for semigroup estimates while making no reference to coordinates, a Riemannian metric, or even a finite-dimensional state space. In their work on hypercontractive diffusions, Bakry and Émery identified strong positivity of the iterated carré du champ as the sufficient condition that could be checked locally and then propagated by the semigroup [1].

### Essential Role

The condition made the infinitesimal-to-global step in the hypercontractivity problem tractable. For example, under \(CD(\rho,\infty)\), apply the condition to the interpolation
\[
\Phi(s)=P_s\!\left(\Gamma(P_{t-s}f)\right),\qquad 0\le s\le t.
\]
A direct differentiation gives
\[
\Phi'(s)=2P_s\!\left(\Gamma_2(P_{t-s}f)\right)
\ge 2\rho\,\Phi(s).
\]
Integration yields the gradient estimate
\[
\Gamma(P_t f)\le e^{-2\rho t}P_t\Gamma(f).
\]
Thus the particular form of \(\Gamma_2\)—the derivative of carré-du-champ energy along the semigroup—and its lower bound by \(\Gamma\) produce a closed differential inequality to which Grönwall's lemma applies. With an invariant probability measure and the usual symmetry, ergodicity, domain, and regularity assumptions, the same semigroup interpolation and diffusion chain rule give, for \(\rho>0\),
\[
\operatorname{Ent}_\mu(f^2)
\le \frac{2}{\rho}\int \Gamma(f)\,d\mu,
\]
and hence the desired hypercontractivity through the logarithmic Sobolev equivalence [1,3].

This was the direct contribution: a global \(L^p\)-to-\(L^q\) property could be proved from a pointwise inequality involving only \(L\) and its first two carré du champ forms. The curvature term supplies exponential control, while the finite-\(N\) term records the extra coercivity coming from dimension and permits dimension-sensitive refinements. Conceptually, the condition also showed that the analytic content of a Ricci lower bound can be encoded at the level of a Markov generator, allowing the hypercontractivity argument to survive beyond the original Riemannian examples [1,2].

## 3. Notes

The condition is a property of a diffusion generator, not the same object as the Bakry–Émery Ricci tensor on a weighted manifold. For a weighted Laplacian, that tensor appears in the Bochner formula and can be used to verify the generator condition. The notation \(CD(\rho,N)\) here refers to the carré-du-champ formulation; later metric-measure curvature-dimension conditions use related notation but are defined by different structures. Geometric comparison theorems, concentration bounds, and nonsmooth extensions are important later developments, not the motivating role recorded here.

## 4. Sources

[1] Dominique Bakry and Michel Émery, “Diffusions hypercontractives,” *Séminaire de probabilités de Strasbourg* 19, Lecture Notes in Mathematics 1123 (1985), 177–206. https://www.numdam.org/article/SPS_1985__19__177_0.pdf

[2] Dominique Bakry, “The Geometry of Markov Diffusion Generators,” *Annales de la Faculté des sciences de Toulouse: Mathématiques*, Série 6, 9(2) (2000), 305–366. https://www.numdam.org/item/?id=AFST_2000_6_9_2_305_0

[3] Leonard Gross, “Logarithmic Sobolev Inequalities,” *American Journal of Mathematics* 97(4) (1975), 1061–1083.
