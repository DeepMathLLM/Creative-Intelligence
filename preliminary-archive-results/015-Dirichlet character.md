# Mathematical Object Origin Archive | Dirichlet Character

## 1. Archive Information

- Standard Name: Dirichlet character
- Mathematical Field: Analytic Number Theory
- Abstract: A Dirichlet character is a one-dimensional character of the finite multiplicative group of reduced residue classes modulo an integer, extended by zero to nonunits. For nontrivial moduli, it reconciles two requirements in Dirichlet’s problem of proving that every reduced arithmetic progression contains infinitely many primes: selecting one congruence class is an additive condition, whereas Euler’s product-based method requires multiplicative coefficients. Character orthogonality supplies the selection, while character multiplicativity preserves the Euler product.

## 2. Core Record

### Precise Description

Fix an integer $q\geq 1$ and let
\[
G_q=(\mathbb Z/q\mathbb Z)^\times.
\]
A **Dirichlet character modulo $q$** is obtained from a group homomorphism
\[
\widetilde\chi:G_q\longrightarrow \mathbb C^\times
\]
by defining a function $\chi:\mathbb Z\to\mathbb C$ through
\[
\chi(n)=
\begin{cases}
\widetilde\chi(n\bmod q),&\gcd(n,q)=1,\\
0,&\gcd(n,q)>1.
\end{cases}
\]
Equivalently, $\chi$ is periodic modulo $q$, completely multiplicative, and satisfies $\chi(n)=0$ exactly when $n$ is not coprime to $q$. Since $G_q$ is finite, every nonzero value of $\chi$ is a root of unity. The principal character $\chi_0$ equals $1$ on integers coprime to $q$ and $0$ on the others.

The $\varphi(q)$ characters modulo $q$ form the dual group $\widehat{G_q}$. Their decisive finite Fourier orthogonality relation is, for $\gcd(a,q)=1$,
\[
\frac{1}{\varphi(q)}\sum_{\chi\bmod q}\overline{\chi(a)}\chi(n)
=
\begin{cases}
1,&n\equiv a\pmod q,\\
0,&n\not\equiv a\pmod q.
\end{cases}
\]
Here the formula also covers nonunits $n$, because then every $\chi(n)$ is zero. Associated to $\chi$ is the Dirichlet series
\[
L(s,\chi)=\sum_{n\geq 1}\frac{\chi(n)}{n^s},
\]
which, by complete multiplicativity, has for $\Re(s)>1$ the Euler product
\[
L(s,\chi)=\prod_p\left(1-\frac{\chi(p)}{p^s}\right)^{-1}.
\]
These definitions and relations are standard in modern accounts of Dirichlet's theorem [2,3].

### Mathematical Context and Formation

The concrete motivating problem is: given integers $q\geq 1$ and $a$ with $\gcd(a,q)=1$, prove that there are infinitely many primes
\[
p\equiv a\pmod q.
\]
The cases $q=1$ and $q=2$ reduce to the infinitude of all primes after at most deleting the prime $2$; their sole reduced-class indicator is already a principal character. The genuinely new separation problem begins when $q>2$, where the reduced-residue group is nontrivial.

Euler's analytic proof of the infinitude of all primes exploits the compatibility between integer factorization and the Euler product for $\zeta(s)$. For a prescribed progression with $q>2$, however, neither the unrestricted zeta function nor a direct Euclidean construction distinguishes an arbitrary desired residue class. In particular, constructing an integer congruent to $a$ modulo $q$ does not generally force any of its prime divisors to be congruent to $a$ modulo $q$.

The natural selector $1_{n\equiv a\, (q)}$ creates a sharper obstruction to adapting Euler’s product argument: for $q>2$ it is not a multiplicative arithmetic function. Consequently, the restricted Dirichlet series
\[
\sum_{n\equiv a\, (q)}n^{-s}
\]
does not have an Euler product obtained from that selector. Thus the two structures required by this particular strategy appeared misaligned: congruence classes had to be isolated, but Euler’s factorization-based analytic argument exposed primes through multiplicative coefficients.

The forming insight is to regard the reduced residue classes not merely as labels but as the finite abelian group $G_q$. Its one-dimensional characters are multiplicative functions, yet the complete family of them is rich enough, by orthogonality, to reconstruct the indicator of any individual reduced class. In modern notation,
\[
1_{n\equiv a\, (q)}
=\frac{1}{\varphi(q)}\sum_{\chi\bmod q}\overline{\chi(a)}\chi(n).
\]
Accordingly, one does not force a single residue-class indicator to be multiplicative. One decomposes that indicator into a finite linear combination of multiplicative modes and studies the corresponding $L(s,\chi)$. This is the mathematical content of the auxiliary root-of-unity-valued multiplicative factors introduced in Dirichlet's proof of the arithmetic-progression theorem [1]; the modern definition packages those factors as characters of $G_q$ [2].

### Essential Role

The Dirichlet character makes the residue-class restriction compatible with Euler's prime-product method in two exact steps. First, its complete multiplicativity yields
\[
\log L(s,\chi)
=\sum_p\sum_{k\geq 1}\frac{\chi(p)^k}{k p^{ks}}
\qquad (\Re(s)>1).
\]
Second, averaging these logarithms against $\overline{\chi(a)}$ and using character orthogonality gives
\[
\frac{1}{\varphi(q)}
\sum_{\chi\bmod q}\overline{\chi(a)}\log L(s,\chi)
=
\sum_{p^k\equiv a\, (q)}\frac{1}{k p^{ks}}.
\]
As $s\to1^+$, the terms with $k\geq2$ remain bounded, so the right-hand side differs from
\[
\sum_{p\equiv a\, (q)}p^{-s}
\]
by only a bounded quantity. This is the precise filtering operation unavailable to the unrestricted $\zeta(s)$ alone: multiplicativity exposes primes through Euler products, and orthogonality retains only the chosen congruence class [2,3].

The principal character supplies the divergent term because
\[
L(s,\chi_0)=\zeta(s)\prod_{p\mid q}(1-p^{-s}),
\]
which has a pole at $s=1$. The remaining analytic difficulty is concentrated into the statement
\[
L(1,\chi)\neq0\qquad(\chi\neq\chi_0).
\]
Once this nonvanishing is proved, the nonprincipal logarithms stay bounded near $1$, while the principal term grows like $\log(1/(s-1))$. It follows that
\[
\sum_{p\equiv a\, (q)}p^{-s}
=\frac{1}{\varphi(q)}\log\frac{1}{s-1}+O(1),
\qquad s\to1^+,
\]
and therefore the progression contains infinitely many primes.

Thus the character did not remove every hard step: nonvanishing at $s=1$ still had to be established. Its direct contribution was to replace, within the Euler-product strategy, an unavailable Euler product for one residue-class indicator by a finite family of genuine Euler products whose Fourier combination recovers that class. The resulting structural viewpoint is that distribution among reduced residue classes can be separated into multiplicative frequency components; for the motivating theorem, only the principal component is singular, while all nonprincipal components must be controlled.

## 3. Notes

A Dirichlet character is not an arbitrary irreducible character of a finite group: it is specifically a one-dimensional character of the abelian group $(\mathbb Z/q\mathbb Z)^\times$, extended by zero to all integers. Its stated modulus need not be minimal. The least modulus from which it is induced is its conductor, and a character whose modulus equals its conductor is called primitive. Dirichlet $L$-functions are constructions from the archived object, not the object itself.

## 4. Sources

[1] P. G. L. Dirichlet, “Beweis des Satzes, dass jede unbegrenzte arithmetische Progression, deren erstes Glied und Differenz ganze Zahlen ohne gemeinschaftlichen Factor sind, unendlich viele Primzahlen enthält,” *Abhandlungen der Königlich Preussischen Akademie der Wissenschaften zu Berlin* (1837).

[2] Tom M. Apostol, *Introduction to Analytic Number Theory*, Springer, 1976, Chapters 6–7.

[3] Andrew V. Sutherland, “Dirichlet $L$-functions, primes in arithmetic progressions,” MIT 18.785 Lecture Notes 18, 2017, https://math.mit.edu/classes/18.785/2017fa/LectureNotes18.pdf.
