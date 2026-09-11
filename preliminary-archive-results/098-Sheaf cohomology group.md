# Mathematical Object Origin Archive | Sheaf Cohomology Group

## 1. Archive Information

- Standard Name: Sheaf cohomology group \(H^q(X,\mathcal F)\)
- Mathematical Field: Algebraic Topology; Complex Analysis; Homological Algebra
- Abstract: For a sheaf \(\mathcal F\) of abelian groups on a space \(X\), the group \(H^q(X,\mathcal F)\) is, in its modern formulation, the \(q\)-th right derived functor of global sections. Higher sheaf cohomology does not measure a failure of the sheaf axiom—local sections that agree on overlaps already glue uniquely. Rather, it records failures of exact global lifting and combines coefficient data that vary locally over a space. The object arose in Leray’s algebraic-topological treatment of continuous maps and was subsequently reformulated and developed for global problems in complex analysis.

## 2. Core Record

### Precise Description

Let \(X\) be a topological space and \(\mathcal F\) a sheaf of abelian groups on \(X\). The global-section functor
\[
\Gamma(X,-):\operatorname{Sh}(X)\longrightarrow \operatorname{Ab}
\]
is left exact but generally not right exact. If
\[
0\longrightarrow \mathcal F\longrightarrow \mathcal I^0\longrightarrow \mathcal I^1\longrightarrow\cdots
\]
is an injective resolution, the modern standard definition is
\[
H^q(X,\mathcal F):=H^q\!\left(\Gamma(X,\mathcal I^\bullet)\right)
=R^q\Gamma(X,\mathcal F).
\]
It is independent, up to canonical isomorphism, of the resolution, and \(H^0(X,\mathcal F)=\Gamma(X,\mathcal F)\) [4][5]. This derived-functor definition is Grothendieck’s later intrinsic formulation, not Leray’s original construction [2][4].

Given an open cover \(\mathfrak U=\{U_i\}\), one can also form the Čech complex
\[
C^p(\mathfrak U,\mathcal F)=
\prod_{i_0<\cdots<i_p}\mathcal F(U_{i_0}\cap\cdots\cap U_{i_p})
\]
with alternating restriction differential. If the cover is \(\mathcal F\)-acyclic, its Čech cohomology computes \(H^q(X,\mathcal F)\); this need not hold for an arbitrary fixed cover [5]. More generally, a short exact sequence
\[
0\longrightarrow\mathcal F'\longrightarrow\mathcal F\longrightarrow\mathcal F''\longrightarrow0
\]
gives connecting maps
\[
\delta:H^q(X,\mathcal F'')\longrightarrow H^{q+1}(X,\mathcal F'),
\]
so a locally available lift of a global section of \(\mathcal F''\) has a canonical obstruction \(\delta(s)\in H^1(X,\mathcal F')\).

### Mathematical Context and Formation

The original formation was algebraic-topological. Leray sought methods applicable to broad classes of topological spaces and continuous maps without making simplicial approximation or a chosen triangulation the organizing device [1][2]. A concrete problem class was this: for a continuous map
\[
\pi:E\longrightarrow B,
\]
how can one determine the cohomology of the total space \(E\) from the topology of the base together with the cohomology present over its varying regions? Replacing \(\pi\) merely by separate groups \(H^q(\pi^{-1}(b);A)\) loses how those groups vary and restrict as \(b\) moves. Treating them as one constant coefficient group is especially inadequate when transport around the base is nontrivial or the local topology changes. A global simplicial calculation on \(E\), when available, computes an answer but does not isolate the contribution made by the map and its local fibers [1][2].

Leray’s response was to localize cohomological data on the base: in his closed-set language, a closed region \(F\subseteq B\) was assigned cohomology coming from \(\pi^{-1}(F)\), with restriction data as \(F\) varied. He introduced sheaves and their cohomology in this setting and organized the resulting groups into the spectral mechanism associated with a map [1][2]. In modern notation the corresponding local coefficient object is the higher direct-image sheaf \(R^q\pi_*\mathcal A\), and the relationship is expressed by the Leray spectral sequence
\[
E_2^{p,q}=H^p\!\left(B,R^q\pi_*\mathcal A\right)
\Longrightarrow H^{p+q}(E,\mathcal A).
\]
Thus cohomology on the base had to accept a sheaf—not only a single constant group—as its coefficient object.

The preceding paragraph is a modern mathematical reconstruction of the structural need visible in Leray’s work, not a claim that Leray used current functorial notation. His original theory used supports, closed subsets, covers, and filtered complexes. Cartan’s seminars of 1950–1951 recast sheaves over open sets, axiomatized sheaf cohomology, and constructed it using fine resolutions; Grothendieck’s 1955 lectures and 1957 paper subsequently identified it with the right derived functors of global sections [2][3][4]. These are successive formulations of the object and should not be conflated.

There was also a distinct complex-analytic formation strand. In the early 1950s, Cartan’s program integrated Leray’s cohomology with global analytic problems such as the first Cousin problem [3][6]. Given local meromorphic functions \(f_i\) whose differences \(f_i-f_j\) are holomorphic, the issue is not gluing already agreeing sections; it is whether holomorphic corrections \(h_i\) can be found so that \(f_i-h_i\) agree. Smooth partitions of unity do not preserve holomorphicity, and pairwise local solvability alone supplies no global correction. Sheaf cohomology therefore became an exact obstruction language for this analytic problem. This was a major adoption and development of the general object, not its unqualified historical origin [2][3][6].

### Essential Role

For Leray’s map problem, the essential role of \(H^p(B,R^q\pi_*\mathcal A)\) was to combine two kinds of information that a constant coefficient group or an undifferentiated computation on \(E\) did not keep separate: degree \(q\) records cohomology over inverse images of local regions of \(B\), while degree \(p\) records the global topology of the base acting on that varying local information. The sheaf’s restriction maps preserve how the local groups fit together; sheaf cohomology then aggregates them globally. The spectral sequence filters \(H^n(E,\mathcal A)\) and supplies successive pages on which differentials measure interactions among the bidegrees \(p+q=n\). It thereby reformulates the calculation of total-space cohomology as a structured passage from local-over-the-base data to a global invariant [1][2].

This is the direct contribution of the object to the motivating problem class: it made cohomology with spatially varying coefficients into a computable intermediate object, rather than forcing the variation either into a constant coefficient system or back into one global chain complex. It also introduced the structural viewpoint that the topology of a map, not only of an isolated space, can be studied by placing local cohomological data on its target.

In the later analytic development, the same structure made the first Cousin obstruction precise. Let \(\mathcal O\), \(\mathcal M\), and \(\mathcal P=\mathcal M/\mathcal O\) denote the sheaves of holomorphic functions, meromorphic functions, and additive principal parts. From
\[
0\longrightarrow\mathcal O\longrightarrow\mathcal M\longrightarrow\mathcal P\longrightarrow0
\]
a prescribed global principal-part datum \(s\in\Gamma(X,\mathcal P)\) receives the canonical connecting class
\[
\delta(s)\in H^1(X,\mathcal O).
\]
It is globally realizable by a meromorphic function exactly when \(\delta(s)=0\). Choosing local meromorphic lifts \(f_i\) produces the Čech cocycle \(c_{ij}=f_i-f_j\); its Čech class maps under the Čech-to-derived comparison to the canonical class \(\delta(s)\), and the two are identified on an \(\mathcal O\)-acyclic cover. Hence the cocycle is not an alleged failure to glue agreeing holomorphic sections: it records the failure to choose local lifts that agree. Vanishing supplies corrections \(c_{ij}=h_i-h_j\), after which \(f_i-h_i\) genuinely agree and glue [5][6].

## 3. Notes

Sheaf cohomology and Čech cohomology of one arbitrary cover are not synonymous. The original Leray constructions, Cartan’s axiomatic and fine-resolution treatment, and Grothendieck’s derived-functor definition are historically and formally distinct, although comparison and uniqueness results relate the resulting theories under standard hypotheses. The first Cousin problem uses the additive sheaf \(\mathcal O\); the second Cousin problem is multiplicative and leads to \(H^1(X,\mathcal O^*)\), so the two obstruction groups should not be conflated.

## 4. Sources

[1] Jean Leray, “L’anneau spectral et l’anneau filtré d’homologie d’un espace localement compact et d’une application continue,” *Journal de Mathématiques Pures et Appliquées*, 9e série, 29 (1950), 1–139.

[2] Haynes Miller, “Leray in Oflag XVIIA: The Origins of Sheaf Theory, Sheaf Cohomology, and Spectral Sequences,” *Gazette des Mathématiciens* 84, supplément (2000), 17–34, https://math.mit.edu/~hrm/papers/ss.pdf.

[3] Henri Cartan, “Faisceaux sur un espace topologique I–II” and “Théorie axiomatique de la cohomologie,” *Séminaire Henri Cartan* 3 (1950–1951), exposés 14–16.

[4] Alexander Grothendieck, “Sur quelques points d’algèbre homologique,” *Tôhoku Mathematical Journal* 9 (1957), 119–221.

[5] Roger Godement, *Topologie algébrique et théorie des faisceaux*, Hermann, 1958.

[6] Robert C. Gunning and Hugo Rossi, *Analytic Functions of Several Complex Variables*, Prentice-Hall, 1965.
