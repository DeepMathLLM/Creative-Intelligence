# Mathematical Object Origin Archive | Ext Functor

## 1. Archive Information

- Standard Name: Ext functor
- Mathematical Field: Homological Algebra
- Abstract: The groups \(\operatorname{Ext}^n_R(A,B)\) turn the problem of classifying extensions of one \(R\)-module by another, and the related failure of homomorphisms to extend or lift, into functorial computable invariants. In degree one, \(\operatorname{Ext}^1\) is precisely the group of equivalence classes of short exact extensions; projective or injective resolutions extend this construction to all degrees.

## 2. Core Record

### Precise Description

Let \(R\) be a ring and let \(A,B\) be left \(R\)-modules. Choose a projective resolution
\[
\cdots \longrightarrow P_2\xrightarrow{d_2}P_1\xrightarrow{d_1}P_0\longrightarrow A\longrightarrow 0.
\]
Applying \(\operatorname{Hom}_R(-,B)\) gives the cochain complex
\[
0\longrightarrow \operatorname{Hom}_R(P_0,B)
 \xrightarrow{d_1^*}\operatorname{Hom}_R(P_1,B)
 \xrightarrow{d_2^*}\operatorname{Hom}_R(P_2,B)\longrightarrow\cdots.
\]
The Ext groups are
\[
\operatorname{Ext}^n_R(A,B)
 =H^n\!\left(\operatorname{Hom}_R(P_\bullet,B)\right),\qquad n\ge 0.
\]
Their canonical isomorphism class is independent of the chosen resolution; equivalently they can be computed from an injective resolution of \(B\). Thus \(\operatorname{Ext}^0_R(A,B)\cong\operatorname{Hom}_R(A,B)\), and \(\operatorname{Ext}^n_R(-,-)\) is contravariant in \(A\) and covariant in \(B\) [1][2].

For \(n=1\), \(\operatorname{Ext}^1_R(A,B)\) is canonically identified with equivalence classes of short exact sequences
\[
0\longrightarrow B\longrightarrow E\longrightarrow A\longrightarrow 0,
\]
where an equivalence is an isomorphism of short exact sequences inducing the identity on \(A\) and \(B\). Baer sum supplies the abelian-group operation, and the zero element is the split extension. More generally, degree-\(n\) Yoneda extensions are exact sequences with \(n\) intermediate objects; concatenation represents the Yoneda product [2][3].

### Mathematical Context and Formation

The motivating problem class is the extension problem: for fixed \(A\) and \(B\), determine all ways an object \(E\) can contain \(B\) as a submodule with quotient \(A\), decide when the resulting short exact sequence splits, and compare such constructions without retaining irrelevant choices of representatives. Directly listing middle modules \(E\), injections, and quotient maps is inadequate: different presentations can define the same extension, an isomorphism of middle modules need not respect the prescribed copies of \(A\) and \(B\), and the non-splitting information is not encoded by the ordinary morphism group \(\operatorname{Hom}_R(A,B)\).

The same difficulty appears as a failure of map extension. Given a projective presentation
\[
0\longrightarrow K\longrightarrow P\longrightarrow A\longrightarrow 0,
\]
a homomorphism \(f:K\to B\) need not extend to a homomorphism \(P\to B\). Its pushout along \(K\hookrightarrow P\) produces an extension of \(A\) by \(B\). Two maps \(K\to B\) produce the same extension class exactly when their difference is the restriction of a map \(P\to B\). Consequently,
\[
\operatorname{Ext}^1_R(A,B)
\cong
\operatorname{coker}\!\left(
\operatorname{Hom}_R(P,B)\longrightarrow\operatorname{Hom}_R(K,B)
\right).
\]
This identifies the extension problem with the first defect of exactness of \(\operatorname{Hom}\). Replacing one presentation by a full projective resolution and retaining the cohomology of the resulting Hom complex is the forming insight behind the family \(\operatorname{Ext}^n\): choices are absorbed by resolution-independence, while successive defects are recorded degree by degree [1][2].

A concrete instance is the classification of extensions of \(\mathbb Z/n\mathbb Z\) by an abelian group \(B\). The resolution
\[
0\longrightarrow\mathbb Z\xrightarrow{\,n\,}\mathbb Z
\longrightarrow\mathbb Z/n\mathbb Z\longrightarrow0
\]
gives
\[
\operatorname{Ext}^1_{\mathbb Z}(\mathbb Z/n\mathbb Z,B)\cong B/nB.
\]
Indeed, if \(e\in E\) lifts \(1\in\mathbb Z/n\mathbb Z\), then \(ne\in B\); replacing \(e\) by \(e+b\) changes \(ne\) by \(nb\). Thus the residue class of \(ne\) is the invariant of the extension, and it vanishes exactly when a lift of the generator can be chosen with order dividing \(n\), equivalently when the extension splits.

### Essential Role

The Ext functor made the classification and splitting parts of the extension problem tractable by replacing a redundant collection of exact sequences with a functorial abelian group. Its defining equivalence relation removes dependence on the presentation of the middle object, Baer sum makes extension classes algebraically composable, and the distinguished zero class gives an exact splitting criterion. The projective-resolution description turns the same classes into cohomology, so the obstruction is computed from homomorphism groups and differentials rather than by guessing all possible middle modules.

More specifically, in a projective presentation the cokernel above measures precisely which maps \(K\to B\) fail to extend across \(K\hookrightarrow P\). Pushout converts each such failure into an extension, while quotienting by extendable maps removes exactly those changes that do not alter its class. Higher \(\operatorname{Ext}^n\) then records analogous higher defects and fits short exact sequences into natural long exact sequences [2][3]. The deeper structural viewpoint is that non-split gluing is not an exceptional pathology of individual modules: it is the derived, functorial failure of \(\operatorname{Hom}\) to be exact.

## 3. Notes

The order of the arguments is essential: \(\operatorname{Ext}^1_R(A,B)\) classifies extensions with submodule \(B\) and quotient \(A\). The notation “Ext” may mean the individual group, the graded family, or the corresponding bifunctor. Ext should not be confused with \(\operatorname{Tor}\), which derives tensor product and measures a different failure of exactness.

## 4. Sources

[1] Henri Cartan and Samuel Eilenberg, *Homological Algebra*, Princeton University Press, 1956, especially Chapters V–VI.

[2] Charles A. Weibel, *An Introduction to Homological Algebra*, Cambridge University Press, 1994, Chapters 2–3.

[3] The Stacks Project Authors, “Ext groups,” Section 13.27, Tag 06XP, https://stacks.math.columbia.edu/tag/06XP.
