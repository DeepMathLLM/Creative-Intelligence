# Mathematical Object Origin Archive | Reidemeister Torsion

## 1. Archive Information

- Standard Name: Reidemeister torsion (also Reidemeister–Franz torsion)
- Mathematical Field: Algebraic Topology
- Abstract: Reidemeister torsion is a determinant-valued invariant extracted from a finite based chain complex, classically from the cellular chain complex of a covering space after a coefficient representation makes it acyclic. It arose in the combinatorial classification of lens spaces, where ordinary homology and homotopy data failed to retain enough information about the gluing parameter. Torsion preserves determinant-level information in the boundary operators and thereby distinguishes, and helps classify, lens spaces that coarser invariants cannot separate.

## 2. Core Record

### Precise Description

Let
\[
0\longrightarrow C_n\xrightarrow{\partial_n}C_{n-1}\longrightarrow\cdots\longrightarrow C_0\longrightarrow0
\]
be a finite acyclic chain complex of finite-dimensional vector spaces over a field \(F\), with an ordered basis \(c_i\) of each \(C_i\). Put \(B_i=\operatorname{im}(\partial_{i+1})\). Choose a basis \(b_i\) of \(B_i\), and choose lifts \(\widetilde b_{i-1}\subset C_i\) of \(b_{i-1}\) under \(\partial_i\). Acyclicity gives short exact sequences
\[
0\longrightarrow B_i\longrightarrow C_i\xrightarrow{\partial_i}B_{i-1}\longrightarrow0,
\]
so the concatenation \((b_i,\widetilde b_{i-1})\) is a basis of \(C_i\). If \([u/c_i]\) denotes the determinant of the change-of-basis matrix expressing a basis \(u\) in the basis \(c_i\), one standard convention defines
\[
\tau(C_*,c_*)=
\prod_{i=0}^{n}[\,b_i,\widetilde b_{i-1}/c_i\,]^{(-1)^{i+1}}\in F^\times.
\]
The arbitrary choices of the \(b_i\) and their lifts cancel in this alternating product. Some authors use the reciprocal convention; statements comparing torsions must therefore fix a convention [2,3].

For a finite connected CW complex \(X\) and a representation \(\rho:\pi_1(X)\to\operatorname{GL}(V)\) over \(F\), the cellular chains of the universal cover can be combined with \(V\) to form a twisted complex
\[
C_*^\rho(X;V)=C_*(\widetilde X)\otimes_{\mathbb Z[\pi_1(X)]}V,
\]
with the usual compatible choice of left/right module conventions. Lifts, orientations, and orderings of the cells induce bases. When this twisted complex is acyclic, its algebraic torsion defines the Reidemeister torsion \(\tau_\rho(X)\). Changing cellular lifts and orientations produces the standard indeterminacy; for a one-dimensional character \(\rho\), the value is naturally considered modulo factors \(\pm\rho(g)\), \(g\in\pi_1(X)\). Subdivision invariance makes the resulting class a combinatorial invariant [2,3].

### Mathematical Context and Formation

The motivating problem was to classify three-dimensional lens spaces
\[
L(p,q)=S^3/((z_1,z_2)\sim(\zeta z_1,\zeta^qz_2)),
\qquad \zeta=e^{2\pi i/p},\quad \gcd(p,q)=1,
\]
up to combinatorial equivalence, now called PL homeomorphism. For fixed \(p\), the readily computed invariants are largely insensitive to \(q\): every such space has fundamental group \(\mathbb Z/p\), integral homology
\[
H_0\cong H_3\cong\mathbb Z,\qquad H_1\cong\mathbb Z/p,\qquad H_2=0,
\]
and universal cover \(S^3\), hence the same higher homotopy groups. These data therefore could not decide when two different quotient actions, or equivalently their gluing parameters, produced the same lens space. The insufficiency is stronger than a failure of homology alone: examples such as \(L(7,1)\) and \(L(7,2)\) are homotopy equivalent but not homeomorphic [3,4].

The cellular chain complex over \(\mathbb Z\) had already discarded the needed information. It is obtained from the equivariant cellular complex of \(\widetilde L=S^3\), whose boundary matrices lie in \(\mathbb Z[\mathbb Z/p]\), by the augmentation sending the deck generator \(t\) to \(1\). That specialization retains ranks, kernels, and quotient groups but erases how powers of \(t\), and therefore \(q\), occur in the boundary operators. Merely taking the homology of the equivariant or twisted complex again discards the matrices once their kernels and images have been recorded.

The decisive idea was instead to retain determinant information from a *based* cellular complex. For a nontrivial character \(t\mapsto\eta\), where \(\eta^p=1\) and \(\eta\ne1\), the corresponding complex over \(\mathbb C\) becomes acyclic. Exactness then identifies every chain group as boundaries together with lifts of boundaries one degree lower. Comparing those exactness-adapted bases with the bases supplied by lifted cells gives determinants, and their alternating product cancels the auxiliary splittings while preserving information in the actual boundary matrices. Reidemeister introduced this construction in 1935 for the combinatorial classification of three-dimensional lens spaces; Franz generalized it to higher-dimensional lens spaces [1,3].

### Essential Role

For \(L(p,q)\), let \(r\) satisfy \(qr\equiv1\pmod p\), and evaluate the equivariant cellular boundary maps at a nontrivial character \(t\mapsto\eta\). With the convention above, the resulting torsion has the form
\[
\tau_\eta(L(p,q))=((\eta-1)(\eta^r-1))^{-1}
\quad\text{in}\quad
\mathbb C^\times/\{\pm\eta^j:j\in\mathbb Z\}
\]
(up to the reciprocal if the opposite torsion convention is used) [4]. Unlike integral homology, this expression still contains the parameter \(r=q^{-1}\bmod p\). Thus the classification problem is converted from comparing cell structures or quotient actions directly into comparing explicit cyclotomic products for all relevant characters, allowing also for the automorphisms of \(\pi_1(L(p,q))\).

This is precisely the part of the lens-space problem that torsion made tractable. Acyclic twisting removes homology groups from the calculation, but exactness does not make the based complex featureless: the alternating determinant records how its boundary isomorphisms sit relative to the cellular bases. Franz's independence lemma then turns equality of these cyclotomic torsions into the congruence restrictions on lens-space parameters needed for classification [4,5]. In particular, torsion can obstruct a homotopy equivalence from being represented by the elementary combinatorial changes associated with a homeomorphism and separates pairs such as \(L(7,1)\) and \(L(7,2)\) [3,4].

The structural viewpoint introduced here is that an exact based chain complex carries multiplicative information beyond its zero homology. Reidemeister torsion is therefore a determinant-level refinement of the information retained by homology, not another homology group. Its original contribution was this recovery of the gluing information lost under augmentation and passage to homology; its later connections with simple homotopy theory, Whitehead torsion, and analytic torsion are developments of that mechanism rather than the motivating role itself [2].

## 3. Notes

- Reidemeister torsion is not, in general, an invariant of ordinary homotopy type. Its finer sensitivity is exactly why it can distinguish homotopy-equivalent lens spaces. It is invariant under simple homotopy equivalence, subject to the usual coefficient and indeterminacy conventions [2].
- Whitehead torsion is a related but distinct object: it assigns to a homotopy equivalence an obstruction to being simple. Reidemeister torsion assigns determinant data to a based (often twisted and acyclic) chain complex or to a space equipped with the corresponding coefficient data.
- If the twisted complex is not acyclic, torsion requires additional homology bases or, in modern language, is naturally placed in an appropriate determinant line. The acyclic form above is the one directly suited to the lens-space origin problem [5].

## 4. Sources

[1] K. Reidemeister, “Homotopieringe und Linsenräume,” *Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg* 11 (1935), 102–109.

[2] J. Milnor, “Whitehead torsion,” *Bulletin of the American Mathematical Society* 72 (1966), 358–426.

[3] A. Ranicki, *Notes on Reidemeister Torsion* (2001), https://webhomes.maths.ed.ac.uk/~v1ranick/papers/torsion.pdf.

[4] P. Mnev, “Lecture Notes on Torsions,” arXiv:1406.3705 (2014), https://arxiv.org/abs/1406.3705.

[5] V. Turaev, *Introduction to Combinatorial Torsions*, Lectures in Mathematics ETH Zürich, Birkhäuser, 2001.
