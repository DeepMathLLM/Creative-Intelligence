# Mathematical Object Origin Archive | Perverse Sheaf

## 1. Archive Information

- Standard Name: Perverse sheaf (middle perversity)
- Mathematical Field: Algebraic Topology; Algebraic Geometry
- Abstract: A middle-perversity perverse sheaf on a complex algebraic variety is a constructible complex whose stalk behavior and Verdier-dual stalk behavior are bounded according to the complex dimensions of their supports. The resulting objects form an abelian, Verdier-self-dual heart inside the constructible derived category. This structure was formed to treat intersection-cohomology complexes on singular spaces as degree-zero coefficient objects and, in particular, to make their canonical minimal extension across singular strata expressible by an image.

## 2. Core Record

### Precise Description

Let $X$ be a complex algebraic variety, let $k$ be a field, and let $D_c^b(X;k)$ be the bounded derived category of sheaves of $k$-vector spaces whose cohomology sheaves are constructible with respect to an algebraic stratification. Write $\mathbb D_X$ for Verdier duality. A complex $K\in D_c^b(X;k)$ is a **middle-perversity perverse sheaf** if, for every $i\in\mathbb Z$,

\[
\dim_{\mathbb C}\operatorname{Supp}\mathcal H^i(K)\le -i
\quad\text{and}\quad
\dim_{\mathbb C}\operatorname{Supp}\mathcal H^i(\mathbb D_XK)\le -i,
\]

with the empty support assigned dimension $-\infty$. The first inequalities are the support conditions and the second are the cosupport conditions. Equivalently, the two families define the nonpositive and nonnegative halves of the middle perverse $t$-structure, and their intersection

\[
\operatorname{Perv}(X;k)={}^{p}D^{\le 0}_c(X;k)\cap{}^{p}D^{\ge 0}_c(X;k)
\]

is its heart. Consequently $\operatorname{Perv}(X;k)$ is an abelian category, although its objects are generally complexes rather than sheaves concentrated in ordinary degree zero; Verdier duality restricts to a contravariant equivalence of this heart [1,2]. If $X$ is smooth of pure complex dimension $n$ and $L$ is a local system on $X$, then $L[n]$ is perverse, which fixes the normalization.

For an open immersion $j:U\hookrightarrow X$ and $P\in\operatorname{Perv}(U;k)$, the perverse intermediate extension is the image formed in this abelian heart,

\[
j_{!*}P
=
\operatorname{im}_{\operatorname{Perv}(X;k)}
\left({}^{p}\!\mathcal H^0(Rj_!P)\longrightarrow{}^{p}\!\mathcal H^0(Rj_*P)\right).
\]

When $U$ is smooth and dense of pure dimension $n$ and $P=L[n]$, the complex $j_{!*}(L[n])$ is the intersection complex $IC_X(L)$ in perverse normalization [1,2].

### Mathematical Context and Formation

The motivating problem class is the following: given a local system $L$ on the smooth part $j:U\hookrightarrow X$ of a singular complex variety, extend its Poincaré-duality-type cohomological information canonically over the singular strata, while retaining exact algebraic operations on such extensions. Ordinary cohomology of $X$ is sensitive to singularities in the wrong way for this purpose: it need not satisfy the manifold form of Poincaré duality. Intersection cohomology corrects this by imposing dimension-dependent restrictions near singular strata, but its sheaf representative $IC_X(L)$ is generally a complex with nonzero ordinary cohomology sheaves in several degrees rather than an ordinary sheaf [2,3].

Neither of the two evident extensions supplies the required object. The extension $Rj_!L[n]$ is forced to vanish toward the boundary, while $Rj_*L[n]$ admits all derived sections approaching it; they are opposite extremes, and the desired intersection complex lies between them. In the constructible derived category there is a natural morphism $Rj_!L[n]\to Rj_*L[n]$, but a triangulated category has no intrinsic abelian image with which to select the middle extension. Moving to the ordinary heart does not solve this: $IC_X(L)$ does not usually lie in that heart, and Verdier duality does not preserve ordinary sheaves, so imposing only stalk-side bounds would lose the dual local restrictions responsible for Poincaré duality.

The formative insight is to alter which complexes count as degree zero. Complex codimension dictates how far nonzero local cohomology may extend: the support inequalities bound stalk-side contributions, and the same inequalities after Verdier duality impose the complementary costalk-side bounds. Their balanced intersection is the perverse heart. The shift $L[n]$ on a smooth $n$-fold and the intersection complex on a singular variety both then lie in degree zero, Verdier duality preserves the heart, and the heart is abelian. Thus the local conditions already present in intersection cohomology become the axioms defining a new kind of coefficient object rather than exceptional properties of one complex [1–3].

### Essential Role

The perverse sheaf makes the previously unavailable “middle” extension mathematically tractable. For $P=L[n]$ on $U$, one may now take the actual abelian image of the boundary-to-direct-extension morphism in $\operatorname{Perv}(X;k)$; this produces $j_{!*}P$. It is characterized among perverse extensions of $P$ by having no nonzero subobject and no nonzero quotient supported on $X\setminus U$ [1,2]. Hence it includes the local information forced by continuation from $U$ but excludes independent classes living only on the singular boundary. This precise exclusion is what neither $Rj_!$ nor $Rj_*$ accomplishes alone.

The mechanism comes directly from the definition. The support condition prevents cohomology in a given degree from spreading over strata that are too large, while the dual cosupport condition imposes the corresponding restriction on compactly supported local, or costalk, behavior. Because Verdier duality exchanges these two conditions, the construction preserves the dual balance required by middle intersection cohomology. In particular,

\[
IC_X(L)=j_{!*}(L[n])
\]

is now a degree-zero object in an abelian category, and its hypercohomology recovers intersection cohomology (with the chosen normalization) [2,3]. Kernels, cokernels, images, extensions, and simple constituents of intersection complexes can therefore be handled inside one exact category rather than only through noncanonical cone manipulations in a triangulated category.

The direct contribution of the object is thus not merely that it supplies another cohomology theory. It reformulates the codimension restrictions needed at singular strata as a self-dual $t$-structure. That reformulation simultaneously makes the canonical minimal extension definable, explains why intersection complexes behave like shifted local systems on singular spaces, and provides the exact-category operations required to organize them.

## 3. Notes

“Perverse” does not mean pathological. It records a nonstandard, dimension-dependent choice of degree. The archive uses the middle perversity on complex algebraic varieties and field coefficients; more general perversity functions, coefficient rings, and suitably stratified topological spaces require corresponding modifications. A perverse sheaf is distinct from its hypercohomology groups and from the intersection homology groups represented by the special perverse sheaf $IC_X(L)$.

## 4. Sources

[1] A. A. Beilinson, J. Bernstein, and P. Deligne, “Faisceaux pervers,” in *Analyse et topologie sur les espaces singuliers, I*, Astérisque **100** (1982), 5–171.

[2] M. Goresky, *Lecture Notes on Sheaves and Perverse Sheaves*, especially the sections on support/cosupport conditions, perverse $t$-structures, and intersection complexes, https://www.math.ias.edu/~goresky/pdf/all.pdf.

[3] M. A. A. de Cataldo and L. Migliorini, “The Decomposition Theorem, Perverse Sheaves and the Topology of Algebraic Maps,” *Bulletin of the American Mathematical Society* **46** (2009), 535–633, https://doi.org/10.1090/S0273-0979-09-01246-9.
