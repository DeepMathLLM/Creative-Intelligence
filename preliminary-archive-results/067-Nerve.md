# Mathematical Object Origin Archive | Nerve

## 1. Archive Information

- Standard Name: Nerve
- Mathematical Field: Category Theory
- Abstract: The nerve encodes a small category as a simplicial set whose simplices are composable strings of arrows. A formative categorical use arose in Grothendieck’s treatment of the problem of forming quotients by internal pre-equivalence relations, especially for preschemes: it organized the objects, arrows, compositions, and identities of an internal category or groupoid into one functorial simplicial object without discarding the original categorical structure.

## 2. Core Record

### Precise Description

Let \(\Delta\) be the simplex category, whose objects are the finite ordered sets \([n]=\{0<\cdots<n\}\) and whose morphisms are order-preserving maps. For a small category \(\mathcal C\), its **nerve** is the simplicial set
\[
N(\mathcal C)\colon \Delta^{\mathrm{op}}\longrightarrow \mathbf{Set},
\qquad
N(\mathcal C)_n=\operatorname{Fun}([n],\mathcal C).
\]
Thus an \(n\)-simplex is a composable string
\[
x_0\xrightarrow{f_1}x_1\xrightarrow{f_2}\cdots\xrightarrow{f_n}x_n.
\]
Precomposition by a map \([m]\to[n]\) supplies the simplicial operators. Concretely, inner face maps compose two adjacent arrows, outer face maps remove the first or last arrow, and degeneracy maps insert identity arrows. Consequently, \(N(\mathcal C)_0\) records objects, \(N(\mathcal C)_1\) records morphisms, and \(N(\mathcal C)_2\), together with its faces, records composition. The simplicial identities encode the unit and associativity laws. The functor
\[
N\colon \mathbf{Cat}\longrightarrow \mathbf{sSet}
\]
is fully faithful, so the category and every functor between categories can be recovered from their nerves [1, §4, Proposition 4.1; 2].

The same construction internalizes. If an internal category in a category \(\mathcal E\) with the required fiber products has object object \(X\), arrow object \(R\), and source and target maps \(s,t\colon R\rightrightarrows X\), then its nerve is the simplicial object with
\[
N_0=X,\qquad N_1=R,\qquad
N_n=\underbrace{R\times_X R\times_X\cdots\times_X R}_{n\text{ factors}}\quad(n\ge 2),
\]
where the fiber products impose composability. Faces use source, target, and composition, while degeneracies use identities. For an internal groupoid, inversion is additional structure satisfying the groupoid identities; equivalently, it gives the appropriate invertibility properties of the associated simplicial object.

### Mathematical Context and Formation

The motivating problem class was the **passage to a quotient** of an object \(X\) by a relation in a category, with the intended application to schemes. In sets, an equivalence relation \(R\subseteq X\times X\) immediately yields a set of equivalence classes. In a general category—and particularly in the category of preschemes—the coequalizer of two maps
\[
s,t\colon R\rightrightarrows X
\]
need not exist, and even when it exists it need not have the geometric properties expected of a quotient. Grothendieck therefore studied criteria under which a pre-equivalence relation admits a quotient prescheme [1, §§4–5].

The exact formal obstacle comes before the existence theorem. A pre-equivalence relation is an internal groupoid with object object \(X\) and arrow object \(R\). The displayed pair \(R\rightrightarrows X\) alone does not specify the unit, inverse, or composition map
\[
R\times_{X}R\longrightarrow R,
\]
nor their compatibility laws. Grothendieck explicitly notes that, unlike an ordinary equivalence-relation pair, these two arrows do not determine the structure being used, while the additional groupoid data enter the quotient arguments [1, §4]. Writing all iterated composability objects and all compatibility maps separately obscures their common pattern and makes functorial transport—especially base change and descent-style reasoning—awkward.

The organizing insight was to probe a category by the finite ordered categories \([n]\). The resulting sets of functors \([n]\to\mathcal C\) collect composable strings in every degree, and order-preserving maps induce all operations among them. Applied internally to \(R\rightrightarrows X\), this produces the sequence
\[
X,\quad R,\quad R\times_XR,\quad R\times_XR\times_XR,\ldots
\]
with the structure maps forced into simplicial identities. In Grothendieck’s 1961 quotient-prescheme exposition, this categorical-to-simplicial encoding appears immediately before the definition of pre-equivalence relations and the quotient criteria; Proposition 4.1 establishes its full faithfulness and characterizes the relevant simplicial diagrams [1]. The documentary evidence therefore ties this categorical form of the nerve directly to the formal problem of quotienting by pre-equivalence relations, rather than merely to its later topological interpretation. Claims of absolute historical priority are not needed here.

### Essential Role

The nerve did not by itself prove that a quotient prescheme exists. Its direct role was to make the **relation data on which the existence proof depends** manageable and invariantly expressible. Degree \(0\) isolates the object being quotiented; degree \(1\) gives the relation arrows; degree \(2\) records composable pairs and their composite; degree \(3\) expresses associativity through compatible faces; and degeneracies encode identities. Thus the many structure maps and coherence equations of an internal category or groupoid become the components and identities of a single simplicial object.

This addressed the inadequacy of treating \(R\rightrightarrows X\) as only a parallel pair. The quotient itself is characterized by coequalizing that pair, but proofs may require the fuller groupoid structure that says why the pair behaves as a relation and how chains of identifications compose. Since the nerve is fully faithful, replacing the groupoid by its simplicial encoding loses none of that information. Since its higher levels are iterated fiber products, they also display exactly the overlap objects on which compatibility and base-change arguments must be checked.

The resulting structural viewpoint reformulated a quotient relation from a binary diagram plus separately stated axioms into a simplicial resolution-like diagram. This made it possible to separate two issues cleanly: the nerve controls the coherent relation data, while separate geometric hypotheses—such as the finiteness and local-freeness conditions studied for preschemes—control representability and existence of the quotient [1, §5]. That division of labor, rather than any later use of geometric realization or classifying spaces, is the nerve’s essential contribution to the motivating quotient problem.

## 3. Notes

The selected object is the nerve of a category, not the older nerve of a covering family in topology. The latter is a simplicial complex recording nonempty intersections. The categorical nerve is instead the simplicial set of composable arrows; its geometric realization is now called the classifying space of the category, but that topological interpretation was not the issue driving the quotient-prescheme presentation discussed here [3]. “Čech nerve” and “homotopy-coherent nerve” are related constructions, not synonyms for the ordinary categorical nerve archived here.

## 4. Sources

[1] Alexander Grothendieck, “Techniques de construction et théorèmes d’existence en géométrie algébrique III : préschémas quotients,” *Séminaire Bourbaki*, no. 6, Exposé 212 (1961), pp. 99–118, especially §§4–5 and Proposition 4.1. http://www.numdam.org/item/SB_1960-1961__6__99_0.pdf

[2] Kerodon, “The Nerve of a Category,” Construction 1.3.1.1 and following remarks. https://kerodon.net/tag/002M

[3] Graeme Segal, “Classifying Spaces and Spectral Sequences,” *Publications Mathématiques de l’IHÉS* 34 (1968), pp. 105–112, especially §2. https://www.numdam.org/item/PMIHES_1968__34__105_0/
