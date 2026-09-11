# Mathematical Object Origin Archive | Martingale

## 1. Archive Information

- Standard Name: Martingale
- Mathematical Field: Probability Theory and Stochastic Processes
- Abstract: A martingale is an integrable stochastic process whose conditional expected future value, relative to the information currently available, equals its present value. It was formed to express fairness in sequential random games when stakes and decisions may depend on past outcomes, a setting in which equality of unconditional expectations is too weak.

## 2. Core Record

### Precise Description

Let \((\Omega,\mathcal F,\mathbb P)\) be a probability space, let \(T\) be an ordered time set, and let \((\mathcal F_t)_{t\in T}\) be a filtration, so that \(\mathcal F_s\subseteq\mathcal F_t\) whenever \(s\le t\). A real-valued process \((M_t)_{t\in T}\) is a martingale with respect to \((\mathcal F_t)\) if

1. \(M_t\) is \(\mathcal F_t\)-measurable for every \(t\) (adaptedness);
2. \(\mathbb E|M_t|<\infty\) for every \(t\) (integrability); and
3. for every \(s\le t\),
   \[
   \mathbb E[M_t\mid\mathcal F_s]=M_s\qquad\text{almost surely}.
   \]

In discrete time, the third condition is equivalently
\[
\mathbb E[M_{n+1}-M_n\mid\mathcal F_n]=0
\]
for every \(n\); the full condition then follows from the tower property of conditional expectation. Thus a martingale is not merely a sequence with constant means: it is a process paired with an information flow, and it has zero conditional drift on every history distinguishable at the current time [1,2].

### Mathematical Context and Formation

The motivating problem class is to formulate and analyze a fair sequential game when a participant can alter future actions after observing earlier outcomes. At round \(n\), the available history is represented by \(\mathcal F_{n-1}\); a stake \(H_n\) must be chosen using that history, and the participant may decide when to stop by a stopping time. A useful definition of fairness therefore has to remain meaningful after conditioning on any observed history and has to interact correctly with nonanticipating changes of stake and time of withdrawal. This fair-game problem is the mathematical setting from which martingale language emerged and in which its modern formulation was systematized [1,3].

A static requirement such as \(\mathbb E[M_n]=\mathbb E[M_0]\) at each fixed \(n\) does not solve the problem, because averaging can cancel favorable conditional drift on some histories against unfavorable drift on others. For a concrete illustration, let \(X\) take the values \(1\) and \(-1\) with equal probability, set \(\mathcal F_0\) to be trivial and \(\mathcal F_1=\mathcal F_2=\sigma(X)\), and define
\[
M_0=0,\qquad M_1=X,\qquad M_2=2X.
\]
Every fixed-time mean is zero, yet after time \(1\) the increment is already predictable:
\[
\mathbb E[M_2-M_1\mid\mathcal F_1]=X\ne0.
\]
Indeed, stopping at time \(2\) when \(X=1\) and at time \(1\) when \(X=-1\) gives expected stopped value \(1/2\), rather than \(0\). Constant unconditional means therefore fail to encode fairness against history-dependent continuation.

The decisive formation step is to represent growing information by a filtration and replace unconditional balance by balance conditional on that information. Requiring
\(\mathbb E[M_{n+1}\mid\mathcal F_n]=M_n\) tests fairness separately on every event in the observed past, rather than only after those events have been averaged together. The resulting object—the adapted process satisfying this conditional invariance—is the martingale [1,2].

### Essential Role

The martingale condition makes the adaptive part of the fair-game problem tractable. For every \(A\in\mathcal F_s\),
\[
\mathbb E\!\left[(M_t-M_s)\mathbf 1_A\right]=0.
\]
Consequently, selecting an action according to information available at time \(s\) cannot isolate a past-measurable class of histories with positive expected future increment while preserving admissibility. This is exactly what the unconditional equality of means could not guarantee.

More concretely, let \(K_0\) be an integrable, \(\mathcal F_0\)-measurable initial capital. Suppose the net return per unit stake in round \(n\), denoted \(Y_n\), is integrable and \(\mathcal F_n\)-measurable, and satisfies
\[
\mathbb E[Y_n\mid\mathcal F_{n-1}]=0.
\]
Let the stake \(H_n\) be \(\mathcal F_{n-1}\)-measurable and assume that every product \(H_nY_n\) is integrable. Then the capital
\[
K_n=K_0+\sum_{k=1}^{n}H_kY_k
\]
is adapted and integrable, and it is a martingale because
\[
\mathbb E[H_nY_n\mid\mathcal F_{n-1}]
=H_n\mathbb E[Y_n\mid\mathcal F_{n-1}]=0.
\]
Thus the definition absorbs arbitrary admissible nonanticipating stake selection into one structural calculation instead of requiring a separate analysis of every strategy. Likewise, for a discrete-time martingale and any bounded stopping time \(\tau\), optional sampling gives
\[
\mathbb E[M_\tau]=\mathbb E[M_0],
\]
so choosing a bounded withdrawal time from observed history does not create expected gain [2].

These consequences identify the martingale's direct contribution: it reformulates “fair after every possible past” as a conditional-expectation invariant and thereby controls predictable betting and bounded adaptive stopping. The deeper structural viewpoint is that fairness is relative to information; it belongs to the pair \((M,(\mathcal F_t))\), not merely to the one-time distributions of \(M_t\). This turns a collection of strategy-specific gambling calculations into the study of an invariant under the revelation of information.

## 3. Notes

A martingale in probability theory is distinct from the historically named “martingale” doubling betting system. Submartingales and supermartingales replace the defining equality by the corresponding conditional inequalities and model nonnegative or nonpositive conditional drift. Optional-stopping conclusions require hypotheses: bounded stopping times give the finite discrete-time statement used above, whereas unbounded stopping and unbounded stakes may require uniform integrability, bounded increments, or other conditions. The definition alone does not validate unrestricted doubling strategies.

## 4. Sources

[1] J. L. Doob, *Stochastic Processes*, John Wiley & Sons, 1953, especially Chapter VII.

[2] David Williams, *Probability with Martingales*, Cambridge University Press, 1991, Chapters 10–12.

[3] Jean Ville, *Étude critique de la notion de collectif*, Gauthier-Villars, 1939.
