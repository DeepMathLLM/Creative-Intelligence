# Mathematical Object Origin Archive | Radon–Nikodym Derivative

## 1. Archive Information

- Standard Name: Radon–Nikodym derivative
- Mathematical Field: Measure Theory; Probability Theory and Stochastic Processes
- Abstract: The Radon–Nikodym derivative is the measurable density that represents one measure by integration against another. It was formed to solve the measure-representation problem of recovering a measure \(\nu\), known to assign no mass to \(\mu\)-null sets, from a pointwise weight relative to \(\mu\).

## 2. Core Record

### Precise Description

Let \((X,\Sigma)\) be a measurable space, and let \(\mu\) and \(\nu\) be \(\sigma\)-finite positive measures on it. If \(\nu\) is absolutely continuous with respect to \(\mu\), written \(\nu\ll\mu\), then the Radon–Nikodym theorem gives a measurable function
\[
f:X\longrightarrow [0,\infty)
\]
that is finite \(\mu\)-almost everywhere and satisfies
\[
\nu(A)=\int_A f\,d\mu\qquad(A\in\Sigma).
\]
This function is unique up to equality \(\mu\)-almost everywhere and is denoted
\[
f=\frac{d\nu}{d\mu}.
\]
Conversely, every nonnegative measurable \(f\) defines an absolutely continuous measure by \(\nu(A)=\int_A f\,d\mu\); when both measures are \(\sigma\)-finite, its derivative may be taken finite \(\mu\)-almost everywhere. The defining identity implies, for every nonnegative measurable \(g\),
\[
\int_X g\,d\nu=\int_X g\frac{d\nu}{d\mu}\,d\mu.
\]
In particular, if \(\mu\) and \(\nu\) are probability measures, then \(d\nu/d\mu\geq 0\) and \(\int_X(d\nu/d\mu)\,d\mu=1\) [1,2].

### Mathematical Context and Formation

The motivating problem is the following representation problem: given two measures on the same measurable space, determine when all values of \(\nu\) can be computed using only integration with respect to \(\mu\), and identify the object carrying the required change of weight. For ordinary functions on an interval, a derivative can express a local rate of change, and an absolutely continuous function can be recovered by integrating that derivative. Measures, however, are set functions. On an abstract measurable space there need be no order, metric, topology, differentiation basis, or canonical family of neighborhoods shrinking to a point on which to form limits of ratios \(\nu(A)/\mu(A)\). Even where such ratios exist for individual sets, they do not by themselves produce a consistent pointwise quantity whose integrals reproduce \(\nu\).

The condition \(\nu\ll\mu\) isolates the indispensable compatibility: if \(\mu(A)=0\), no formula \(\nu(A)=\int_A f\,d\mu\) can give \(\nu(A)>0\). Yet absolute continuity alone is only a relation between null sets; it does not itself provide the representing weight. The decisive reformulation is to define the sought “derivative” not through geometric difference quotients but through its global integral action on every measurable set. Countable additivity points to the Lebesgue integral as the mechanism for assembling a measurable local weight, leading to the requirement
\[
\nu(A)=\int_A f\,d\mu\quad\text{for all }A\in\Sigma.
\]
The Radon–Nikodym theorem proves that, under the stated \(\sigma\)-finiteness hypotheses, the null-set condition is sufficient for such an \(f\) to exist [1,2]. Thus the derivative is formed as an almost-everywhere equivalence class of measurable densities, exactly matching the fact that integration cannot detect changes on \(\mu\)-null sets.

### Essential Role

The Radon–Nikodym derivative makes the representation part of the problem tractable: it replaces the unknown set function \(\nu\) by the measurable function \(d\nu/d\mu\). Its defining identity simultaneously recovers \(\nu(A)\) for every measurable \(A\), rather than assigning unrelated ratios to separate sets. The construction bypasses the absence of canonical local geometric or differentiation structure—such as a topology, metric, differentiation basis, or distinguished shrinking neighborhoods—because it is characterized entirely by measurable sets and integration. Its almost-everywhere uniqueness removes precisely the ambiguity that the reference measure cannot observe.

More structurally, the derivative turns absolute continuity from a qualitative statement—\(\nu\) has no mass outside what \(\mu\) can see—into a quantitative classification: absolutely continuous measures correspond to nonnegative measurable weights (subject to the relevant finiteness conditions). The change-of-measure formula
\[
\int g\,d\nu=\int g\frac{d\nu}{d\mu}\,d\mu
\]
then resolves the associated integration problem as well as the setwise representation problem. In probability, this same feature gives the likelihood ratio between absolutely continuous laws, but that is an instance of the original measure-representation mechanism rather than a separate reason for the object's formation.

## 3. Notes

The Radon–Nikodym derivative is not generally a pointwise limit of ratios of measures; differentiation-basis theorems can provide such formulas only when additional geometric structure is available. It is also distinct from the derivative of a cumulative distribution function, which depends on an ordered domain. For signed or complex measures, corresponding versions represent the measure by an integrable signed or complex density under the standard hypotheses. The Lebesgue decomposition theorem complements the object by separating a measure into an absolutely continuous part, which has a Radon–Nikodym derivative, and a singular part, which cannot be represented by a density relative to the reference measure.

## 4. Sources

[1] Gerald B. Folland, *Real Analysis: Modern Techniques and Their Applications*, 2nd ed., Wiley, 1999, Chapter 3 (Lebesgue–Radon–Nikodym theorem).

[2] Vladimir I. Bogachev, *Measure Theory*, Vol. I, Springer, 2007 (Radon–Nikodym theorem and densities of measures).
