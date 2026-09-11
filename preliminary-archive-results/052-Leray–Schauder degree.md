# Mathematical Object Origin Archive | Leray–Schauder Degree

## 1. Archive Information

- Standard Name: Leray–Schauder degree
- Mathematical Field: Functional Analysis (nonlinear functional analysis and topological degree theory)
- Abstract: The Leray–Schauder degree is an integer-valued invariant for compact perturbations of the identity on a real Banach space. It was formed to make topological continuation available for nonlinear functional equations—especially equations obtained from nonlinear integral and elliptic boundary-value problems—when a priori bounds were available but finite-dimensional Brouwer degree and local continuation methods did not directly apply.

## 2. Core Record

### Precise Description

Let \(X\) be a real Banach space, let \(\Omega\subset X\) be bounded and open, and let \(K:\overline{\Omega}\to X\) be compact, meaning that it is continuous and \(K(\overline{\Omega})\) is relatively compact. For
\[
F=I-K
\]
and \(y\notin F(\partial\Omega)\), the Leray–Schauder degree is an integer
\[
\deg_{LS}(I-K,\Omega,y)\in\mathbb Z.
\]

Its construction reduces the infinite-dimensional problem to Brouwer degree. Compactness permits a uniformly close approximation \(K_\varepsilon\) whose range lies in a finite-dimensional subspace \(E_\varepsilon\subset X\), chosen also to contain \(y\). For a sufficiently close approximation, \(y\notin (I-K_\varepsilon)(\partial\Omega)\), and one sets
\[
\deg_{LS}(I-K,\Omega,y)
 =\deg_B\!\left((I-K_\varepsilon)|_{\Omega\cap E_\varepsilon},\,
                    \Omega\cap E_\varepsilon,\,y\right).
\]
Here the restricted map is understood as \(x\mapsto x-K_\varepsilon(x)\) from \(E_\varepsilon\) to itself. The stabilization theorem shows that this integer is independent of all sufficiently accurate finite-dimensional approximations and of the finite-dimensional space used [2].

The resulting degree inherits the decisive properties of Brouwer degree: normalization, additivity over disjoint regions containing the solution set, existence when the degree is nonzero, and invariance under admissible compact homotopies. In particular,
\[
\deg_{LS}(I-K,\Omega,y)\ne0
\quad\Longrightarrow\quad
(I-K)x=y\text{ for some }x\in\Omega.
\]
For fixed-point equations \(x=K(x)\), one uses \(y=0\).

### Mathematical Context and Formation

The motivating problem class was to prove existence throughout a parameter family of nonlinear functional equations
\[
x-K(x,\lambda)=0,\qquad 0\leq\lambda\leq1,
\]
on an infinite-dimensional function space. Nonlinear integral equations and nonlinear elliptic boundary-value problems enter this form after the principal linear part is solved and its inverse, often an integral or Green operator, is composed with the nonlinearity. In the relevant settings this composition is completely continuous (compact on bounded sets). The practical continuation scheme starts from a tractable equation at \(\lambda=0\) and seeks a solution of the target equation at \(\lambda=1\) [1], [2].

The obstacle is that a family of solutions need not be a single graph that can be followed by the implicit-function theorem: linearization can become singular, solutions can bifurcate, and uniqueness can be lost. A priori estimates may nevertheless show that every possible solution remains in some bounded open set \(\Omega\), so no solution lies on \(\partial\Omega\) during the deformation. Such estimates control escape but, by themselves, do not force a solution to exist at every parameter. Brouwer degree supplied exactly the missing global invariant in finite dimensions, but it was not directly defined for arbitrary maps between infinite-dimensional Banach spaces; in particular, the finite-dimensional compactness and homological setting behind its standard construction are absent.

The decisive insight was to restrict the required extension rather than seek a degree for every infinite-dimensional map. For \(I-K\), compactness of \(K\) makes its image uniformly approximable by maps with finite-dimensional range. Brouwer degree can therefore be applied on a finite-dimensional slice, while stability under sufficiently close approximations makes the resulting integer intrinsic. Leray and Schauder developed this construction together with its continuation principle in their 1934 work on topology and functional equations [1]. Thus the object joins three ingredients that fit the motivating equations: compactness provides finite-dimensional reduction, a priori bounds provide the boundary exclusion needed for admissibility, and degree supplies a homotopy invariant.

### Essential Role

For the continuation problem, suppose \(H:\overline{\Omega}\times[0,1]\to X\) is a compact homotopy and
\[
x-H(x,\lambda)\ne0
\quad\text{for all }(x,\lambda)\in\partial\Omega\times[0,1].
\]
Leray–Schauder degree makes the integer
\[
\deg_{LS}(I-H(\cdot,\lambda),\Omega,0)
\]
independent of \(\lambda\). If the starting equation has a computable nonzero degree—commonly the normalization value \(1\)—then the target degree at \(\lambda=1\) is also nonzero, and the target equation has a solution. When an a priori estimate gives \(\|x\|<R\) for every solution along the homotopy, one may take \(\Omega=B_R(0)\); the analytic estimate then becomes precisely the no-boundary-solution hypothesis needed by the degree [2], [3].

This mechanism made the existence step tractable without requiring uniqueness, an invertible derivative, or an explicit continuous choice of solutions. Singular points and bifurcations can obstruct local tracking, but they do not change the degree unless solutions cross the chosen boundary (or admissibility otherwise fails). The finite-dimensional approximation in the definition overcomes the lack of a general infinite-dimensional Brouwer degree, while compactness guarantees that this reduction retains the relevant fixed-point information. The deeper structural viewpoint is that continuation is governed by a global obstruction: a nonzero algebraic solution count cannot disappear during an admissible deformation. This separates the problem into an analytic part—compact reformulation and a priori bounds—and a topological part—degree invariance and nonzero degree—rather than treating each parameter value as an unrelated existence problem.

## 3. Notes

The Leray–Schauder degree is not a degree for arbitrary nonlinear maps between Banach spaces; its classical domain is the special class \(I-K\) with \(K\) compact. It is closely related to the fixed-point index: for a compact self-map, the fixed-point index on an admissible open set equals the Leray–Schauder degree of \(I-K\) at \(0\). The Leray–Schauder continuation theorem is a consequence built from the degree and should not be identified with the degree itself.

## 4. Sources

[1] Jean Leray and Jules Schauder, “Topologie et équations fonctionnelles,” *Annales scientifiques de l’École Normale Supérieure*, 3e série, 51 (1934), 45–78. https://doi.org/10.24033/asens.836

[2] Jean Mawhin, “Leray–Schauder Degree: A Half Century of Extensions and Applications,” *Topological Methods in Nonlinear Analysis* 14 (1999), 195–228. https://doi.org/10.12775/TMNA.1999.029

[3] Jean Mawhin, “Leray–Schauder Continuation Theorems in the Absence of A Priori Bounds,” *Topological Methods in Nonlinear Analysis* 9 (1997), 179–200. https://projecteuclid.org/euclid.tmna/1476841908
