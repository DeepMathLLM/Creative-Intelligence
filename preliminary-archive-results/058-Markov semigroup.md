# Mathematical Object Origin Archive | Markov semigroup

## 1. Archive Information

- Standard Name: Markov semigroup
- Mathematical Field: Probability Theory and Stochastic Processes
- Abstract: A Markov semigroup is a time-indexed family of probability-transition operators whose composition law expresses memoryless, time-homogeneous stochastic evolution. It formed as the natural object for the problem of propagating transition probabilities consistently over arbitrary time intervals and, under regularity assumptions, for converting that probabilistic evolution into an evolution equation governed by an infinitesimal generator.

## 2. Core Record

### Precise Description

Let \((E,\mathcal E)\) be a measurable state space and let the time parameter set be \(T=\mathbb N_0\) or \(T=[0,\infty)\). A Markov semigroup may be specified by Markov kernels \((p_t)_{t\in T}\), where \(p_t(x,\cdot)\) is a probability measure for every \(x\in E\), \(x\mapsto p_t(x,A)\) is measurable for every \(A\in\mathcal E\), and
\[
p_0(x,A)=\mathbf 1_A(x),\qquad
p_{s+t}(x,A)=\int_E p_t(y,A)\,p_s(x,dy).
\]
The second identity is the time-homogeneous Chapman–Kolmogorov equation: evolution through a duration \(s+t\) factors through every possible intermediate state after duration \(s\).

Equivalently, each kernel defines a transition operator
\[
(P_t f)(x)=\int_E f(y)\,p_t(x,dy)
\]
on bounded measurable functions. Then
\[
P_0=I,\qquad P_{s+t}=P_sP_t,
\]
and every \(P_t\) is linear, positivity preserving, satisfies \(P_t\mathbf 1=\mathbf 1\), and is a contraction in the supremum norm. Conversely, such operators are represented by Markov kernels under the usual hypotheses appropriate to the chosen function space; this converse is not automatic for an arbitrary measurable space and arbitrary operator domain.

For a continuous-time process one often imposes strong continuity on a Banach space such as \(C_0(E)\). Its infinitesimal generator is then
\[
Lf=\lim_{t\downarrow0}\frac{P_tf-f}{t}
\]
for those \(f\) for which the limit exists. Strong continuity and the generator belong to an important regular version of the concept, not to the bare definition of a measurable Markov semigroup.

### Mathematical Context and Formation

The motivating problem class is to determine the future law of a time-homogeneous memoryless random evolution—classically including random walks, continuous-time jump systems, and diffusion—when its present state or initial distribution is known. For a state \(x\), the required datum is the transition probability \(p_t(x,A)\) that the state lies in \(A\) after elapsed time \(t\). A single transition law at one duration does not by itself organize all durations, while specifying separate laws for each \(t\) leaves a stringent consistency problem: direct evolution for time \(s+t\) must agree with evolution for time \(s\), followed by evolution for time \(t\), after averaging over the random intermediate state.

The obstacle is therefore not merely to list probability distributions, but to make their dependence on elapsed time compatible with conditional probability. If \(X\) is Markov and time homogeneous, conditioning on \(X_s\) removes dependence on the history before \(s\); integrating over \(X_s=y\) gives
\[
\Pr_x(X_{s+t}\in A)=\int_E \Pr_y(X_t\in A)\,\Pr_x(X_s\in dy).
\]
Thus the required compatibility is exactly composition of kernels. Ordinary deterministic flows had the law \(\phi_{s+t}=\phi_t\circ\phi_s\), but they assign one future state to each present state and cannot represent branching random outcomes. Isolated probability measures do represent uncertainty, but have no operation encoding succession conditional on an intermediate state. The decisive construction is to replace each deterministic state map by a probability kernel and replace ordinary function composition by integration over intermediate states. The resulting family has the semigroup law while retaining total mass and positivity.

This structure appeared concretely in the analysis of transition probabilities for Brownian displacement and other Markov processes: Chapman's composition relation and Kolmogorov's analytical treatment of transition probabilities supplied the compatibility equation from which the modern semigroup formulation is abstracted [1][2]. It is safer to regard “Markov semigroup” as the modern structural packaging of this problem and equation, rather than as a term or definition attributable in its present form to a single founding paper.

A second difficulty arises in continuous time. Even if every \(p_t\) were recorded, solving directly for an uncountable family of finite-time kernels is unwieldy. Under suitable continuity assumptions, the short-time behavior can instead be encoded by \(L\). Formally, \(u(t,x)=P_tf(x)\) then satisfies the backward equation \(\partial_tu=Lu\), while the evolution of probability measures is described by the dual forward equation. The semigroup law is what permits local-in-time data to be propagated coherently to finite times; the relevant analytic qualifications are substantive, because such differentiability and generator descriptions do not hold for every bare Markov semigroup [3].

### Essential Role

The Markov semigroup makes the consistency part of the motivating problem tractable. Its identity element fixes zero-time evolution, and its multiplication law enforces all decompositions of an elapsed interval at once. Starting from an initial probability measure \(\mu\), the future law is
\[
(\mu P_t)(A)=\int_E p_t(x,A)\,\mu(dx),
\]
and \((\mu P_s)P_t=\mu P_{s+t}\). Consequently, no separate compatibility check is needed for every chain of intermediate times: associativity of kernel composition supplies it. Repeated discrete-time evolution becomes \(P_n=P_1^n\); continuous-time evolution becomes a one-parameter semigroup rather than an unrelated collection of transition laws.

The operator form also overcomes a mismatch between probabilistic and analytic methods. Expectations of observables become \(P_tf(x)=\mathbb E_x[f(X_t)]\), so positivity and preservation of constants record the probabilistic constraints, while linearity and composition permit operator-theoretic analysis. When strong continuity is available, the generator compresses the local transition mechanism into an infinitesimal operator, and semigroup theory reconstructs and controls finite-time evolution. This is the direct route by which Kolmogorov-type differential equations and transition probabilities are treated as two descriptions of the same evolution rather than as separate calculations.

The deeper structural viewpoint is that a time-homogeneous Markov process induces a stochastic analogue of a deterministic flow: points evolve not to points but to probability measures, and the semigroup law expresses composition after averaging over the intermediate uncertainty. The object does not, by itself, determine path regularity or every pathwise property; different process realizations may require additional hypotheses. Its essential contribution is the coherent finite-time transition mechanism and its bridge to infinitesimal evolution, not a complete replacement for the underlying stochastic process.

## 3. Notes

A Markov semigroup is distinct from a Markov chain: the chain is a stochastic process (often in discrete time), whereas the semigroup is its family of transition kernels or corresponding operators. Sub-Markov semigroups allow \(P_t\mathbf 1\leq\mathbf 1\), representing loss of mass through killing; the present archive uses the conservative convention \(P_t\mathbf 1=\mathbf 1\). A Feller semigroup is a regular Markov semigroup acting strongly continuously on \(C_0(E)\).

## 4. Sources

[1] S. Chapman, “On the Brownian Displacements and Thermal Diffusion of Grains Suspended in a Non-Uniform Fluid,” *Proceedings of the Royal Society of London, Series A* **119** (1928), 34–54.

[2] A. Kolmogoroff, “Über die analytischen Methoden in der Wahrscheinlichkeitsrechnung,” *Mathematische Annalen* **104** (1931), 415–458. https://doi.org/10.1007/BF01457949

[3] S. N. Ethier and T. G. Kurtz, *Markov Processes: Characterization and Convergence*, Wiley, 1986, Chapters 1 and 4.
