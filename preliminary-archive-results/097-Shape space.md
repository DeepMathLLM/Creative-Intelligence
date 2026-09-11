# Mathematical Object Origin Archive | Shape space

## 1. Archive Information

- Standard Name: Shape space (Kendall shape space of landmark configurations)
- Mathematical Field: Differential Geometry; Statistical Shape Analysis
- Abstract: A Kendall shape space is the quotient space whose points are labeled landmark configurations modulo translation, positive uniform scaling, and rotation. It was formed to give statistical comparison of geometric shape an intrinsic sample space in which nuisance pose and size have been removed without discarding the remaining joint geometry.

## 2. Core Record

### Precise Description

Let \(m\ge 2\), \(k\ge 2\), and let a noncoincident configuration of \(k\) labeled landmarks in \(\mathbb{R}^m\) be represented by a matrix \(X\in\mathbb{R}^{m\times k}\), with one landmark in each column. Put
\[
C=I_k-\frac1k\mathbf 1\mathbf 1^{\mathsf T}.
\]
The centered configuration is \(XC\). Its *pre-shape* is
\[
Z=\frac{XC}{\lVert XC\rVert_F},
\]
so all translation and positive uniform scale information has been removed. The pre-shapes form the sphere
\[
S_m^k=\{Z\in\mathbb{R}^{m\times k}:Z\mathbf 1=0,\ \lVert Z\rVert_F=1\}
\cong S^{m(k-1)-1}.
\]
Rotations act on this sphere by \(Z\mapsto RZ\), with \(R\in SO(m)\). The Kendall shape space is the orbit space
\[
\Sigma_m^k=S_m^k/SO(m),
\qquad [Z]=\{RZ:R\in SO(m)\}.
\]
Thus one point of \(\Sigma_m^k\) is one similarity shape, not one chosen pose of it. The spherical metric on pre-shape space induces the angular Procrustes quotient metric
\[
\rho([Z],[W])
=\min_{R\in SO(m)}\arccos\langle RZ,W\rangle_F
=\arccos\!\left(\max_{R\in SO(m)}\langle RZ,W\rangle_F\right).
\]
The use of \(SO(m)\), rather than \(O(m)\), means that reflection equivalence is not imposed. In particular, a full-rank configuration and its image under an improper orthogonal map occupy distinct \(SO(m)\)-orbits. For a rank-deficient configuration, however, an improper map on \(\mathbb{R}^m\) can restrict to the same action on the configuration's span as some element of \(SO(m)\), so a reflected representative need not define a distinct orbit.

For planar configurations, centered pre-shapes may be represented as unit vectors in \(\mathbb{C}^{k-1}\), and planar rotations act by multiplication by \(S^1\). Consequently
\[
\Sigma_2^k\cong S^{2k-3}/S^1\cong\mathbb{CP}^{k-2}.
\]
In particular, the shape space of labeled planar triangles is \(\mathbb{CP}^1\), hence a two-sphere with the appropriately scaled quotient metric [1,3].

### Mathematical Context and Formation

The motivating problem class is the statistical comparison of objects recorded as corresponding landmark configurations—triangles, anatomical outlines, or other figures—when only shape is relevant. Two observations can have identical shape while their coordinate matrices differ because one has been translated, rotated, or uniformly enlarged. Raw Euclidean coordinate differences therefore confound the variable of interest with nuisance transformations. Conversely, reducing a configuration to selected lengths, angles, or ratios can remove nuisance information but may discard part of the joint landmark geometry [1,2].

Pairwise superposition methods align two configurations, but a statistical theory also needs a single sample space containing *all* possible shapes, together with distances that do not depend on a selected baseline, orientation, or reference specimen. Treating aligned coordinates as ordinary vectors is inadequate globally: the removal of rotation is not a linear constraint, different representatives of the same shape remain possible, and the resulting space is generally curved rather than Euclidean. Thus ordinary linear averaging or inference has no intrinsic justification for dispersed shape data [1,2].

The forming insight was to express nuisance removal as successive geometric operations. Centering projects away translations; normalization places the result on a unit pre-shape sphere and removes positive scale; quotienting that sphere by the rotation group identifies exactly the remaining coordinate representatives of one oriented similarity shape. The Procrustes comparison is then the shortest spherical separation between the two rotation orbits. This turns “shape after alignment” into a well-defined quotient object. In the planar case, recognizing rotation as scalar \(S^1\)-action identifies the quotient with complex projective space, exposing its global non-Euclidean geometry [1].

### Essential Role

The shape space made the central invariance problem tractable by replacing each entire family of translated, scaled, and rotated coordinate matrices with one orbit \([Z]\). This gives an exact criterion for sameness under orientation-preserving similarity transformations and prevents nuisance pose or size from entering the variable being analyzed. Its quotient metric makes comparison intrinsic: minimizing over \(SO(m)\) selects the closest representatives, while the resulting distance belongs to the orbits and is independent of any arbitrary alignment [1,2].

More importantly, the construction solved the global sample-space problem that pairwise fitting alone did not solve. Probability distributions, means, variability, regression, and tests can be formulated on \(\Sigma_m^k\) itself, with curvature taken into account rather than silently replacing shape data by unconstrained Euclidean coordinates. For planar landmarks, the identification \(\Sigma_2^k\cong\mathbb{CP}^{k-2}\) supplies explicit manifold geometry. For planar triangles it turns the full family of shapes into a sphere: noncollinear mirror mates occupy distinct points, while collinear configurations form the degenerate locus where that handedness distinction disappears [1,3]. The direct contribution is therefore not merely a new visualization: the sphere-and-quotient structure preserves the complete labeled-landmark configuration modulo orientation-preserving similarities and provides the mathematically correct domain for comparing and statistically modeling it.

## 3. Notes

“Shape space” here means Kendall's landmark-based similarity-shape space, not every space called a shape space in geometry or imaging. Landmarks are labeled and complete coincidence is excluded. Quotienting by \(SO(m)\) does not deliberately quotient by reflections, but full-rank is required for the blanket conclusion that a configuration and its mirror lie in different orbits. If reflection equivalence is required for every configuration, the relevant orbit space uses \(O(m)\).

The planar quotient \(\mathbb{CP}^{k-2}\) is a smooth manifold. In higher dimensions the geometry depends on \(k\), rank, and orbit type. When configurations of different ranks have different isotropy types, the quotient can be stratified rather than globally smooth; the mere existence of a nontrivial stabilizer does not by itself imply a singular quotient.

## 4. Sources

[1] D. G. Kendall, “Shape Manifolds, Procrustean Metrics, and Complex Projective Spaces,” *Bulletin of the London Mathematical Society* 16 (1984), 81–121. https://doi.org/10.1112/blms/16.2.81

[2] I. L. Dryden and K. V. Mardia, *Statistical Shape Analysis*, Wiley, 1998.

[3] S. F. Huckemann, “Intrinsic Inference on the Mean Geodesic of Planar Shapes and Tree Discrimination by Leaf Growth,” *The Annals of Statistics* 39 (2011), 1098–1124. https://doi.org/10.1214/10-AOS862
