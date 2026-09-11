# Mathematical Object Origin Archive | Tor Functor

## 1. Archive Information

- Standard Name: Tor functor
- Mathematical Field: Homological Algebra; Commutative Algebra
- Abstract: The functors \(\operatorname{Tor}_n^R(-,-)\) measure, degree by degree, the failure of tensor product over a ring \(R\) to preserve exact sequences. They are formed by replacing one module with a projective resolution, tensoring that resolution with the other module, and taking homology. This construction turns the loss of kernels under tensoring into canonical algebraic objects and exact-sequence calculations.

## 2. Core Record

### Precise Description

Let \(R\) be a commutative ring and let \(M,N\) be \(R\)-modules. Choose a projective resolution
\[
\cdots \longrightarrow P_2\longrightarrow P_1\longrightarrow P_0\longrightarrow M\longrightarrow 0.
\]
The Tor modules are
\[
\operatorname{Tor}_n^R(M,N)=H_n(P_\bullet\otimes_R N),\qquad n\geq 0.
\]
Up to canonical natural isomorphism, this is independent of the chosen resolution; resolving \(N\) instead gives the same result. Thus \(\operatorname{Tor}_n^R(-,-)\) is a bifunctor, \(\operatorname{Tor}_0^R(M,N)\cong M\otimes_RN\), and the positive-degree Tor functors are the left derived functors of tensor product [1][2]. Equivalently,
\[
\operatorname{Tor}_n^R(M,N)\cong H^{-n}(M\otimes_R^{\mathbf L}N).
\]

For a short exact sequence \(0\to M'\to M\to M''\to0\), these functors supply a natural long exact sequence
\[
\cdots\to \operatorname{Tor}_1^R(M,N)\to \operatorname{Tor}_1^R(M'',N)
\to M'\otimes_RN\to M\otimes_RN\to M''\otimes_RN\to0,
\]
with the omitted higher terms following the usual pattern
\(\operatorname{Tor}_n(M',N)\to\operatorname{Tor}_n(M,N)\to\operatorname{Tor}_n(M'',N)\to\operatorname{Tor}_{n-1}(M',N)\) [2][3].

### Mathematical Context and Formation

The motivating problem class is to determine what happens to an exact sequence of modules after tensoring. The functor \(-\otimes_RN\) preserves cokernels, so from
\[
0\to M'\to M\to M''\to0
\]
one always obtains
\[
M'\otimes_RN\to M\otimes_RN\to M''\otimes_RN\to0.
\]
The missing assertion is injectivity at the left: tensoring can collapse a nonzero element of \(M'\otimes_RN\), and the ordinary tensor product contains no preceding term whose image identifies that kernel.

This obstruction already appears over \(\mathbb Z\). Tensor the exact sequence
\[
0\to\mathbb Z\xrightarrow{\,m\,}\mathbb Z\to\mathbb Z/m\mathbb Z\to0
\]
with \(\mathbb Z/n\mathbb Z\). The first resulting map is multiplication by \(m\) on \(\mathbb Z/n\mathbb Z\), which need not be injective. Its kernel is abstractly isomorphic to \(\mathbb Z/\gcd(m,n)\mathbb Z\). Torsion-element calculations expose this particular failure, but they do not by themselves provide a uniform, functorial hierarchy of obstructions for arbitrary modules over arbitrary rings.

The formation of Tor addresses exactly that deficiency. Projective modules are used because tensoring a split exact sequence involving a projective module creates no hidden kernel, while every module admits a free, hence projective, resolution. Such a resolution expands \(M\) into projective generators together with successive modules of relations, or syzygies. After tensoring the resolution with \(N\), failure of exactness can occur, but it is now visible as homology: cycles record relations that survive tensoring, and boundaries record those already forced from one degree higher. Taking \(H_n(P_\bullet\otimes_RN)\) therefore converts a presentation-dependent calculation into the resolution-independent functors \(\operatorname{Tor}_n^R(M,N)\). In the displayed integer example,
\[
\operatorname{Tor}_1^{\mathbb Z}(\mathbb Z/m\mathbb Z,\mathbb Z/n\mathbb Z)
\cong \mathbb Z/\gcd(m,n)\mathbb Z,
\]
and its connecting map identifies it with the kernel of multiplication by \(m\) on \(\mathbb Z/n\mathbb Z\).

### Essential Role

Tor makes the lost-kernel part of the tensor-exactness problem tractable. For every short exact sequence above, exactness at \(M'\otimes_RN\) states precisely that
\[
\ker(M'\otimes_RN\to M\otimes_RN)
=
\operatorname{im}\!\left(\operatorname{Tor}_1^R(M'',N)\to M'\otimes_RN\right).
\]
Thus \(\operatorname{Tor}_1\), together with its connecting homomorphism, does not merely announce that tensoring failed: it computes the elements responsible for the failure. Higher \(\operatorname{Tor}_n\) continue this correction through the successive syzygies, replacing an isolated defect by a natural long exact sequence that supports recursive computation.

The mechanism is specific to the definition. Projective resolutions move the nonexact input into a complex whose terms are well behaved under tensoring; homology then retains exactly the discrepancy between cycles and boundaries created by tensoring. Resolution independence makes those discrepancies intrinsic to \(M\) and \(N\), rather than artifacts of chosen generators and relations. In particular, an \(R\)-module \(N\) is flat exactly when \(\operatorname{Tor}_1^R(M,N)=0\) for every \(R\)-module \(M\) [3]. Tor therefore reformulates the qualitative question “does tensoring by \(N\) preserve all injections?” as a canonical vanishing criterion and supplies graded obstruction modules when the answer is no. This correction of tensor product, rather than Tor's later use in other theories, is its direct role in the motivating problem.

## 3. Notes

For noncommutative \(R\), one takes a right \(R\)-module in one variable and a left \(R\)-module in the other. The name “Tor” is related to tensor product and should not be conflated with the torsion submodule of a single module: over \(\mathbb Z\), \(\operatorname{Tor}_1\) recovers familiar torsion interactions, but the Tor functors are defined over general rings and in all nonnegative degrees. The derived tensor product packages the entire family into one object, whereas this archive's object is the family of homology functors \(\operatorname{Tor}_n^R\).

## 4. Sources

[1] Henri Cartan and Samuel Eilenberg, *Homological Algebra*, Princeton University Press, 1956.

[2] Charles A. Weibel, *An Introduction to Homological Algebra*, Cambridge University Press, 1994.

[3] The Stacks Project Authors, “Tor groups and flatness,” Section 10.75, Tag 00LY, https://stacks.math.columbia.edu/tag/00LY.
