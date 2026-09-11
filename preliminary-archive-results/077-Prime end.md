# Mathematical Object Origin Archive | Prime End

## 1. Archive Information

- Standard Name: Prime end (Carathéodory prime end)
- Mathematical Field: Complex Analysis
- Abstract: A prime end is an equivalence class of nested, shrinking crosscut approaches to the boundary of a simply connected plane domain. It was formed to solve the boundary-correspondence problem left open by the Riemann mapping theorem when the domain boundary is not a Jordan curve. Prime ends replace the possibly wild Euclidean boundary by an intrinsic boundary circle on which every Riemann map extends homeomorphically.

## 2. Core Record

### Precise Description

Let \(\Omega\subset\mathbb C\) be a bounded simply connected domain and fix \(z_0\in\Omega\). A **crosscut** \(C\) of \(\Omega\) is an open Jordan arc in \(\Omega\) whose closure \(\overline C\) is a closed Jordan arc with two distinct endpoints in \(\partial\Omega\) and no other boundary points. In what follows, only crosscuts satisfying \(z_0\notin C\) are used. The set \(\Omega\setminus C\) has two components, exactly one of which contains \(z_0\). Write \(U(C)\) for the other component.

A **null chain of crosscuts relative to \(z_0\)** is a sequence \((C_n)_{n\ge 1}\) of such crosscuts for which, with \(U_n=U(C_n)\),

\[
\overline{U_{n+1}}\cap\Omega\subset U_n,\qquad
\overline C_n\cap\overline C_m=\varnothing\quad(n\ne m),
\qquad
\operatorname{diam}(C_n)\longrightarrow 0.
\]

Thus the \(U_n\) form nested regions lying successively farther from the base point and toward the boundary. Two null chains \((C_n,U_n)\) and \((C'_n,U'_n)\) are **equivalent** when they are cofinal under inclusion: for every \(n\) there is an \(m\) with \(U'_m\subset U_n\), and for every \(n\) there is an \(m\) with \(U_m\subset U'_n\). A **prime end** of \(\Omega\) is an equivalence class of null chains. Changing the base point produces the same prime-end boundary up to its canonical identification, since any given chain eventually separates either base point from the end in the same way [2][3].

The **impression** of a prime end \(P=[(C_n)]\) is

\[
I(P)=\bigcap_{n=1}^{\infty}\overline{U_n}.
\]

It is a nonempty compact connected subset of \(\partial\Omega\), independent of the representative chain. It need not be a single point. Conversely, distinct prime ends can have impressions containing the same Euclidean boundary point: a prime end records an internal manner of approach, not merely a point of \(\partial\Omega\) [2][3].

Let \(\partial_P\Omega\) be the set of prime ends. Adjoining it to \(\Omega\), with neighborhoods of \(P\) determined by the crosscut domains \(U_n\) together with all prime ends eventually represented inside \(U_n\), gives the **prime-end compactification**

\[
\Omega^P=\Omega\sqcup\partial_P\Omega.
\]

For such \(\Omega\), \(\Omega^P\) is homeomorphic to the closed disk and \(\partial_P\Omega\) is homeomorphic to the circle [1][2].

### Mathematical Context and Formation

The motivating problem was the boundary-extension problem for the Riemann map. The Riemann mapping theorem gives a conformal bijection

\[
f:\mathbb D\longrightarrow\Omega
\]

for every proper simply connected plane domain \(\Omega\), but it is an interior theorem. For a Jordan domain, one can ask for—and obtain—a homeomorphic extension \(\overline{\mathbb D}\to\overline\Omega\). For an arbitrary simply connected domain, however, \(\partial\Omega\) may have slits, infinitely accumulating fjords, or non-locally-connected continua. Its Euclidean closure need not be a closed disk, and its boundary need not be a circle. Consequently there may be no bijection \(S^1\to\partial\Omega\) compatible with interior convergence.

The exact obstruction is that a Euclidean boundary point does not encode how it is approached from inside \(\Omega\). Different interior channels can terminate at the same point, while a single approach channel can have a whole continuum as its cluster set. Merely adjoining points of \(\partial\Omega\) therefore either identifies approaches that the conformal map distinguishes or asks one point of \(S^1\) to correspond to several Euclidean limit points. The ordinary Euclidean boundary is consequently the wrong target for a general one-to-one boundary correspondence. Results restricted to Jordan boundaries avoid this obstruction but do not describe arbitrary simply connected domains [1][3].

The formative insight was to treat an **end from within the domain** as the boundary object. A crosscut separates two sides of \(\Omega\); a nested sequence of crosscut domains specifies a progressively finer approach channel; the null condition forces the gates of that channel to shrink; and cofinal equivalence discards the accidental choice of gates while preserving the channel itself. This converts boundary approach into an intrinsic geometric object and produces enough distinct boundary elements to separate inequivalent accesses, without requiring each element to be a Euclidean point. Carathéodory introduced this construction in his treatment of the boundaries of arbitrary simply connected domains [1].

### Essential Role

Prime ends make the missing boundary part of the Riemann mapping problem tractable. Carathéodory's prime-end theorem states that a conformal bijection \(f:\mathbb D\to\Omega\) extends uniquely to a homeomorphism

\[
f^P:\overline{\mathbb D}\longrightarrow\Omega^P.
\]

Equivalently, every \(\zeta\in S^1\) corresponds to exactly one prime end of \(\Omega\), and every prime end occurs this way [1][2][3]. The extension does not falsely assert that \(f(z)\) has a single Euclidean limit at every \(\zeta\): the impression of the corresponding prime end records the full boundary cluster continuum when a point limit fails to exist.

The mechanism is specific to the definition. Crosscuts convert proximity to a complicated boundary into planar separation data; nesting orders approaches by refinement; shrinking diameter prevents an alleged end from retaining a macroscopic interior gate; and cofinal equivalence makes the resulting boundary element independent of the particular chain used. Conformal maps preserve the relevant separation and nested-access structure, so the boundary correspondence is attached to \(\Omega\), not to a chosen Riemann map. The original extension problem is thereby reformulated from “match the circle bijectively with \(\partial\Omega\)”—which can be impossible—to “match it with the set of internal boundary approaches,” which always yields a circle.

When \(\partial\Omega\) is a Jordan curve, every prime-end impression is a singleton and each boundary point determines exactly one prime end. In that case \(\Omega^P\) canonically identifies with \(\overline\Omega\), and the prime-end theorem specializes to the homeomorphic boundary extension for Jordan domains. Thus prime ends both recover the classical regular-boundary result and identify precisely what must replace Euclidean boundary points when regularity is absent [1][3].

## 3. Notes

A prime end should not be confused with its impression. The former is an equivalence class of approaches inside the domain; the latter is a subset of the Euclidean boundary and can lose information because different prime ends may have overlapping or identical impressions. For bounded simply connected domains with locally connected boundary, every impression is a singleton and a Riemann map extends continuously to \(\overline{\mathbb D}\), but that boundary extension need not be injective unless the boundary is a Jordan curve [3].

The archive uses the classical planar, simply connected version. Prime-end constructions have extensions to multiply connected domains, surfaces, and metric-space settings, but their hypotheses and definitions are not identical to the object recorded here [2].

## 4. Sources

[1] C. Carathéodory, “Über die Begrenzung einfach zusammenhängender Gebiete,” *Mathematische Annalen* **73** (1913), 323–370. https://doi.org/10.1007/BF01456699

[2] D. B. A. Epstein, “Prime Ends,” *Proceedings of the London Mathematical Society*, Third Series **42** (1981), no. 3, 385–414. https://doi.org/10.1112/plms/s3-42.3.385

[3] Ch. Pommerenke, *Boundary Behaviour of Conformal Maps*, Grundlehren der mathematischen Wissenschaften 299, Springer-Verlag, 1992. https://doi.org/10.1007/978-3-662-02770-7
