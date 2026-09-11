# Mathematical Object Origin Archive | n-Selmer Group of an Elliptic Curve

## 1. Archive Information

- Standard Name: n-Selmer group of an elliptic curve
- Mathematical Field: Algebraic Number Theory
- Abstract: For an elliptic curve over a number field, the \(n\)-Selmer group is the finite subgroup of global Galois cohomology whose classes satisfy the local Kummer condition at every place. It was formed within descent to replace the generally infinite cohomological space containing \(E(K)/nE(K)\) by a finite, in-principle computable envelope. This makes the weak Mordell–Weil step tractable while recording, through its quotient by \(E(K)/nE(K)\), the remaining local-to-global obstruction.

## 2. Core Record

### Precise Description

Let \(K\) be a number field, let \(E/K\) be an elliptic curve, and let \(n\ge 2\). Write
\[
E[n]=\ker\!\left([n]:E(\overline K)\to E(\overline K)\right)
\]
for the finite \(G_K=\operatorname{Gal}(\overline K/K)\)-module of \(n\)-torsion points. The multiplication sequence
\[
0\longrightarrow E[n]\longrightarrow E(\overline K)
 \xrightarrow{[n]}E(\overline K)\longrightarrow 0
\]
gives the global Kummer map
\[
\delta_K:E(K)/nE(K)\hookrightarrow H^1(K,E[n]).
\]
For every place \(v\) of \(K\), its analogue over the completion \(K_v\) is
\[
\delta_v:E(K_v)/nE(K_v)\hookrightarrow H^1(K_v,E[n]).
\]
The \(n\)-Selmer group is
\[
\operatorname{Sel}^{(n)}(E/K)
=
\left\{\xi\in H^1(K,E[n]):
\operatorname{res}_v(\xi)\in\operatorname{im}(\delta_v)
\text{ for every }v\right\},
\]
or equivalently
\[
\operatorname{Sel}^{(n)}(E/K)
=
\ker\!\left(
H^1(K,E[n])\longrightarrow
\prod_v
\frac{H^1(K_v,E[n])}{\operatorname{im}(\delta_v)}
\right).
\]
Here all \(H^1\) groups are continuous Galois cohomology groups. For fixed \(n\), this Selmer group is finite; it is computable in principle using finite descent and local calculations [1, §§7–9; 2, §§12–13].

If
\[
\Sha(E/K)=\ker\!\left(H^1(K,E)\longrightarrow\prod_v H^1(K_v,E)\right)
\]
is the Tate–Shafarevich group, comparison of the global and local Kummer sequences gives the fundamental exact sequence
\[
0\longrightarrow E(K)/nE(K)
\longrightarrow \operatorname{Sel}^{(n)}(E/K)
\longrightarrow \Sha(E/K)[n]
\longrightarrow 0.
\]
Thus the Selmer group is generally an upper envelope for, not a synonym of, the weak Mordell–Weil quotient [1, §§7–8; 3, Chapter X, §4].

### Mathematical Context and Formation

The motivating problem class is descent on elliptic curves over number fields: given \(E/K\), prove that \(E(K)\) is finitely generated and, more concretely, obtain finite information about its generators or rank. The height argument in the Mordell–Weil proof needs the weak Mordell–Weil assertion that \(E(K)/nE(K)\) is finite for some \(n\ge2\). Once there are finitely many representatives modulo \(nE(K)\), subtraction of a representative followed by division by \(n\) lowers canonical height and turns descent into a finite reduction process. Without a finite quotient, the height step has no finite set of residue-class representatives from which to start [1, §1].

The Kummer map supplies a natural first reformulation. If \(P\in E(K)\) and \(Q\in E(\overline K)\) satisfies \(nQ=P\), then
\[
\sigma\longmapsto \sigma(Q)-Q
\]
defines a class in \(H^1(K,E[n])\) depending only on \(P\bmod nE(K)\). This embeds the desired quotient into a cohomology group built from the finite module \(E[n]\). The obstacle is that \(H^1(K,E[n])\) is generally infinite, so this embedding alone neither proves that \(E(K)/nE(K)\) is finite nor reduces its determination to a finite search [2, §§10–12].

Every class coming from a global point nevertheless has additional compatibility: after restriction to every completion \(K_v\), it must come from a local point under \(\delta_v\). The formative insight is therefore to retain precisely the global Kummer classes passing all these necessary local tests. These simultaneous local Kummer conditions define \(\operatorname{Sel}^{(n)}(E/K)\). They exclude most of the infinite ambient cohomology: outside a finite set containing the archimedean places, the places above \(n\), and the places of bad reduction, the relevant classes are constrained by the unramified condition. Finiteness results for the resulting restricted cohomology, ultimately using such arithmetic inputs as finite ideal class groups and finitely generated unit groups, then make the Selmer group finite [1, §9; 2, §13]. In this way, the object arises from joining the global Kummer encoding of divisibility by \(n\) with local solvability as the finiteness-producing restriction.

### Essential Role

The \(n\)-Selmer group makes the exact weak-descent bottleneck tractable. Its definition preserves every class arising from \(E(K)/nE(K)\), because a global point automatically supplies compatible points over all \(K_v\), but it replaces the infinite ambient group \(H^1(K,E[n])\) by a finite group determined through global arithmetic and finitely many substantive local tests. Consequently,
\[
E(K)/nE(K)\hookrightarrow \operatorname{Sel}^{(n)}(E/K).
\]
This directly proves the finiteness required by weak Mordell–Weil; combined with the height descent, it supplies the finite-generation step for \(E(K)\). In explicit descent, the same inclusion yields a finite upper bound on the weak quotient and hence on the Mordell–Weil rank [1, §§1, 9; 3, Chapter X, §4].

The exact sequence with \(\Sha(E/K)[n]\) explains precisely what the local tests do not resolve. A Selmer class may satisfy every local Kummer condition while failing to come from a global rational point; the quotient \(\Sha(E/K)[n]\) measures that discrepancy. Thus the Selmer group does not simply assert that local data determine global points. Rather, it separates descent into a finite, locally testable computation and a residual failure of the local-to-global principle. This is the deeper structural viewpoint introduced by the object: the rational-point problem is bounded by a finite global-to-local compatibility group, and the possible overcount is isolated as a specific obstruction group rather than left hidden inside an infinite cohomology set [1, §§7–9; 3, Chapter X, §4].

## 3. Notes

- The defining local condition is membership in \(\operatorname{im}(\delta_v)\), not vanishing in \(H^1(K_v,E[n])\). Accordingly, the \(n\)-Selmer group should not be confused with the subgroup of everywhere locally trivial classes in \(H^1(K,E[n])\) [2, §12].
- The construction extends to an isogeny \(\phi:E\to E'\), producing a \(\phi\)-Selmer group that contains \(E'(K)/\phi E(K)\). The object archived here is specifically the multiplication-by-\(n\) case \(\phi=[n]\).
- Finiteness of \(\operatorname{Sel}^{(n)}(E/K)\) holds for each fixed \(n\). This does not imply that the full Tate–Shafarevich group is finite, and a Selmer computation need not by itself exhibit generators of \(E(K)\).

## 4. Sources

[1] Bjorn Poonen, *The Selmer Group, the Shafarevich–Tate Group, and the Weak Mordell–Weil Theorem*, lecture notes, 2001, https://math.mit.edu/~poonen/f01/weakmw.pdf.

[2] Bjorn Poonen, *Selmer Group Heuristics and Sieves*, expanded lecture notes for the 2014 Arizona Winter School on Arithmetic Statistics, https://math.mit.edu/~poonen/papers/aws2014.pdf.

[3] Joseph H. Silverman, *The Arithmetic of Elliptic Curves*, 2nd ed., Graduate Texts in Mathematics 106, Springer, 2009, Chapter X, §4.
