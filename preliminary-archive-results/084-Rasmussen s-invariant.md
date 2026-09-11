# Mathematical Object Origin Archive | Rasmussen s-invariant

## 1. Archive Information

- Standard Name: Rasmussen s-invariant
- Mathematical Field: Knot Theory and Low-Dimensional Topology
- Abstract: The Rasmussen s-invariant is an integer-valued invariant of an oriented knot, extracted from the quantum filtration on Lee's deformation of the Khovanov chain complex. It was formed to turn combinatorial link-homology data into an effective obstruction to low-genus smooth surfaces in the four-ball. Its defining filtration levels transform predictably under knot cobordisms, giving the bound \(|s(K)|\leq 2g_4(K)\) and, for positive torus knots, the exact value needed to determine their smooth slice genus.

## 2. Core Record

### Precise Description

Let \(K\subset S^3\) be an oriented knot and work over \(\mathbb{Q}\). Lee's deformation \(C_{\mathrm{Lee}}(K)\) of the Khovanov cochain complex has a differential that is not homogeneous in the Khovanov quantum grading \(q\), but it preserves the decreasing quantum filtration
\[
F^jC_{\mathrm{Lee}}(K)=\{x:q(x)\geq j\},
\]
where for a nonhomogeneous chain \(x\), \(q(x)\) is the least quantum degree among its nonzero homogeneous summands. Thus Lee homology \(H_{\mathrm{Lee}}(K;\mathbb{Q})\) inherits a filtration. For a nonzero homology class \(\alpha\), define its filtration degree by
\[
q(\alpha)=\max\{j:\alpha\text{ lies in the image of }H^*(F^jC_{\mathrm{Lee}}(K))\to H^*(C_{\mathrm{Lee}}(K))\}.
\]
Equivalently, \(q(\alpha)\) is the greatest filtration level attained by any cycle representing \(\alpha\).

For a knot, Lee homology is two-dimensional and is canonically associated with the two orientations of the underlying knot. Set
\[
s_{\min}(K)=\min_{0\ne\alpha\in H_{\mathrm{Lee}}(K)}q(\alpha),\qquad
s_{\max}(K)=\max_{0\ne\alpha\in H_{\mathrm{Lee}}(K)}q(\alpha).
\]
Rasmussen proved that \(s_{\max}(K)=s_{\min}(K)+2\). The **Rasmussen s-invariant** is therefore
\[
s(K)=\frac{s_{\min}(K)+s_{\max}(K)}2
     =s_{\min}(K)+1=s_{\max}(K)-1\in\mathbb Z.
\]
With the standard normalization, \(s(U)=0\) for the unknot \(U\). It is a smooth-concordance invariant; moreover, \(s(K\#K')=s(K)+s(K')\) and \(s(\overline K)=-s(K)\), where \(\overline K\) denotes the mirror with reversed orientation convention as appropriate [1].

### Mathematical Context and Formation

The concrete problem class was to bound, and where possible determine, the smooth slice genus
\[
g_4(K)=\min\{g(\Sigma):\Sigma\subset B^4\text{ is a smooth, connected, oriented surface with }\partial\Sigma=K\}.
\]
A decisive benchmark was the torus-knot genus problem: for coprime positive integers \(p,q\), prove
\[
g_4(T_{p,q})=\frac{(p-1)(q-1)}2.
\]
The upper bound comes from the standard Seifert surface, but obtaining the matching lower bound is genuinely four-dimensional. Classical numerical obstructions such as the knot signature do not give this value uniformly for all positive torus knots, while the earlier proof of the equality used gauge theory. The desired route was a combinatorial one based on a knot diagram [1].

Khovanov homology supplied diagrammatically defined bigraded groups categorifying the Jones polynomial [3], but the slice-genus problem requires information that behaves quantitatively under a surface cobordism, not merely a collection of groups attached to its boundary. Lee's modified differential provided the needed intermediate structure: it destroys the separate quantum grading but retains it as a filtration, and its homology for a knot collapses to two canonical orientation classes [2]. This combination resolves two opposing requirements. The small terminal homology isolates distinguished surviving classes, while the retained filtration remembers how far those classes sit in the original quantum grading.

Rasmussen's formation of \(s(K)\) consists precisely in measuring the two extremal filtration positions of this two-dimensional Lee homology and taking their midpoint [1]. The fact that the extrema differ by two makes the midpoint a single integer rather than an interval. This was not simply a repackaging of the Jones polynomial or of unfiltered Lee homology: forgetting the filtration would leave only a two-dimensional vector space for every knot and hence no genus information. The interpretive synthesis is that the object was engineered as a numerical interface between diagrammatic homological algebra and the Euler-characteristic cost of a smooth cobordism; the definitions and theorems supporting that interpretation are established in [1,2].

### Essential Role

An oriented knot cobordism \(S\subset S^3\times[0,1]\) induces a map on Lee homology whose filtration shift is controlled by \(\chi(S)\). For a connected genus-\(g\) cobordism between two knots, \(\chi(S)=-2g\), and the induced map acts nontrivially on the canonical orientation classes. Comparing their extremal filtration levels gives
\[
|s(K_1)-s(K_0)|\leq 2g.
\]
If a genus-\(g\) surface in \(B^4\) bounds \(K\), removing a disk turns it into a genus-\(g\) cobordism from \(K\) to the unknot. Since \(s(U)=0\), one obtains
\[
|s(K)|\leq 2g_4(K).
\]
Thus the exact difficulty made tractable is the lower-bound half of a smooth slice-genus computation: the filtration converts every proposed bounding surface into a numerical inequality [1].

For a knot admitting a positive diagram \(D\), Rasmussen's calculation gives
\[
s(K)=n(D)-O(D)+1=2g(D),
\]
where \(n(D)\) is the number of crossings, \(O(D)\) the number of Seifert circles, and \(g(D)\) the genus of the Seifert surface produced by Seifert's algorithm [1]. The standard positive diagram of \(T_{p,q}\), obtained from the closure of \((\sigma_1\cdots\sigma_{p-1})^q\), has \(n=q(p-1)\) and \(O=p\). Hence
\[
s(T_{p,q})=(p-1)(q-1).
\]
The cobordism inequality supplies
\(g_4(T_{p,q})\geq (p-1)(q-1)/2\), while the standard Seifert surface supplies the reverse inequality. In this benchmark problem, the object therefore gives exactly the missing lower bound and yields a combinatorial proof of the torus-knot slice-genus formula [1].

The deeper structural viewpoint is that smooth genus is detected not by the rank of a homology theory but by the persistence of selected classes through a grading filtration. The two-class structure of Lee homology makes the invariant canonical; the two-step separation makes it integer-valued; and filtered cobordism maps make it sensitive to four-dimensional genus. These are the specific features that allow \(s\) to overcome the inadequacy of unfiltered Lee homology and to sharpen classical genus bounds.

## 3. Notes

- The Rasmussen s-invariant is not Lee homology itself and not the Lee spectral sequence. It is the integer extracted from the induced quantum filtration on Lee homology.
- The definition above uses the original rational Lee deformation and Rasmussen's normalization. Variants over other coefficient systems require care and need not reproduce every property in exactly the same form.
- The symbol \(s\) is also used for extensions to links and for invariants arising from other deformed Khovanov-type theories; those are distinct objects and are outside this archive.

## 4. Sources

[1] Jacob Rasmussen, “Khovanov Homology and the Slice Genus,” *Inventiones Mathematicae* **182** (2010), 419–447, doi:10.1007/s00222-010-0275-6; preprint arXiv:math/0402131, https://arxiv.org/abs/math/0402131.

[2] Eun Soo Lee, “An Endomorphism of the Khovanov Invariant,” *Advances in Mathematics* **197** (2005), no. 2, 554–586, doi:10.1016/j.aim.2004.10.015; preprint arXiv:math/0210213, https://arxiv.org/abs/math/0210213.

[3] Mikhail Khovanov, “A Categorification of the Jones Polynomial,” *Duke Mathematical Journal* **101** (2000), no. 3, 359–426, doi:10.1215/S0012-7094-00-10131-7.
