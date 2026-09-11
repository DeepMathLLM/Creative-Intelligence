# Mathematical Object Origin Archive | Conley Index

## 1. Archive Information

- Standard Name: Conley index of an isolated invariant set
- Mathematical Field: Dynamical Systems; Algebraic Topology
- Abstract: The Conley index is the pointed homotopy type obtained by collapsing the exit part of an isolating neighborhood of an isolated invariant set. It was formed to extract robust topological information from invariant dynamics that may be nonhyperbolic, may contain several recurrent pieces and connecting orbits, and need not be accessible through a Morse index or a local linearization. Its quotient construction records what remains trapped while making the result independent of the auxiliary neighborhood and stable under continuation.

## 2. Core Record

### Precise Description

Let \(\varphi:\mathbb{R}\times X\to X\) be a continuous flow on a locally compact metric space. For a compact set \(N\subset X\), set
\[
\operatorname{Inv}(N)=\{x\in N: \varphi(t,x)\in N\text{ for every }t\in\mathbb{R}\}.
\]
A compact invariant set \(S\) is *isolated* if there is a compact neighborhood \(N\) such that
\[
S=\operatorname{Inv}(N)\subset \operatorname{int}N.
\]
Such an \(N\) is an isolating neighborhood.

An index pair for \(S\) is a pair of compact sets \(N_0\subset N_1\subset X\) for which:

1. \(\overline{N_1\setminus N_0}\) is an isolating neighborhood for \(S\), with \(S\subset\operatorname{int}(N_1\setminus N_0)\);
2. \(N_0\) is positively invariant relative to \(N_1\): if \(x\in N_0\) and \(\varphi([0,t],x)\subset N_1\), then \(\varphi([0,t],x)\subset N_0\);
3. \(N_0\) is an exit set: if \(x\in N_1\) and \(\varphi(t,x)\notin N_1\) for some \(t>0\), then for some \(\tau\in[0,t]\), \(\varphi([0,\tau],x)\subset N_1\) and \(\varphi(\tau,x)\in N_0\).

The **Conley index** \(h(S,\varphi)\) is the pointed homotopy type of
\[
(N_1/N_0,[N_0]),
\]
where all of \(N_0\) is collapsed to the basepoint; when \(N_0=\varnothing\), a disjoint basepoint is adjoined. Index pairs exist, and the resulting pointed homotopy type is independent of the chosen index pair. The homological Conley index is correspondingly
\[
CH_k(S)=\widetilde H_k(N_1/N_0)\cong H_k(N_1,N_0)
\]
under the usual good-pair hypotheses. The index is also invariant under continuation: subject to the standard compactness and isolation hypotheses, a parameterized family of flows whose associated invariant sets remain isolated in a common isolating neighborhood has constant Conley index [1,2].

For calibration, if \(S=\{p\}\) is a hyperbolic equilibrium with an unstable subspace of dimension \(m\), then
\[
h(S,\varphi)\simeq (S^m,*).
\]
For a nondegenerate critical point of Morse index \(m\) under the negative gradient flow, this recovers the same sphere and hence the classical Morse-index information [1].

### Mathematical Context and Formation

The motivating problem class is to detect and compare isolated invariant behavior in a flow without requiring that the invariant set be a single nondegenerate equilibrium. Concretely, given a bounded region containing an unknown maximal invariant set, one wants an invariant that can (i) certify that invariant dynamics occur in the region, (ii) distinguish some forms of local instability, and (iii) survive perturbations as long as no invariant trajectory reaches the boundary of the isolating region.

The familiar local tools did not solve this problem at the required level of generality. The Morse index applies to a nondegenerate critical point of a function, and unstable eigenspace dimension supplies a local integer for a hyperbolic equilibrium. An isolated invariant set, however, can be nonhyperbolic or can consist of equilibria, periodic orbits, other recurrent pieces, and connecting trajectories taken together. It may have no distinguished point at which a Hessian or linearization yields a complete descriptor. Moreover, merely taking the homotopy type or homology of an isolating neighborhood does not isolate the dynamical content: the neighborhood contains transit points, and different neighborhoods may have different ordinary topology even though they isolate the same invariant set.

The decisive construction is therefore not to model \(S\) directly but to retain a neighborhood together with its forward escape data. The subset \(N_0\) marks every route by which trajectories leave \(N_1\), while relative positive invariance prevents a trajectory already in that exit set from re-entering the dynamically relevant part before leaving \(N_1\). Collapsing \(N_0\) to one point turns all escape into a single pointed state and retains the topology of the part organized around the maximal invariant set. The index-pair axioms are exactly what make this topological quotient compatible with the flow; the comparison theorem for index pairs then removes dependence on the chosen pair. Thus a local dynamical problem that lacks a canonical geometric model is converted into a canonical pointed homotopy type [1,2].

### Essential Role

The Conley index made the robust detection of isolated invariant dynamics tractable from neighborhood and boundary-flow information rather than from an explicit description of every orbit in \(S\). Its two structural components perform different jobs. Isolation separates the target dynamics from the rest of phase space, while the pair \((N_1,N_0)\) records which boundary behavior is genuine escape. The quotient \(N_1/N_0\) discards the accidental geometry of the exit routes without discarding how the nonescaping region is attached to them. Independence from the index pair then converts this computable local model into an invariant of \(S\), rather than of the selected neighborhood.

This directly answers the motivating detection problem. The empty isolated invariant set has the trivial pointed index, so a nontrivial Conley index forces \(S\neq\varnothing\); the converse need not hold. Continuation invariance answers the perturbation problem: if one flow is deformed while a fixed neighborhood remains isolating, the indexed invariant set may change internally, split into recurrent pieces, or lose hyperbolicity, but its Conley index does not change. Consequently, a change between endpoint indices proves that such an isolated continuation cannot persist throughout the deformation. This provides existence and bifurcation information without following individual trajectories.

The sphere computation for a hyperbolic equilibrium explains precisely how the construction extends the older index. Locally, the exit set lies in the unstable directions, and collapsing it turns an unstable \(m\)-disk relative to its boundary into \(D^m/\partial D^m\cong S^m\). The integer unstable dimension is thereby replaced by a pointed homotopy type that still agrees with it in the classical case but remains defined for much more complicated isolated invariant sets. The deeper structural viewpoint is that local instability is encoded not only by a count of expanding directions but by the relative topology of an isolating neighborhood and its dynamically determined exit set.

## 3. Notes

The Conley index is an invariant of an isolated invariant set together with its flow; it is not the ordinary homotopy type of the invariant set itself. Its homology is easier to compute but can forget information present in the pointed homotopy type. A trivial index does not imply that the isolated invariant set is empty. Variants for discrete maps require additional index-map data, so the flow definition above should not be transferred verbatim to that setting.

## 4. Sources

[1] Charles C. Conley, *Isolated Invariant Sets and the Morse Index*, CBMS Regional Conference Series in Mathematics, no. 38, American Mathematical Society, 1978.

[2] Dietmar Salamon, “Connected Simple Systems and the Conley Index of Isolated Invariant Sets,” *Transactions of the American Mathematical Society* 291, no. 1 (1985), 1–41, https://doi.org/10.1090/S0002-9947-1985-0797044-3.
