# Mathematical Object Origin Archive | Martin Boundary

## 1. Archive Information

- Standard Name: Martin boundary
- Mathematical Field: Harmonic Analysis (Potential Theory)
- Abstract: The Martin boundary is an ideal boundary canonically constructed from normalized Green functions. It was formed to parameterize the positive harmonic functions on a general Greenian domain when ordinary Euclidean boundary points and classical Poisson formulas do not supply an adequate set of elementary positive harmonic functions. Its minimal part indexes the extremal building blocks in the unique Martin integral representation.

## 2. Core Record

### Precise Description

Let \(\Omega\subset \mathbb{R}^n\), \(n\ge 2\), be a Greenian domain with Green function \(G_\Omega\), and fix a reference point \(x_0\in\Omega\). For \(y\ne x_0\), normalize the Green function in its second variable by
\[
K_\Omega(x,y)=\frac{G_\Omega(x,y)}{G_\Omega(x_0,y)}.
\]
The **Martin compactification** \(\overline{\Omega}^{M}\) is the compactification induced by these normalized kernels: when \(y_j\) leaves every compact subset of \(\Omega\), convergence to an ideal point \(\xi\) is characterized by locally uniform convergence in \(x\) of \(K_\Omega(x,y_j)\) to a normalized positive harmonic function \(K_\Omega(x,\xi)\). The **Martin boundary** is
\[
\partial_M\Omega=\overline{\Omega}^{M}\setminus\Omega.
\]
Equivalent standard constructions specify the compactification by a metric or by the topology of kernel convergence; the resulting compactification is independent, up to canonical homeomorphism, of the auxiliary choices. Changing \(x_0\) only renormalizes the kernels and does not change the boundary as a canonical compactification [2,3].

A positive harmonic function \(u\) is *minimal* if \(0\le v\le u\) and \(v\) harmonic imply \(v=cu\) for some \(c\in[0,1]\). The minimal Martin boundary \(\partial_m\Omega\subseteq\partial_M\Omega\) consists of those \(\xi\) for which \(K_\Omega(x,\xi)\), as a function of \(x\), is minimal. The Martin representation theorem states that every positive harmonic function \(h\) on \(\Omega\) has a unique representation
\[
h(x)=\int_{\partial_m\Omega}K_\Omega(x,\xi)\,d\mu_h(\xi),
\]
where \(\mu_h\) is a finite positive measure; with the displayed normalization, \(\mu_h(\partial_m\Omega)=h(x_0)\) [1,2].

### Mathematical Context and Formation

The motivating problem was to describe the entire cone of positive harmonic functions on a general domain and, in particular, to identify its indecomposable or minimal elements. On the unit disk or unit ball, Poisson kernels attached to ordinary boundary points provide elementary positive harmonic functions, and every positive harmonic function can be recovered by integrating those kernels against a finite boundary measure. That model does not extend merely by retaining the Euclidean boundary. For irregular domains, different ways of approaching the same Euclidean boundary point can yield different limiting positive harmonic profiles; unbounded domains may also require ideal points at infinity. Thus geometric boundary location alone need not distinguish the extremal positive harmonic functions. Conversely, solving a Dirichlet problem for prescribed regular boundary data does not classify positive harmonic functions with singular boundary behavior or determine the extreme rays of their cone [1,3].

The decisive construction was to extract the needed boundary objects from potential theory inside the domain. A Green function with pole \(y\) already records the domain's geometry, but its scale changes as the pole moves and therefore raw Green functions do not have a useful common normalization. Dividing by the value at \(x_0\) puts all kernels on the slice \(K_\Omega(x_0,y)=1\). If \(y_j\) escapes every compact subset, the poles eventually lie outside each fixed compact set; the normalized kernels are then positive harmonic there. Harnack inequalities and compactness give locally convergent subsequences. Treating distinct limiting kernels as ideal boundary points produces \(\partial_M\Omega\), including distinctions that the Euclidean boundary may collapse. Selecting the limits that are minimal then matches the extremal rays required by the original representation problem [1,2].

### Essential Role

The Martin boundary makes the classification problem tractable by replacing an inadequate preassigned geometric boundary with one defined by the asymptotic behavior of the operator's own Green function. Its normalization removes scalar ambiguity and turns escaping poles into a relatively compact family of normalized positive functions; its kernel-convergence topology preserves every distinct limiting harmonic profile; and its minimal subset isolates precisely the profiles that cannot be decomposed into smaller positive harmonic functions.

These features yield the direct solution to the motivating problem: the minimal kernels are the elementary positive harmonic functions, and every positive harmonic function is reconstructed from them by the Martin integral, with a unique representing measure on \(\partial_m\Omega\). The construction therefore reformulates boundary representation as the decomposition of the normalized cone \(\{h>0:h(x_0)=1\}\) into its extreme elements. This is more than the addition of points at infinity: it supplies exactly the boundary needed by the cone of positive harmonic solutions, whether or not that boundary agrees with the Euclidean one. In regular classes such as bounded uniform domains the two boundaries can be homeomorphic, whereas in general a single Euclidean boundary point may correspond to multiple Martin points [3].

## 3. Notes

The full Martin boundary and the minimal Martin boundary are not synonymous. The full boundary is the ideal boundary of the compactification; only its minimal part is required as the support of the unique representing measure. The object is also distinct from the Poisson boundary: in probabilistic potential theory the two are related, but they encode different representation and boundary notions. Variants replace the Laplacian and its Green function by kernels for Markov chains, diffusions, elliptic operators, or parabolic equations; those are extensions of the same structural construction, not part of the present definition.

## 4. Sources

[1] R. S. Martin, “Minimal Positive Harmonic Functions,” *Transactions of the American Mathematical Society* **49** (1941), 137–172.

[2] J. L. Doob, *Classical Potential Theory and Its Probabilistic Counterpart*, Grundlehren der mathematischen Wissenschaften 262, Springer, 1984, Chapters XI–XII.

[3] K. Hirata, “Martin Kernels of General Domains,” in *Potential Theory in Matsue*, Advanced Studies in Pure Mathematics 44, Mathematical Society of Japan, 2006, 145–160, https://projecteuclid.org/ebooks/advanced-studies-in-pure-mathematics/Potential-Theory-in-Matsue/chapter/Martin-kernels-of-general-domains/10.2969/aspm/04410145.
