# Mathematical Object Origin Archive | Stopping Time

## 1. Archive Information

- Standard Name: Stopping time (relative to a filtration)
- Mathematical Field: Probability Theory and Stochastic Processes
- Abstract: A stopping time is a random time whose occurrence can be recognized from the information available up to that time. It formalizes admissible observation-based stopping rules and makes martingale arguments at random horizons possible without permitting anticipation of future data.

## 2. Core Record

### Precise Description

Let \((\Omega,\mathcal F,\mathbb P)\) be a probability space and \((\mathcal F_t)_{t\in T}\) a filtration, where \(T=\mathbb N_0\) in discrete time or \(T=[0,\infty)\) in continuous time. A map
\[
\tau:\Omega\longrightarrow T\cup\{\infty\}
\]
is a **stopping time** relative to \((\mathcal F_t)\) if
\[
\{\tau\le t\}\in\mathcal F_t\qquad\text{for every }t\in T.
\]
Thus, by time \(t\), the available information suffices to decide whether stopping has already occurred; the definition does not require knowledge of outcomes after \(t\). In discrete time the condition is equivalently \(\{\tau=n\}\in\mathcal F_n\) for every \(n\). Standard examples include a deterministic time and the first entrance time
\[
\tau_A=\inf\{t\ge 0:X_t\in A\},
\]
when the process and state set satisfy the measurability or regularity hypotheses needed to make these events measurable. In continuous time, an adapted continuous process has a stopping-time first entrance into a closed set; more general hitting-time statements require additional hypotheses [2].

### Mathematical Context and Formation

The formative problem class is **sequential stopping under partial information**. For example, suppose \((M_n,\mathcal F_n)\) models a fair game and a player stops when the observed fortune first reaches a target or loss boundary. One wants to compare the expected stopped fortune \(M_\tau\) with the initial fortune, or to estimate the probability of reaching one boundary before another. The choice of \(\tau\) is random and depends on the sample path, whereas the defining martingale identity
\[
\mathbb E[M_{n+1}\mid\mathcal F_n]=M_n
\]
controls one deterministic step at a time [1].

An arbitrary random index is inadequate for this problem because it may encode future information. For instance, choosing between two times after inspecting both corresponding outcomes can systematically select a favorable value even from a fair process. Consequently, the deterministic-time equality \(\mathbb E[M_n]=\mathbb E[M_0]\) cannot simply be transferred to \(M_\tau\). On the other hand, requiring \(\tau\) to be deterministic would exclude precisely the first-passage and boundary-exit rules that motivate sequential stopping.

The decisive structural idea is therefore to express “no foresight” as an information condition rather than as a fixed-time condition: for every \(t\), the event that the rule has acted by \(t\) must belong to \(\mathcal F_t\). This measurability condition separates observation-based rules from anticipative random times while retaining path-dependent rules such as first exits. It turns the informal notion of a permissible random horizon into the stopping-time object [1,2].

### Essential Role

The stopping-time condition makes the random-horizon part of the problem tractable because the indicator of stopping at a discrete time \(k\), \(\mathbf 1_{\{\tau=k\}}\), is \(\mathcal F_k\)-measurable. Decisions to retain or discard subsequent martingale increments can therefore be conditioned on information already available when the decision is made. Concretely, if \(M\) is a discrete-time martingale and \(\tau\) is a stopping time, then
\[
M^{\tau}_n:=M_{n\wedge\tau}
\]
is again a martingale. The original random-horizon question can first be treated at the bounded horizon \(n\wedge\tau\), where ordinary martingale conditioning applies [1].

This mechanism yields optional-sampling results: under standard sufficient hypotheses—such as bounded \(\tau\), or appropriate uniform-integrability and convergence conditions—one may pass from the stopped process to identities such as
\[
\mathbb E[M_\tau]=\mathbb E[M_0].
\]
The stopping-time property alone does **not** guarantee this equality for an unbounded \(\tau\); integrability or limiting failures remain possible. Its exact contribution is instead to remove anticipation and preserve adapted martingale structure, isolating the remaining issue as one of integrability and passage to a limit. This reformulation also makes first-passage questions accessible through stopped martingales: boundary information can be inserted into \(M_\tau\), and martingale identities or inequalities can then determine hitting probabilities and expected exit behavior. The deeper structural viewpoint is that a random time is mathematically admissible not because its numerical value is controlled in advance, but because its occurrence is synchronized with the filtration representing available information.

## 3. Notes

A stopping time is stronger than an arbitrary random time. It is also distinct from notions such as an honest time or last-exit time, which may depend on future path information. In continuous time, whether a hitting or entrance time is a stopping time can depend on path regularity, the target set, and regularity of the filtration; blanket claims for arbitrary adapted processes and sets are therefore invalid. Optional-stopping conclusions always require hypotheses beyond the stopping-time definition.

## 4. Sources

[1] David Williams, *Probability with Martingales*, Cambridge University Press, 1991.

[2] Daniel Revuz and Marc Yor, *Continuous Martingales and Brownian Motion*, 3rd ed., Springer, 1999.
