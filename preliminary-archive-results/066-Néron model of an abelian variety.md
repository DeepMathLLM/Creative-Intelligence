# Mathematical Object Origin Archive | Néron Model of an Abelian Variety

## 1. Archive Information

- Standard Name: Néron model of an abelian variety
- Mathematical Field: Algebraic Geometry; Arithmetic Geometry
- Abstract: The Néron model is the canonical smooth, separated group scheme that extends an abelian variety from the fraction field of a discrete valuation ring to the ring itself. It was formed to make extension and reduction of points and morphisms well defined even at places of bad reduction, where no smooth proper group model can exist. Its defining mapping property replaces a potentially singular, equation-dependent compactification by a universal smooth extension target [1][2].

## 2. Core Record

### Precise Description

Let $R$ be a discrete valuation ring with fraction field $K$, residue field $k$, and generic point $\eta=\operatorname{Spec}K$. Let $A/K$ be an abelian variety. A **Néron model** of $A$ over $R$ is a smooth, separated $R$-scheme of finite type $\mathcal A$, together with an identification $\mathcal A_K\cong A$, satisfying the Néron mapping property:

\[
\operatorname{Hom}_R(Y,\mathcal A)\;\xrightarrow{\sim}\;
\operatorname{Hom}_K(Y_K,A)
\]

for every smooth $R$-scheme $Y$, where the map is restriction to the generic fiber [2, Ch. 1, §2]. Such a model exists for every abelian variety over $K$ and is unique up to a unique isomorphism [1][2].

Although a group law is not an extra clause in this formulation, the multiplication, inverse, and identity of $A$ extend uniquely by the mapping property, making $\mathcal A$ a smooth separated $R$-group scheme. For example, multiplication extends by applying the property to the smooth scheme $Y=\mathcal A\times_R\mathcal A$. Taking $Y=\operatorname{Spec}R$ gives the canonical bijection

\[
\mathcal A(R)\cong A(K).
\]

Thus each $K$-rational point has one and only one integral section and hence a well-defined specialization in the smooth algebraic group $\mathcal A_k$.

### Mathematical Context and Formation

The motivating problem is local reduction for abelian varieties. Given $A/K$, one wants to compare its generic-fiber geometry with geometry over the residue field: extend $K$-rational points to integral sections, extend homomorphisms and families of maps across the closed point, and obtain a reduction object that is independent of a chosen projective embedding or set of equations. This is straightforward at a place of good reduction, because then $A$ extends to an abelian scheme, namely a smooth proper group scheme over $R$.

At a place of bad reduction, those requirements conflict if properness is retained. A smooth proper group model would itself be an abelian scheme and would therefore assert good reduction. Taking the closure of $A$ in a projective model avoids losing properness, but its special fiber may be singular, the group operations need not extend as morphisms on the entire closure, and the result depends on the presentation. Properness can extend a $K$-point to a section of such a model, but the section may meet its nonsmooth locus; moreover, properness alone does not supply the universal extension of maps from arbitrary smooth $R$-schemes. Merely resolving or regularizing a compactification likewise does not impose a canonical group model or the required universal mapping behavior [2, Chs. 1–3].

The formative idea is therefore to relax properness and make smooth extension, rather than compactification, the organizing requirement. The target is required to be smooth and separated over $R$, while the Néron mapping property says exactly that every generic-fiber map from a smooth test scheme extends uniquely. Constructions by successive smoothening remove the obstructions presented by a chosen model until this universal property holds; the property then makes the result independent of those construction choices [1][2]. This reformulates bad reduction: one does not force the degenerate fiber to remain an abelian variety, but retains the largest canonical smooth group-theoretic extension behavior compatible with the generic fiber.

### Essential Role

The Néron model makes the extension-and-reduction part of the motivating problem tractable. First, $A(K)=\mathcal A(R)$ turns every rational point into a unique section, so reduction is obtained by evaluating that section on the closed fiber rather than by choosing coordinates and clearing denominators. Second, if $A$ and $B$ have Néron models and $f:A\to B$ is a $K$-morphism, applying the mapping property for $\mathcal B$ to the smooth source $\mathcal A$ produces a unique extension $\mathcal A\to\mathcal B$. In particular, homomorphisms and the group operations extend canonically. Separatedness supplies uniqueness, while smoothness specifies the class of nonsingular test families for which extension is guaranteed.

The special fiber $\mathcal A_k$ is therefore a canonical smooth algebraic group even when $A$ has bad reduction. Its identity component and its group of connected components record how the generic abelian variety degenerates; nonproperness and possible disconnectedness are not defects accidentally introduced by a projective model, but structural data permitted by abandoning the impossible demand for an abelian scheme at a bad place. At good reduction the Néron model is the abelian scheme, whereas at bad reduction it isolates the smooth group geometry from the singularities of compactifications [2][3]. The direct achievement is thus not a generic compactification theorem: it is the canonical extension of points, morphisms, and group structure across a valuation, together with a smooth special fiber on which reduction can be studied.

## 3. Notes

The Néron model should not be confused with a minimal proper regular model. For an elliptic curve these objects are closely related—the Néron model can be obtained from the smooth locus of the minimal proper regular model—but the Néron model is generally not proper at bad reduction. Some authors also use **Néron lft-model** when only local finite type is required. Néron models behave well under étale base change, but formation need not commute with arbitrary ramified extensions [2].

## 4. Sources

[1] André Néron, “Modèles minimaux des variétés abéliennes sur les corps locaux et globaux,” *Publications Mathématiques de l’IHÉS* **21** (1964), 5–128. https://www.numdam.org/item/PMIHES_1964__21__5_0/

[2] Siegfried Bosch, Werner Lütkebohmert, and Michel Raynaud, *Néron Models*, Ergebnisse der Mathematik und ihrer Grenzgebiete, 3rd Series, vol. 21, Springer, 1990. https://doi.org/10.1007/978-3-642-51438-8

[3] Brian Conrad, *Néron Models* (seminar notes), especially §§1.3 and 2.3. http://virtualmath1.stanford.edu/~conrad/mordellsem/Notes/L11.pdf
