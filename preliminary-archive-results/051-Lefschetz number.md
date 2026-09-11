# Mathematical Object Origin Archive | Lefschetz Number

## 1. Archive Information

- Standard Name: Lefschetz number
- Mathematical Field: Algebraic Topology
- Abstract: The Lefschetz number is the alternating sum of the traces induced by a self-map on homology. It was formed to turn the geometric fixed-point problem for a continuous self-map into a homotopy-invariant algebraic calculation. Its nonvanishing forces a fixed point, while under isolated-fixed-point hypotheses it equals the sum of local fixed-point indices.

## 2. Core Record

### Precise Description

Let \(X\) be a finite CW complex (equivalently for the classical theorem, one may take a compact polyhedron), let \(f:X\to X\) be continuous, and take rational homology so that every \(H_q(X;\mathbb{Q})\) is finite-dimensional. The **Lefschetz number** of \(f\) is
\[
L(f)=\sum_{q\ge 0}(-1)^q\operatorname{tr}\!\left(f_{*q}:H_q(X;\mathbb{Q})\to H_q(X;\mathbb{Q})\right).
\]
Only finitely many terms are nonzero. This rational-homology formula has an integer value: equivalently, it is the alternating trace of a cellular or simplicial chain map over \(\mathbb Z\), with the equality between chain-level and homology-level alternating traces supplied by the Hopf trace principle. The number depends only on the homotopy class of \(f\). In particular,
\[
L(\operatorname{id}_X)=\sum_q(-1)^q\dim H_q(X;\mathbb{Q})=\chi(X).
\]

For a self-map of a finite polyhedron, the Lefschetz fixed-point theorem states
\[
L(f)\ne 0\quad\Longrightarrow\quad \operatorname{Fix}(f)\ne\varnothing.
\]
When the fixed points are isolated and local fixed-point indices are defined, the more precise Lefschetz–Hopf formula is
\[
L(f)=\sum_{x\in\operatorname{Fix}(f)}\operatorname{ind}(f,x).
\]
Thus \(L(f)\) is not generally the cardinality of the fixed-point set: it is an algebraic, signed total.

### Mathematical Context and Formation

The motivating problem belongs to a concrete class: for continuous maps \(f,g:M\to N\) between closed oriented manifolds of the same dimension, decide whether there is a coincidence point \(x\) with \(f(x)=g(x)\); the fixed-point problem is the case \(M=N\) and \(g=\operatorname{id}_M\). Lefschetz's 1926 paper explicitly set out to obtain formulas for fixed points and coincidences of continuous transformations [1]. The geometric condition is that the map \((f,g):M\to N\times N\) meet the diagonal \(\Delta_N\). For self-maps this says that the graph of \(f\) meets the diagonal.

The difficulty is that solving \(f(x)=x\) point by point is neither a finite algebraic procedure for an arbitrary continuous map nor stable under homotopy. Individual fixed points can move, split, or be created and annihilated in pairs. An unsigned count therefore cannot provide the desired topological obstruction. Brouwer-type results established existence on balls, but their domain-specific hypotheses did not by themselves yield a computable criterion sensitive to the action of a map on an arbitrary triangulable space. Local fixed-point indices capture signs when fixed points are already isolated, yet direct local calculation still presupposes access to the fixed points one is trying to detect.

The decisive reformulation is to count intersections algebraically rather than count solutions literally. After putting the graph and diagonal in suitable position, isolated intersections carry signs; cancellation of opposite signs is precisely what makes their total invariant under deformation. Homology records this global intersection class, and Poincaré duality converts its pairing with the diagonal into an alternating trace of the maps induced on homology. In the fixed-point specialization \(g=\operatorname{id}\), the resulting scalar is \(L(f)\). For finite complexes, simplicial approximation and the Hopf trace principle extend this trace expression beyond the transverse manifold picture: the same alternating trace can be calculated on finite chain groups and is unchanged on passage to homology [2]. This explains mathematically why the object's defining features are exactly a trace—measuring the part of each homology group returned to itself—and alternating signs—combining dimensions with the signs required by chain-complex and intersection theory.

### Essential Role

The Lefschetz number makes the existence-obstruction part of the fixed-point problem tractable. Instead of locating solutions of \(f(x)=x\), one computes finitely many linear maps \(f_{*q}\) and their traces. If there were no fixed point, a sufficiently fine simplicial approximation can be arranged so that no simplex contributes a diagonal term; its alternating chain trace is then zero. The Hopf trace principle identifies that chain trace with \(L(f)\). Contrapositively, \(L(f)\ne0\) forces a fixed point [2]. Because induced homology maps are homotopy invariant, the same computation proves the stronger conclusion that every map homotopic to \(f\) has a fixed point.

Under isolated-fixed-point hypotheses, the local-to-global formula explains what the invariant has retained from the original geometric question: every fixed point contributes its local index, and \(L(f)\) is their signed sum. The signs allow unstable pairs to cancel, overcoming the failure of raw cardinality to survive deformation. The construction therefore does not merely supply another sufficient condition; it recasts coincidence with the diagonal as a global trace and shows that fixed-point data are constrained by the action of the map on the homology of the whole space. The familiar consequence for a contractible finite polyhedron illustrates the mechanism rather than a later application: all positive-degree rational homology vanishes and \(f_{*0}\) has trace \(1\), so \(L(f)=1\), recovering fixed-point existence without solving the fixed-point equation.

## 3. Notes

- The Lefschetz number should be distinguished from the local fixed-point index. The former is a global invariant of a self-map; the latter is attached to an isolated fixed point or an admissible fixed-point region. Their equality after summing is a theorem, not a definition.
- The implication is one-way: \(L(f)=0\) does not imply that \(f\) is fixed-point-free.
- More general Lefschetz numbers are defined for spaces and homology theories satisfying suitable finiteness and trace conditions, but the finite-polyhedron setting is the classical core relevant to the motivating problem.

## 4. Sources

[1] Solomon Lefschetz, “Intersections and Transformations of Complexes and Manifolds,” *Transactions of the American Mathematical Society* 28 (1926), 1–49. https://doi.org/10.1090/S0002-9947-1926-1501331-3

[2] Robert F. Brown, *The Lefschetz Fixed Point Theorem*, Scott, Foresman and Company, 1971.

[3] Martin Arkowitz and Robert F. Brown, “The Lefschetz–Hopf Theorem and Axioms for the Lefschetz Number,” *Fixed Point Theory and Applications* 2004, no. 1 (2004), 1–11. https://doi.org/10.1155/S1687182004312099
