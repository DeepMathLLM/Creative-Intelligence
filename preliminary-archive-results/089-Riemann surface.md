# Mathematical Object Origin Archive | Riemann Surface

## 1. Archive Information

- Standard Name: Riemann surface
- Mathematical Field: Complex Analysis
- Abstract: A Riemann surface is a one-complex-dimensional manifold. Its formative role was to provide a natural domain on which the locally holomorphic branches of an algebraic function, an inverse function, or an analytically continued integral become parts of one globally single-valued holomorphic or meromorphic function. The surface records a base value together with a choice of analytic branch, and its topology records how those branches are permuted by continuation.

## 2. Core Record

### Precise Description

A **Riemann surface** is a connected Hausdorff, second-countable topological space \(X\) equipped with an atlas of homeomorphisms \(\phi_i:U_i\to V_i\subset\mathbb C\) such that every transition map
\[
\phi_j\circ\phi_i^{-1}:\phi_i(U_i\cap U_j)\longrightarrow \phi_j(U_i\cap U_j)
\]
is holomorphic wherever defined. Two compatible atlases determine the same complex structure; equivalently, a Riemann surface is a connected complex manifold of complex dimension one [3].

When the surface represents the branches of a relation between variables, it carries additional data, usually a holomorphic projection \(\pi:X\to D\) to a plane domain or to the Riemann sphere and a holomorphic or meromorphic function \(F\) on \(X\). Thus the Riemann surface itself should not be confused with the chosen projection. For an algebraic relation \(P(z,w)=0\), one seeks \(\pi\) and \(F\) satisfying
\[
P\bigl(\pi(p),F(p)\bigr)=0\qquad(p\in X).
\]
Away from exceptional values, \(\pi\) is locally biholomorphic and its fiber lists the local branches. At a ramification point there are local coordinates \(t\) on \(X\) and \(z\) on the base in which \(\pi\) has the form \(z=t^e\), with \(e>1\).

For example,
\[
X=\{(z,w)\in\mathbb C^2:w^2=z\}
\]
is a Riemann surface, with global coordinate \(w\), projection \(\pi(z,w)=z\), and single-valued holomorphic function \(F(z,w)=w\). The two plane values conventionally denoted \(\pm\sqrt z\) are different points over the same nonzero \(z\). At \((0,0)\), the coordinate \(w\) gives \(\pi=w^2\), so the apparent branch point in the base is an ordinary point of the surface at which the projection ramifies.

### Mathematical Context and Formation

The motivating problem class was the global treatment of quantities defined locally by holomorphic continuation but not representable by one-valued functions of the plane variable. Algebraic equations such as \(w^2=z\), local inverses, \(\log z\), and integrals whose values change after continuation around singular points all produce valid local analytic elements. The obstruction is global: continuation of an element around a closed loop can return a different element. For \(w^2=z\), continuation once around \(0\) interchanges the two roots; for a logarithm it changes the value by \(2\pi i\). This branch permutation is now described as monodromy.

An ordinary function on a domain in \(\mathbb C\) must assign exactly one value to each argument. Deleting a cut and choosing a branch can enforce that condition on a smaller domain, but it does not retain all continuations at once; moreover, the answer depends on an auxiliary cut, and loops responsible for the obstruction have been removed rather than represented. Treating the values merely as an unordered finite set is also inadequate for complex analysis, because differentiation, integration, and continuation concern a locally chosen analytic element and its passage into another branch, not only the set of values at an isolated base point.

The decisive geometric idea is to change the domain. One replaces a base point \(z\) by points \(p\) encoding both \(z\) and a local branch, arranges such points in sheets, and glues the sheets according to analytic continuation. Continuation that changes a value in the plane then moves to a different point of the new space instead of making a function ambiguous. Near coalescing algebraic branches, the sheets are joined with a ramified local model such as \(z=t^e\). Compatible local complex coordinates make the resulting space itself a domain for complex analysis. Riemann used this surface viewpoint in his 1851 dissertation as part of his foundation for functions of a complex variable [1]; the fully abstract manifold formulation is a later clarification, notably developed in Weyl's axiomatic treatment [2].

This account is partly interpretive synthesis: the local-to-global obstruction may now be formulated using monodromy and covering-space language that postdates Riemann. Mathematically, however, it isolates the problem solved by the surface construction: retaining every analytic continuation while restoring the ordinary one-value-per-point meaning of “function.”

### Essential Role

The Riemann surface makes the branch-selection part of the motivating problem tractable by moving it from the value of a function into the identity of a point of its domain. A multivalued expression in \(z\) becomes a single-valued function \(F(p)\), while \(\pi(p)=z\) remembers which base argument is being considered. Analytic continuation becomes path lifting on the surface: a path and an initial branch determine a path through the sheets, and monodromy is read from whether its endpoint lies over the same base point on the same or a different sheet. Thus branch changes are represented geometrically rather than prohibited by cuts.

The local model \(\pi(t)=t^e\) handles a branch value without making \(X\) singular: the coordinate \(t\), not the projected coordinate \(z\), is the regular local parameter. Consequently, holomorphic differentiation, integration, zeros, poles, and continuation can be defined intrinsically at points where a plane branch description fails. In the example \(w^2=z\), the impossible request for a global square root as a holomorphic function of \(z\) on \(\mathbb C^*\) is reformulated as the entirely ordinary global holomorphic coordinate \(w\) on \(X\), with the nontriviality retained in the two-to-one projection \(w\mapsto w^2\).

The deeper structural change is that topology becomes part of the analytic data. Connectivity, loops, sheets, and ramification organize which local elements belong to one global analytic object and how continuation relates them. For algebraic functions, this viewpoint leads, after resolving singularities and adding points when necessary, to a branched covering of the Riemann sphere whose meromorphic function field encodes the original algebraic relation [3], [4]. That algebraic-geometric development is broader than the initial problem, but its mechanism is the same one that directly addressed multivaluedness: separate branches as points, then glue them by analytic continuation.

## 3. Notes

- A branch cut is a device for selecting one branch on a restricted plane domain; it is not itself the Riemann surface of all branches.
- A covering surface has no ramification, whereas the natural projection associated with an algebraic function is generally a branched covering. The underlying space can still be a nonsingular Riemann surface.
- Not every Riemann surface is initially presented as the surface of one named multivalued function. “Riemann surface” is the intrinsic object; a pair \((X,\pi)\) is a surface spread over a base, and \((X,\pi,F)\) records a particular functional relation.

## 4. Sources

[1] Bernhard Riemann, *Grundlagen für eine allgemeine Theorie der Functionen einer veränderlichen complexen Grösse*, Inauguraldissertation, Göttingen, 1851; reprinted in *Gesammelte mathematische Werke*, 2nd ed., Teubner, 1892, pp. 3–48.

[2] Hermann Weyl, *Die Idee der Riemannschen Fläche*, B. G. Teubner, 1913.

[3] Otto Forster, *Lectures on Riemann Surfaces*, Graduate Texts in Mathematics 81, Springer, 1981.

[4] Curtis T. McMullen, *Riemann Surfaces*, Harvard University course notes, especially the discussion of algebraic functions and branched coverings, https://people.math.harvard.edu/~ctm/math213b/home/course/course.pdf.
