# Mathematical Object Origin Archive | Radical of an Ideal

## 1. Archive Information

- Standard Name: Radical of an ideal
- Mathematical Field: Commutative Algebra; Algebraic Geometry
- Abstract: For an ideal $I$ in a commutative ring $R$, its radical $\sqrt I$ is the ideal of elements whose positive powers lie in $I$. It is the power-insensitive closure of $I$. In polynomial rings over an algebraically closed field, this closure answers the concrete problem of recovering every polynomial that vanishes on the common zero set of the equations in $I$: Hilbert's Nullstellensatz gives $I(V(I))=\sqrt I$.

## 2. Core Record

### Precise Description

Let $R$ be a commutative ring with identity and let $I\subseteq R$ be an ideal. The **radical of $I$** is

\[
\sqrt I=\{r\in R: r^n\in I\text{ for some integer }n\ge 1\}.
\]

This set is an ideal, contains $I$, and is radical in the sense that $r^n\in\sqrt I$ implies $r\in\sqrt I$. Moreover, it is the smallest radical ideal containing $I$: if $I\subseteq J$ and $J$ is radical, then $\sqrt I\subseteq J$. Equivalent descriptions are

\[
\sqrt I/I=\operatorname{Nil}(R/I)
\qquad\text{and}\qquad
\sqrt I=\bigcap_{\mathfrak p\supseteq I}\mathfrak p,
\]

where the intersection ranges over prime ideals of $R$ containing $I$ [1]. Thus $R/\sqrt I$ is the reduced quotient of $R/I$.

For $R=k[x_1,\ldots,x_n]$ and $I\subseteq R$, write

\[
V_k(I)=\{a\in k^n:f(a)=0\text{ for every }f\in I\}
\]

and, for $X\subseteq k^n$,

\[
I(X)=\{f\in R:f(a)=0\text{ for every }a\in X\}.
\]

If $k$ is algebraically closed, Hilbert's Nullstellensatz states

\[
I(V_k(I))=\sqrt I.
\]

Equivalently, a polynomial $f$ vanishes at every common zero of $I$ exactly when $f^N\in I$ for some $N\ge 1$ [2].

### Mathematical Context and Formation

The motivating problem is the equation-to-locus-to-equation problem for affine algebraic sets: given polynomial equations generating $I\subseteq k[x_1,\ldots,x_n]$, determine all polynomial equations that hold on their common solution set $V_k(I)$, and determine when two systems of equations define the same set.

Ordinary ideal membership is too fine for this problem. It records direct polynomial combinations of the chosen equations, while a zero set cannot distinguish an equation from a positive power of that equation. If $g^m\in I$, then at any $a\in V_k(I)$ one has $g(a)^m=0$, hence $g(a)=0$ because a field has no nonzero nilpotent elements; nevertheless, $g$ need not belong to $I$. For example, in $k[x]$,

\[
I=(x^2),\qquad V_k(I)=V_k((x))=\{0\},
\]

but $x\notin(x^2)$. Thus $I$ does not itself contain every polynomial consequence visible on the solution set. Passing merely to arbitrary larger ideals would discard too much information and would not provide a canonical answer.

The decisive structural observation is that pointwise vanishing is insensitive precisely to taking positive powers. Closing $I$ under the implication $g^m\in I\Rightarrow g\in I$ produces the canonical ideal $\sqrt I$. This construction removes the nilpotent classes in $R/I$, since such a class $\bar g$ is nilpotent exactly when $g\in\sqrt I$. The general identity $V(I)=V(\sqrt I)$ on $\operatorname{Spec}(R)$ and the prime-intersection formula show algebraically why the radical preserves the underlying closed locus [1]. Over an algebraically closed field, the Nullstellensatz supplies the nontrivial converse: no additional polynomial vanishing on all closed points is missed, so $I(V_k(I))$ is exactly $\sqrt I$, not merely an ideal containing it [2].

### Essential Role

The radical makes the recovery step in the motivating problem exact. It replaces a presentation-dependent equation ideal $I$ by the unique smallest power-closed ideal carrying the same set-theoretic zero locus. Consequently,

\[
V_k(I)=V_k(J)\quad\Longleftrightarrow\quad \sqrt I=\sqrt J
\]

for ideals $I,J\subseteq k[x_1,\ldots,x_n]$ when $k$ is algebraically closed. The forward implication is obtained by applying $I(-)$ and the Nullstellensatz; the reverse implication follows from $V(I)=V(\sqrt I)$.

Each feature of the definition addresses a specific obstruction. The condition “some power of $g$ lies in $I$” captures exactly the implication forced by evaluation in fields. Taking all such $g$ gives a canonical closure rather than an arbitrary enlargement. The minimality of $\sqrt I$ ensures that no further algebraic equations are added beyond those forced by power-insensitivity. Finally, the quotient $R/\sqrt I$ deletes nilpotent residue classes while retaining the same prime spectrum as $R/I$ at the level of underlying closed sets [1]. In this way the radical separates the set-theoretic geometry of a system of equations from multiplicity or infinitesimal information encoded by nonradical ideals: $(x)$ and $(x^2)$ have the same zero set, while their quotient rings retain different nilpotent structure.

This role is exact only under the stated hypotheses for $k$-rational zero sets. If $k$ is not algebraically closed, $I(V_k(I))$ can be strictly larger than $\sqrt I$; for instance, $V_{\mathbb R}((x^2+1))=\varnothing$, so its vanishing ideal is the whole ring, whereas $(x^2+1)$ is a proper radical ideal of $\mathbb R[x]$. The unrestricted ring-theoretic statements about $\sqrt I$, prime ideals, and $\operatorname{Spec}(R)$ remain valid.

## 3. Notes

The radical of $I$ should not be confused with the **nilradical** $\sqrt{(0)}$, which is the special case $I=(0)$, or with the **Jacobson radical**, the intersection of all maximal ideals of a ring. A radical ideal is an ideal $J$ satisfying $J=\sqrt J$; the object archived here is the closure operation $I\mapsto\sqrt I$ and its value on a specified ideal.

## 4. Sources

[1] The Stacks Project Authors, “The spectrum of a ring,” Section 10.17, especially Lemma 10.17.2, Tag 00DY. https://stacks.math.columbia.edu/tag/00DY

[2] The Stacks Project Authors, “Hilbert Nullstellensatz,” Theorem 10.34.1, Tag 00FV. https://stacks.math.columbia.edu/tag/00FV
