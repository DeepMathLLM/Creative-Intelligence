# Mathematical Object Origin Archive | Persistence Module

## 1. Archive Information

- Standard Name: Persistence module
- Mathematical Field: Algebraic Topology
- Abstract: A persistence module is a functorial family of vector spaces or modules indexed by a scale parameter. It was formed to retain how homology classes change across a filtration, thereby turning multiscale topological inference and the computation of persistent homology into a structured algebraic problem.

## 2. Core Record

### Precise Description

Let \((P,\leq)\) be a poset, regarded as a category with one morphism \(p\to q\) exactly when \(p\leq q\), and let \(k\) be a field. A persistence module over \(P\) is a functor
\[
V:P\longrightarrow \mathbf{Vect}_k.
\]
Equivalently, it consists of vector spaces \(V_p\) and linear transition maps
\[
\varphi_{p,q}:V_p\longrightarrow V_q \qquad (p\leq q)
\]
satisfying \(\varphi_{p,p}=\operatorname{id}_{V_p}\) and \(\varphi_{q,r}\varphi_{p,q}=\varphi_{p,r}\) whenever \(p\leq q\leq r\). One may replace \(\mathbf{Vect}_k\) by modules over a fixed ring; the field-valued version is the standard setting for barcode classification.

If \(K_p\subseteq K_q\) for \(p\leq q\) is a filtered family of spaces or simplicial complexes, then, for each homological degree \(n\),
\[
V_p=H_n(K_p;k),\qquad
\varphi_{p,q}=H_n(K_p\hookrightarrow K_q;k)
\]
defines a persistence module. The persistent homology group between two parameters is the image
\[
H_n^{p,q}=\operatorname{im}(\varphi_{p,q}),
\]
not the whole persistence module.

For a discretely indexed module \(V_0\to V_1\to V_2\to\cdots\), the graded vector space \(M=\bigoplus_{i\geq0}V_i\) becomes a graded \(k[t]\)-module by setting \(t v=\varphi_{i,i+1}(v)\) for \(v\in V_i\). Conversely, multiplication by \(t\) in a graded \(k[t]\)-module supplies the consecutive transition maps. This algebraic correspondence is central to the original finite-type formulation [2].

### Mathematical Context and Formation

The motivating problem class is multiscale recovery and computation of topology from incomplete or imprecise geometric information. For example, given a finite point cloud \(X\subset\mathbb{R}^d\), one builds nested Čech or Vietoris–Rips complexes
\[
K_{r_0}\subseteq K_{r_1}\subseteq\cdots\subseteq K_{r_m}
\]
as the distance threshold increases. Small thresholds may leave the sample disconnected, while larger thresholds may fill holes as well as create short-lived combinatorial ones. Since the data usually provide no canonically correct threshold, the concrete task is not merely to compute \(H_n(K_r;k)\) once, but to determine which classes survive across scales and to compute their births and deaths. This multiscale difficulty was the setting of topological persistence [1].

Ordinary homology applied separately at each scale is inadequate for that task: the list of groups, or even all Betti numbers \(\dim H_n(K_r;k)\), forgets which class at one stage maps to which class at a later stage. Thus it cannot by itself express survival. The decisive formation step was to retain the inclusion-induced homomorphisms together with the homology groups. Functoriality supplies the compatibility relations, so the resulting diagram is one algebraic object rather than unrelated topological snapshots.

In the discrete finite-filtration setting, Zomorodian and Carlsson explicitly formalized this object as a persistence module and recognized the sequence as a graded module over a polynomial ring [2]. That recognition addressed a second concrete problem: finding a simple classification and a computable representation of persistent homology beyond the earlier algorithmic restriction to subcomplexes of \(S^3\) with \(\mathbb{Z}_2\)-coefficients. Over a field, the passage to finitely generated graded \(k[t]\)-modules made the structure theorem over the principal ideal domain \(k[t]\) available, while the filtration supplied finite matrices from which the module could be computed [2].

### Essential Role

The transition maps are exactly the added structure that makes persistence measurable. For \(p\leq q\), the rank of \(\varphi_{p,q}\) counts the independent degree-\(n\) classes present at \(p\) that remain nonzero at \(q\); kernels record classes that die under passage to later stages. Consequently, the module resolves the scale-selection obstacle by replacing the demand for one privileged scale with a comparison across all scales. It does not declare every long-lived class to be genuine, but it makes lifetime a mathematically defined and computable quantity.

For a finite-type, one-parameter persistence module over a field, the graded-module structure gives a decomposition, with the generator of \(k[t](-b)\) placed in degree \(b\), of the form
\[
M\cong
\bigoplus_{\alpha} k[t](-b_\alpha)
\;\oplus\;
\bigoplus_{\beta} \bigl(k[t]/(t^{\ell_\beta})\bigr)(-b_\beta).
\]
A free summand represents a class born at \(b_\alpha\) that persists indefinitely; a torsion summand represents one born at \(b_\beta\) and killed after \(\ell_\beta\) steps. Hence the otherwise complicated system of spaces, cycles, boundaries, and inclusion maps is reduced to interval data, while matrix reduction can compute the corresponding birth–death pairs in arbitrary homological dimension over any field [2]. This is the precise tractability gained: persistent homology groups for every parameter pair can be recovered from one classified algebraic object rather than recomputed and matched ad hoc.

The deeper viewpoint introduced by the object is that topology under changing scale is functorial evolution, not a collection of static invariants. Later formulations express this directly as a functor from an ordered parameter category, and interval-decomposition results extend the barcode viewpoint to pointwise finite-dimensional modules over suitable totally ordered sets [3].

## 3. Notes

A persistence module should not be conflated with a barcode or a persistence diagram. The module is the functorial algebraic object; a barcode is the multiset of intervals obtained when an interval decomposition theorem applies. Finite-type one-parameter modules over a field have the decomposition used above. More general persistence modules need not have a finite barcode, and multiparameter modules generally do not admit classification solely by intervals.

## 4. Sources

[1] Herbert Edelsbrunner, David Letscher, and Afra Zomorodian, “Topological Persistence and Simplification,” *Discrete & Computational Geometry* 28 (2002), 511–533. https://doi.org/10.1007/s00454-002-2885-2

[2] Afra Zomorodian and Gunnar Carlsson, “Computing Persistent Homology,” *Discrete & Computational Geometry* 33 (2005), 249–274. https://doi.org/10.1007/s00454-004-1146-y

[3] William Crawley-Boevey, “Decomposition of Pointwise Finite-Dimensional Persistence Modules,” *Journal of Algebra and Its Applications* 14, no. 5 (2015), 1550066. https://doi.org/10.1142/S0219498815500668
