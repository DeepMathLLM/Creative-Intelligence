# Mathematical Object Origin Archive | Jordan canonical form

## 1. Archive Information

- Standard Name: Jordan canonical form
- Mathematical Field: Linear Algebra
- Abstract: The Jordan canonical form is a block-diagonal representative of a similarity class of finite-dimensional linear operators whose characteristic polynomial splits. It was formed to solve the reduction problem for linear substitutions under change of coordinates when ordinary diagonalization fails: generalized-eigenvector chains retain both the eigenvalues and the precise nilpotent defect at each eigenvalue.

## 2. Core Record

### Precise Description

Let \(T:V\to V\) be a linear operator on a finite-dimensional vector space over a field \(F\), and assume that the characteristic polynomial of \(T\) splits over \(F\). A Jordan block of size \(r\) with eigenvalue \(\lambda\in F\) is
\[
J_r(\lambda)=
\begin{pmatrix}
\lambda&1&0&\cdots&0\\
0&\lambda&1&\ddots&\vdots\\
\vdots&\ddots&\ddots&\ddots&0\\
0&\cdots&0&\lambda&1\\
0&\cdots&\cdots&0&\lambda
\end{pmatrix}.
\]
A Jordan canonical form of \(T\) is a block-diagonal matrix
\[
J=\operatorname{diag}\bigl(J_{r_1}(\lambda_1),\ldots,J_{r_s}(\lambda_s)\bigr)
\]
such that \([T]_{\mathcal B}=J\) for some basis \(\mathcal B\) of \(V\), equivalently \(A=PJP^{-1}\) for any matrix \(A\) representing \(T\). Such a form exists under the splitting assumption and is unique up to permutation of its blocks [2]. In particular, it exists over every algebraically closed field.

For a fixed eigenvalue \(\lambda\), the basis vectors in a block form a chain \(v_1,\ldots,v_r\) satisfying
\[
(T-\lambda I)v_1=0,\qquad (T-\lambda I)v_j=v_{j-1}\quad(2\le j\le r).
\]
Thus the block records the scalar action \(\lambda I\) together with one indecomposable nilpotent chain. If
\(d_k=\dim\ker(T-\lambda I)^k\) and \(d_0=0\), then \(d_k-d_{k-1}\) is the number of \(\lambda\)-blocks of size at least \(k\); consequently these intrinsic kernel dimensions determine all block sizes.

### Mathematical Context and Formation

The motivating problem was the reduction and classification of finite-dimensional linear substitutions under a change of coordinates. Two matrices \(A\) and \(P^{-1}AP\) describe the same linear substitution in different bases, so a satisfactory reduction had to choose a simple representative for every similarity class and disclose exactly when two substitutions were equivalent. Diagonalization gives an ideal answer when eigenvectors span the space. It does not solve the general problem: with a repeated eigenvalue, the eigenspace \(\ker(T-\lambda I)\) can have dimension smaller than the eigenvalue's algebraic multiplicity. The characteristic polynomial then identifies the eigenvalue but not the missing directional structure. For example,
\[
\begin{pmatrix}\lambda&0\\0&\lambda\end{pmatrix}
\quad\text{and}\quad
\begin{pmatrix}\lambda&1\\0&\lambda\end{pmatrix}
\]
have the same characteristic polynomial but are not similar.

The decisive enlargement is to replace eigenvectors alone by generalized eigenvectors. On the generalized eigenspace
\(V_\lambda=\ker(T-\lambda I)^N\) for sufficiently large \(N\), the operator has the form \(\lambda I+N_\lambda\) with \(N_\lambda\) nilpotent. Decomposing this nilpotent action into chains
\(N_\lambda v_j=v_{j-1}\) supplies the vectors missing from an eigenbasis. Writing each chain in order produces one block \(J_r(\lambda)\), and the primary decomposition into generalized eigenspaces assembles the blocks for distinct eigenvalues. Jordan's treatment of canonical reduction for linear substitutions appears in his *Traité des substitutions et des équations algébriques* [1]. The account here describes the mathematical formation in modern language; it does not claim that Jordan used the modern terminology of generalized eigenspaces or modules.

### Essential Role

The Jordan canonical form makes the previously unresolved non-diagonalizable part of the similarity problem explicit. Its diagonal entries retain the eigenvalues, while the superdiagonal ones partition the nilpotent defect into chain lengths. Hence it distinguishes operators that eigenvalues, characteristic polynomials, and eigenspace dimensions alone may fail to distinguish. The intrinsic quantities \(\dim\ker(T-\lambda I)^k\) recover the block partition, so the construction proves both that every split operator has such a reduced representative and that two such operators are similar exactly when their block multisets agree.

This mechanism does not force a defective operator to become diagonal. Instead, it reformulates the obstruction to diagonalization as finite combinatorial data: the sizes of the nilpotent chains. The original reduction problem is thereby separated into a semisimple datum (the eigenvalues) and a nilpotent datum (the block sizes). In particular, diagonalizability becomes the precise special case in which every Jordan block has size \(1\). That structural separation, rather than later computational applications of Jordan form, is its direct contribution to the motivating classification problem.

## 3. Notes

Over a field on which the characteristic polynomial does not split, a Jordan form need not exist over the original field; rational canonical form is the corresponding field-independent similarity normal form. The displayed convention uses ones on the superdiagonal; the transposed convention is equivalent and also common. Exact Jordan form is a similarity invariant but is numerically unstable under small perturbations, a limitation separate from its algebraic classification role.

## 4. Sources

[1] Camille Jordan, *Traité des substitutions et des équations algébriques*, Gauthier-Villars, Paris, 1870.

[2] Kenneth Hoffman and Ray Kunze, *Linear Algebra*, 2nd ed., Prentice-Hall, 1971, Chapters 6–7.
