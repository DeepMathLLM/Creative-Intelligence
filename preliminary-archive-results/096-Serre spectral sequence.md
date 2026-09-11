# Mathematical Object Origin Archive | Serre Spectral Sequence

## 1. Archive Information

- Standard Name: Serre spectral sequence
- Mathematical Field: Algebraic Topology
- Abstract: The Serre spectral sequence is a page-by-page algebraic object associated with a fibration. It begins with homology of the base with coefficients in homology of the fiber and converges to the associated graded homology of the total space. It was formed to make the homology of nontrivial fibrations computable, notably in the study of loop spaces and homotopy groups of spheres [1].

## 2. Core Record

### Precise Description

Let
\[
F\longrightarrow E\xrightarrow{\pi}B
\]
be a fibration with path-connected CW base, and let \(R\) be a coefficient ring. Transport along paths in \(B\) makes the groups \(H_q(F_b;R)\) into a local coefficient system \(\mathcal H_q\) on \(B\). The homological Serre spectral sequence is a first-quadrant collection \((E^r_{p,q},d_r)\) with
\[
E^2_{p,q}\cong H_p(B;\mathcal H_q),
\qquad
d_r:E^r_{p,q}\longrightarrow E^r_{p-r,q+r-1},
\qquad
E^{r+1}\cong H(E^r,d_r).
\]
Under the standard convergence hypotheses for this CW-fibration setting, it abuts to \(H_*(E;R)\): if \(B^{(p)}\) is the \(p\)-skeleton and \(E_p=\pi^{-1}(B^{(p)})\), then the induced filtration \(F_pH_n(E;R)\) satisfies
\[
E^\infty_{p,q}\cong
F_pH_{p+q}(E;R)/F_{p-1}H_{p+q}(E;R).
\]
If the monodromy action on fiber homology is trivial, then \(\mathcal H_q\) is constant and the \(E^2\)-term becomes \(H_p(B;H_q(F;R))\); over a field this is commonly written \(H_p(B;R)\otimes_R H_q(F;R)\). There is a cohomological form with
\[
E_2^{p,q}\cong H^p(B;\mathcal H^q),
\qquad d_r:E_r^{p,q}\to E_r^{p+r,q-r+1},
\]
converging to the associated graded of \(H^*(E;R)\), with a multiplicative structure when the coefficients and hypotheses permit it [2], [3].

### Mathematical Context and Formation

The motivating problem class was to compute the homology of the total space \(E\) of a fibration from information about its base \(B\), its fiber \(F\), and the way the fibers are assembled. A central concrete instance in Serre's work was the use of path and loop-space fibrations in the study of homotopy groups of spheres [1]. For example,
\[
\Omega S^n\longrightarrow PS^n\longrightarrow S^n
\]
has contractible total space \(PS^n\), while \(\pi_k(\Omega S^n)\cong\pi_{k+1}(S^n)\). Thus information about \(H_*(\Omega S^n)\) could provide algebraic access to a problem otherwise phrased in terms of difficult homotopy classes.

The obstacle is that a fibration is only locally product-like. For an actual product, the Künneth theorem computes \(H_*(B\times F)\) from the two factors, but in a nontrivial fibration transition around loops can act on \(H_*(F)\), and higher attaching data can mix base and fiber dimensions. Consequently, the groups \(H_*(B)\) and \(H_*(F)\) alone do not determine \(H_*(E)\). The long exact homotopy sequence records one-dimensional chains of homotopy groups, but in the path-loop example it mainly identifies the unknown sphere groups with unknown loop-space groups; it does not compute the loop-space homology or organize the interactions among all base and fiber degrees.

The forming insight was to avoid demanding an immediate formula for \(H_*(E)\). Filter \(B\) by its skeleta and pull that filtration back to \(E\). Over each open cell the fibration is homotopically a product with \(F\), so the relative homology of successive filtration stages separates a base-cell degree \(p\) from a fiber-homology degree \(q\). The first differential glues these local pieces and includes monodromy, producing cellular homology of \(B\) with the local coefficients \(\mathcal H_q\) and hence the stated \(E^2\)-page. Later differentials retain and successively resolve the higher ways in which the local products fail to assemble into a global product. This skeletal-filtration construction turned the original all-at-once computation into a controlled succession of homology calculations [1], [2].

### Essential Role

The Serre spectral sequence made the passage from base and fiber data to total-space homology tractable without falsely replacing a fibration by a product. Its bigrading preserves the two distinct sources of degree; its local coefficient system records twisting by loops in the base; its higher differentials record cross-degree gluing and transgression; and its convergence identifies exactly what remains as the graded pieces of a filtration on \(H_*(E)\). In this way it reformulates the missing global product decomposition as the concrete tasks of finding differentials and then resolving any extension problems.

The path-loop fibration displays the mechanism sharply. For \(n\ge 2\), the \(E^2\)-page for \(\Omega S^n\to PS^n\to S^n\) has nonzero columns only at \(p=0\) and \(p=n\). Degree considerations leave \(d_n\) as the only possible nonzero differential between them. Since \(PS^n\) is contractible, every positive-total-degree class must disappear by \(E^\infty\); this forces
\[
d_n:E^n_{n,q}\longrightarrow E^n_{0,q+n-1}
\]
to give the recurrence that \(H_j(\Omega S^n;\mathbb Z)\cong\mathbb Z\) when \(j\) is a nonnegative multiple of \(n-1\), and \(0\) otherwise. The spectral sequence has therefore extracted nontrivial loop-space homology from a fibration whose fiber was initially the unknown part. Such calculations supplied the homological input for attacks on sphere homotopy, rather than by themselves constituting a complete computation of all homotopy groups [1], [2].

The deeper structural change was to treat a fibration not as a defective product but as a filtered object whose failure to split is itself computable. The pages distinguish successive levels of that failure, and transgression turns geometric attachment in the total space into explicit algebraic maps between base and fiber invariants.

## 3. Notes

The name “Leray–Serre spectral sequence” emphasizes that Serre's construction belongs to the spectral-sequence method initiated by Leray; “Serre spectral sequence” usually denotes the singular (co)homology sequence of a fibration. Convergence gives an associated graded object, not automatically a canonical direct-sum decomposition of \(H_*(E)\), so differential and extension ambiguities are genuine limitations. The local-coefficient formulation is needed when \(\pi_1(B)\) acts nontrivially on fiber (co)homology.

## 4. Sources

[1] Jean-Pierre Serre, “Homologie singulière des espaces fibrés. Applications,” *Annals of Mathematics*, 2nd Series, 54 (1951), 425–505.

[2] Allen Hatcher, *Spectral Sequences*, Chapter 5 of the online supplementary material for *Algebraic Topology*, Section 5.1, https://pi.math.cornell.edu/~hatcher/AT/ATch5.pdf.

[3] John McCleary, *A User's Guide to Spectral Sequences*, 2nd ed., Cambridge Studies in Advanced Mathematics 58, Cambridge University Press, 2001.
