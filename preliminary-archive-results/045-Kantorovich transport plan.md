# Mathematical Object Origin Archive | Kantorovich Transport Plan

## 1. Archive Information

- Standard Name: Kantorovich transport plan
- Mathematical Field: Probability Theory and Stochastic Processes; Functional Analysis
- Abstract: A Kantorovich transport plan is a joint measure with prescribed source and target marginals. It was formed by relaxing mass transport by a deterministic map to mass allocation on pairs of locations, thereby allowing splitting and turning the transport problem into a linear optimization problem over a weakly compact convex set.

## 2. Core Record

### Precise Description

Let \(X\) and \(Y\) be Polish spaces with Borel probability measures \(\mu\in\mathcal P(X)\) and \(\nu\in\mathcal P(Y)\). A **Kantorovich transport plan** from \(\mu\) to \(\nu\) is a Borel probability measure \(\pi\in\mathcal P(X\times Y)\) whose marginals are \(\mu\) and \(\nu\):
\[
(p_X)_\#\pi=\mu,\qquad (p_Y)_\#\pi=\nu,
\]
where \(p_X(x,y)=x\) and \(p_Y(x,y)=y\). Equivalently,
\[
\pi(A\times Y)=\mu(A),\qquad \pi(X\times B)=\nu(B)
\]
for all Borel sets \(A\subseteq X\) and \(B\subseteq Y\). The set of such plans is denoted by \(\Pi(\mu,\nu)\).

For a measurable cost \(c:X\times Y\to[0,\infty]\), the plan's transportation cost is
\[
C_c(\pi)=\int_{X\times Y}c(x,y)\,d\pi(x,y),
\]
and an optimal Kantorovich transport plan is a minimizer of \(C_c\) over \(\Pi(\mu,\nu)\) [2]. A measurable transport map \(T:X\to Y\) satisfying \(T_\#\mu=\nu\) determines the graph-supported plan
\[
\pi_T=(\operatorname{id}_X,T)_\#\mu.
\]
Conversely, not every plan is graph-supported. On standard Borel spaces, disintegration writes a plan as \(\pi(dx,dy)=\mu(dx)K(x,dy)\), where the probability kernel \(K(x,\cdot)\) can distribute the mass at \(x\) among several destinations.

### Mathematical Context and Formation

The motivating problem class is optimal mass transportation. Given source and target distributions \(\mu\) and \(\nu\) of equal total mass and a unit cost \(c(x,y)\), the Monge formulation asks for a measurable map \(T\) such that \(T_\#\mu=\nu\) and
\[
\int_X c(x,T(x))\,d\mu(x)
\]
is minimal. The map requirement is the central obstruction: all mass situated at a given \(x\) must be sent to one destination \(T(x)\). An admissible map may therefore fail to exist. For example, no map can push \(\delta_0\) to \(\tfrac12\delta_{-1}+\tfrac12\delta_1\), because the single source atom cannot be divided. Even when admissible maps exist, the associated class of graph-supported plans is generally not closed under nontrivial convex mixtures, and limits of increasingly fine or oscillatory map-based allocations need not remain concentrated on a graph. Thus the map formalism does not in general provide the closed convex feasible class needed for a direct existence and linear-optimization argument.

The formative insight is already visible in a finite transportation problem. Instead of assigning each source site \(i\) to one target, introduce nonnegative shipment amounts \(\gamma_{ij}\) satisfying the supply and demand equations
\[
\sum_j\gamma_{ij}=a_i,\qquad \sum_i\gamma_{ij}=b_j,
\]
and minimize the linear cost \(\sum_{i,j}c_{ij}\gamma_{ij}\). Replacing the shipment matrix \((\gamma_{ij})\) by a measure on \(X\times Y\), and the row and column equations by prescribed marginal conditions, produces \(\pi\in\Pi(\mu,\nu)\). This measure-theoretic linear-programming relaxation is the Kantorovich formulation of translocation of masses [1]. It retains exact conservation of source and target mass while removing only the indivisibility imposed by a deterministic map.

### Essential Role

The transport plan makes the existence and optimization stage of the mass-transport problem tractable. First, \(\Pi(\mu,\nu)\) is never empty, since it contains \(\mu\otimes\nu\). Its marginal constraints are linear, so it is convex. For Polish \(X,Y\), fixed marginals make this family tight, and the marginal conditions are closed under weak convergence; hence \(\Pi(\mu,\nu)\) is weakly compact. If \(c\) is lower semicontinuous and bounded below, then \(\pi\mapsto\int c\,d\pi\) is weakly lower semicontinuous, so the direct method yields an optimal plan [2]. These are precisely the compactness and closure properties generally unavailable within the class of graph-supported allocations.

The plan also bypasses the indivisibility obstruction: in the atomic example, the measure
\[
\pi=\tfrac12\delta_{(0,-1)}+\tfrac12\delta_{(0,1)}
\]
has the required marginals even though no Monge map exists. At the same time, graph plans remain inside the relaxed class, so the new formulation extends rather than discards deterministic transport. The linear marginal conditions further permit a dual description. If \(\varphi:X\to\mathbb R\) and \(\psi:Y\to\mathbb R\) are Borel functions with \(\varphi\in L^1(\mu)\), \(\psi\in L^1(\nu)\), and
\[
\varphi(x)+\psi(y)\le c(x,y)
\]
for all \((x,y)\), then every feasible plan obeys the weak-duality bound
\[
\int_X\varphi\,d\mu+\int_Y\psi\,d\nu\le\int_{X\times Y}c\,d\pi.
\]
Thus lower bounds and, under standard hypotheses, optimality can be analyzed through linear-programming duality [2]. Structurally, the transport plan recasts transportation as choosing a joint law with fixed marginals: the unknown is no longer necessarily a destination function but a dependence relation between source and target. The relaxation does not by itself solve the original map problem; recovering a Monge solution requires additional conditions ensuring that an optimal plan is concentrated on a graph.

## 3. Notes

“Transport plan,” “transportation plan,” and “coupling” are common synonymous terms; “transference plan” also occurs. A transport plan need not be optimal. The same definition applies to finite measures of equal total mass after replacing probability measures by finite positive measures with the prescribed marginals. A randomized kernel is a representation of a plan under suitable measurable-space hypotheses, not a separate requirement in its definition.

## 4. Sources

[1] L. V. Kantorovitch, “On the Translocation of Masses,” *Management Science* 5, no. 1 (1958), 1–4. https://doi.org/10.1287/mnsc.5.1.1

[2] Cédric Villani, *Optimal Transport: Old and New*, Grundlehren der mathematischen Wissenschaften 338, Springer, 2009, especially Chapters 1 and 4. https://doi.org/10.1007/978-3-540-71050-9
