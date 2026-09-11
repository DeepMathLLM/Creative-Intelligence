# Mathematical Object Origin Archive | Jones polynomial

## 1. Archive Information

- Standard Name: Jones polynomial
- Mathematical Field: Knot Theory and Low-Dimensional Topology
- Abstract: The Jones polynomial is a Laurent-polynomial invariant of oriented links. It formed when a trace arising from finite-index subfactor theory was applied to braid-group representations and normalized so that its value depended only on the isotopy class of the braid closure, thereby solving a precise descent problem from braid presentations to links.

## 2. Core Record

### Precise Description

For an oriented link \(L\subset S^3\), the Jones polynomial is the ambient-isotopy invariant
\[
V_L(t)\in \mathbb Z[t^{1/2},t^{-1/2}]
\]
characterized, in a standard normalization, by
\[
V_{\bigcirc}(t)=1
\]
and the skein relation
\[
t^{-1}V_{L_+}(t)-tV_{L_-}(t)
   =\bigl(t^{1/2}-t^{-1/2}\bigr)V_{L_0}(t).
\]
Here \(L_+\), \(L_-\), and \(L_0\) agree outside a ball and inside it differ respectively by a positive crossing, a negative crossing, and the oriented smoothing. These conditions determine \(V_L\) recursively; for a knot its exponents are integral, whereas a link may require half-integral exponents. Equivalent conventions may invert \(t\), multiply by a component-dependent normalization, or change signs, so the normalization must be stated when polynomials are compared [1].

### Mathematical Context and Formation

The immediate problem was to turn algebraic data attached to a braid into a quantity attached to the closed link, independent of the chosen braid presentation. Alexander's theorem represents every oriented link as the closure \(\widehat\beta\) of some braid \(\beta\in B_n\), but this does not by itself produce a link invariant: the same link has many braid representatives, often on different numbers of strands. Markov's theorem identifies the precise obstruction. Besides conjugation in a fixed \(B_n\), one must preserve the value under the stabilizations
\[
\beta\longmapsto \beta\sigma_n^{\pm1}\in B_{n+1}.
\]
An ordinary character or trace of a braid representation handles conjugation by cyclicity, but generally changes under stabilization; hence an unnormalized trace of a braid word does not descend to its closure.

Jones's finite-index subfactor work supplied the missing structure. The associated tower of algebras carried canonical traces and projections satisfying the Temperley--Lieb relations. Suitable invertible combinations of these projections satisfy the braid relations, giving representations of \(B_n\). More importantly, the tower trace obeys a conditional-expectation, or Markov, rule of the form
\[
\operatorname{tr}_{n+1}(x e_n)=\delta\,\operatorname{tr}_n(x),
\]
with a fixed scalar \(\delta\). Thus stabilization changed the trace in a controlled multiplicative way rather than unpredictably. A correction depending on the strand number and the exponent sum of the braid compensated for the two stabilization signs. The resulting normalized trace was therefore invariant under both kinds of Markov move and became \(V_{\widehat\beta}(t)\) [1]. This explains the object's formation mathematically: the Jones polynomial is the normalized trace quantity forced by the problem of descending the new subfactor-derived braid representation from braids to closed links, not merely an already existing polynomial later applied to knots.

### Essential Role

The Jones polynomial made the descent step tractable. Cyclicity of the trace removes dependence on conjugating the braid representative; the Markov rule controls the change caused by adding a strand; and the exponent-sum/strand normalization cancels that change for both positive and negative stabilization. Markov's theorem then converts those algebraic checks into invariance under ambient isotopy of the closed link [1].

The quadratic relation obeyed by each braid-generator image has a second direct effect: after taking the normalized trace, it becomes the three-term skein relation displayed above. A global equivalence problem for link diagrams is thereby reformulated as local crossing changes and smoothings, permitting recursive calculation and comparison of links. The object does not solve knot classification completely, since distinct links can share a Jones polynomial. Its essential contribution to the motivating problem is instead a new, computable invariant whose well-definedness follows from the exact compatibility between braid closure, Markov moves, and the subfactor trace. Structurally, it also showed that operator-algebraic trace data and braid relations can encode three-dimensional topological information; that mechanism, rather than generic later applications, is the central insight of its formation.

## 3. Notes

The Jones polynomial is distinct from the earlier Alexander polynomial: both are one-variable Laurent-polynomial link invariants, but they satisfy different skein relations and arise from different algebraic constructions. The Kauffman bracket later provided a diagrammatic state-sum construction of the same normalized invariant; it is an alternative formulation, not the operator-algebraic route by which the object first formed. The Jones polynomial is also a specialization of later two-variable link polynomials, but those extensions are not part of its original defining role.

## 4. Sources

[1] Vaughan F. R. Jones, “A Polynomial Invariant for Knots via von Neumann Algebras,” *Bulletin of the American Mathematical Society* (New Series) 12 (1985), 103–111. https://doi.org/10.1090/S0273-0979-1985-15304-2

[2] Vaughan F. R. Jones, “Hecke Algebra Representations of Braid Groups and Link Polynomials,” *Annals of Mathematics* 126 (1987), 335–388. https://doi.org/10.2307/1971403
