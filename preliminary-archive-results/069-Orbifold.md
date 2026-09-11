# Mathematical Object Origin Archive | Orbifold

## 1. Archive Information

- Standard Name: Orbifold
- Mathematical Field: Differential Geometry
- Abstract: An orbifold is a space locally modeled not directly on Euclidean space, but on the quotient of a Euclidean domain by a finite group of smooth symmetries. It was formed to treat quotients by actions with finite stabilizers as differential-geometric objects while retaining the local isotropy data that an ordinary quotient space forgets.

## 2. Core Record

### Precise Description

An effective smooth orbifold of dimension \(n\) consists of a Hausdorff, paracompact underlying space \(|X|\) together with an equivalence class of compatible orbifold atlases. A chart over an open set \(U\subset |X|\) is a triple
\[
(\widetilde U,G,\phi),
\]
where \(\widetilde U\subset \mathbb R^n\) is open, \(G\) is a finite group acting effectively on \(\widetilde U\) by smooth diffeomorphisms, and \(\phi:\widetilde U\to U\) is \(G\)-invariant and induces a homeomorphism \(\widetilde U/G\cong U\). Charts are required to admit compatible local refinements on overlaps: changes of charts lift to smooth embeddings between the covering domains, equivariant with respect to injective homomorphisms between the relevant finite groups. Two atlases define the same orbifold when they have a common refinement.

For \(x\in |X|\), the stabilizer of a lift \(\widetilde x\) in a chart is well defined up to isomorphism and is called the isotropy group \(G_x\). Points with trivial isotropy form the regular locus; nontrivial \(G_x\) records a quotient singularity. Definitions allowing non-effective actions retain an additional ineffective kernel, but the effective convention above is sufficient for the motivating quotient problem [3].

### Mathematical Context and Formation

The motivating problem class is to do differential geometry on orbit spaces \(M/\Gamma\) when a discrete group acts properly on a smooth manifold \(M\) with finite, but not necessarily trivial, stabilizers. If the action is free, the projection \(M\to M/\Gamma\) is locally a covering and the quotient inherits an ordinary manifold structure. At a point fixed by a nontrivial finite subgroup, however, the projection is not locally a diffeomorphism: a neighborhood in the quotient has the form \(\widetilde U/G_x\), not an unambiguous Euclidean coordinate neighborhood.

Replacing the orbit space by only its underlying topological space does not solve this difficulty. For example, the quotient of \(\mathbb R^2\) by a cyclic rotation group of order \(m\) is homeomorphic to \(\mathbb R^2\), so the topological space cannot record \(m\). Yet the quotient-smooth functions are precisely the invariant smooth functions upstairs, and geometric calculations near the fixed point depend on the stabilizer. Treating the image merely as an unspecified singular space also supplies neither lifted coordinate changes nor a rule for gluing invariant differential forms, metrics, or bundles.

The decisive formation principle was therefore to weaken the manifold-chart requirement in a controlled way: retain a smooth domain upstairs, permit a finite local symmetry group, and use its quotient only as the visible neighborhood. Equivariant lifted changes of charts preserve the differential information, while the finite group records the failure of the quotient map to be locally one-to-one. Satake's \(V\)-manifolds gave an early systematic formulation of this local finite-quotient structure, and Thurston's orbifold terminology and treatment made the same viewpoint central in geometric topology [1][2]. The mathematical content of the formation is the replacement
\[
\text{Euclidean chart }\widetilde U \longrightarrow U
\quad\text{by}\quad
\text{finite quotient chart }\widetilde U/G \cong U,
\]
which is exactly the relaxation needed for proper actions with finite isotropy.

### Essential Role

The orbifold structure makes the differential-geometric part of the quotient problem tractable without either deleting fixed points or pretending that the orbit space is a manifold. A smooth function on an orbifold is specified locally by a \(G\)-invariant smooth function on \(\widetilde U\); differential forms are invariant forms upstairs; and vector bundles use compatible equivariant bundles over the chart domains. Because chart transitions lift smoothly and equivariantly, these local objects can be differentiated and glued. Thus the obstruction caused by the absence of ordinary coordinates at fixed orbits is bypassed by performing calculus before taking the finite quotient.

The finite group in each chart also restores information lost by the coarse space. It distinguishes, for instance, cone points of different orders even when their underlying neighborhoods are homeomorphic. Local integration can be normalized by the factor \(1/|G|\) on an effective chart, so that global quotient geometry carries the multiplicities forced by isotropy rather than counting every lift as a distinct point [3]. In this way the same two defining features—smooth local covers and recorded finite group actions—address both defects of the coarse quotient: loss of differential coordinates and loss of stabilizer data.

The resulting structural viewpoint is more specific than the generic claim that orbifolds are useful singular spaces. It identifies quotients with finite isotropy as objects that are still locally smooth *with symmetry*: their singularities are controlled by finite group actions, and ordinary manifold constructions extend by invariant and equivariant descent. That is the orbifold's direct contribution to the motivating quotient problem; applications to moduli spaces, three-dimensional geometrization, and string theory are later uses rather than the reason needed here.

## 3. Notes

An orbifold should not be identified with its coarse underlying topological space. Modern equivalent presentations include proper étale Lie groupoids, with suitable notions of equivalence, and differentiable stacks; these presentations make the retained isotropy especially explicit. Orbifolds also form a narrower class than arbitrary singular spaces because every point must possess a local finite-quotient model.

## 4. Sources

[1] I. Satake, “On a Generalization of the Notion of Manifold,” *Proceedings of the National Academy of Sciences of the United States of America* 42 (1956), 359–363. https://doi.org/10.1073/pnas.42.6.359

[2] W. P. Thurston, *The Geometry and Topology of Three-Manifolds*, Princeton lecture notes, 1978–1981, Chapter 13, “Orbifolds.” http://library.msri.org/books/gt3m/

[3] A. Adem, J. Leida, and Y. Ruan, *Orbifolds and Stringy Topology*, Cambridge Tracts in Mathematics 171, Cambridge University Press, 2007, Chapters 1–2. https://doi.org/10.1017/CBO9780511543081
