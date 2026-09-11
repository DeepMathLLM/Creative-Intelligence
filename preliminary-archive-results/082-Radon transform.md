# Mathematical Object Origin Archive | Radon Transform

## 1. Archive Information

- Standard Name: Radon transform
- Mathematical Field: Harmonic Analysis and Integral Geometry
- Abstract: The Radon transform assigns to a function its integrals over lines, or more generally over affine hyperplanes. It arose from the concrete inverse problem of determining a planar function from all of its line integrals. Radon's original construction made those integrals into a function on the space of lines and reduced recovery at each point to inversion of an Abel integral equation.

## 2. Core Record

### Precise Description

For \(f\in\mathcal S(\mathbb R^n)\), the Radon transform is
\[
(Rf)(\theta,s)=\int_{\{x\in\mathbb R^n:x\cdot\theta=s\}}f(x)\,d\mathcal H^{n-1}(x),
\qquad (\theta,s)\in S^{n-1}\times\mathbb R,
\]
where \(d\mathcal H^{n-1}\) is Euclidean hypersurface measure. Because \((\theta,s)\) and \((-\theta,-s)\) represent the same unoriented hyperplane,
\[
(Rf)(-\theta,-s)=(Rf)(\theta,s).
\]
The planar case \(n=2\), in which the integrating manifolds are straight lines, is the object used in Radon's original determination problem [1, 2]. The Schwartz assumption is a convenient modern domain; the definition extends to broader classes of functions, measures, and distributions under suitable hypotheses [3].

A geometric reduction central to the planar inversion can be stated explicitly. Fix \(P\in\mathbb R^2\), and define the circular mean
\[
m_P(r)=\frac1{2\pi}\int_0^{2\pi}f\bigl(P+r(\cos\varphi,\sin\varphi)\bigr)\,d\varphi.
\]
Average the line data over all lines tangent to the circle of radius \(q\) centered at \(P\):
\[
A_P(q)=\frac1{2\pi}\int_0^{2\pi}
(Rf)\bigl(\theta(\alpha),P\cdot\theta(\alpha)+q\bigr)\,d\alpha,
\quad \theta(\alpha)=(\cos\alpha,\sin\alpha).
\]
For rapidly decreasing \(f\), a change to polar coordinates gives
\[
A_P(q)=2\int_q^\infty \frac{m_P(r)r}{\sqrt{r^2-q^2}}\,dr.
\]
Writing \(u=q^2\), \(v=r^2\), \(B_P(u)=A_P(\sqrt u)\), and \(h_P(v)=m_P(\sqrt v)\), this becomes the Abel equation
\[
B_P(u)=\int_u^\infty\frac{h_P(v)}{\sqrt{v-u}}\,dv.
\]
Its inversion determines \(h_P\), hence \(f(P)=m_P(0)=h_P(0)\).

### Mathematical Context and Formation

The documented problem in Radon's 1917 paper is the inversion of a functional transformation: a point-function \(f(x,y)\) is integrated over every straight line \(g\), producing a line-function \(F(g)\); one asks which line-functions arise this way and, above all, whether and how \(f\) is determined by \(F\) [1, 2]. This was not merely a later application of an existing transform: the line-function now called \(Rf\) was organized in direct response to that determination problem.

The exact difficulty is that a single datum \(F(g)\) collapses all values of \(f\) along an entire line. Pointwise algebra cannot separate them, and using only one family of parallel lines loses one spatial variable. The full family of lines contains enough information, but its information is distributed through incidence relations among lines, circles, and points; an inversion mechanism had to combine the data in a geometrically controlled way.

Radon explicitly credited the route to his solution to Funk's treatment of an analogous spherical problem: recovery from integrals over great circles had been reduced to an Abel integral equation [1, 2]. In the planar problem, Radon fixed a point \(P\), averaged the known line-function over lines tangent to circles centered at \(P\), and obtained an Abel-type relation between those known averages and circular means of the unknown function. Abel inversion then recovers the limiting circular mean at radius zero, namely \(f(P)\). Thus the historically documented formative mechanism was integral-geometric averaging followed by Abel inversion, not the Fourier-slice argument commonly used in modern accounts.

As interpretive synthesis, the direction-offset parametrization can be understood as the minimum data structure needed for that mechanism: the direction indexes which line family is used, while the offset lets those lines be assembled as tangents to circles about an arbitrary reconstruction point. This interpretation explains the definition's fit to the problem; it is not a claim about Radon's stated historical reasoning beyond the construction and Abel method documented in his paper.

### Essential Role

The transform made the uniqueness and reconstruction parts of the original determination problem tractable. Its essential move was to retain every line integral as a value of one line-function rather than attempting to undo any integral separately. For each desired point \(P\), the incidence average \(A_P(q)\) combines exactly those measured lines tangent to the radius-\(q\) circle about \(P\). The displayed Abel equation converts this nonlocal two-parameter data into a one-variable integral equation for the circular mean \(m_P\). Abel inversion recovers \(m_P(0)=f(P)\), and repeating the construction for every \(P\) reconstructs the function. In particular, zero line data force every recovered point value to vanish, yielding uniqueness under the stated regularity assumptions.

This directly overcomes the original obstacle: line integration had mixed point values irreversibly when viewed one line at a time, but the geometry of the complete line family creates overlapping measurements whose tangent-line averages isolate radial information around each point. The deeper structural viewpoint is a duality between functions on points and functions on lines, with incidence-based averaging providing a route back from the latter to the former. That point-line functional transformation, together with its explicit inversion, is the object's original contribution.

A separate modern explanation uses the Fourier-slice identity
\[
\mathcal F_s[(Rf)(\theta,\cdot)](\sigma)=\widehat f(\sigma\theta),
\]
which shows that Fourier transformation in the offset recovers radial restrictions of \(\widehat f\) and hence gives another proof of injectivity and reconstruction [3]. This is a retrospective structural interpretation, not the method asserted here to have produced Radon's 1917 construction. Likewise, frequency filtering followed by integration over directions is a later standard reconstruction formulation, not part of the archive's account of the object's original formation.

## 3. Notes

In \(\mathbb R^2\), affine hyperplanes are lines, so the Radon and planar X-ray transforms have the same defining integral. In dimensions \(n>2\), the hyperplane Radon transform is distinct from the X-ray transform over lines. Symmetry under \((\theta,s)\mapsto(-\theta,-s)\) is necessary but not sufficient for a function to be Radon data; range descriptions impose further consistency conditions, including moment conditions [3].

## 4. Sources

[1] Johann Radon, “Über die Bestimmung von Funktionen durch ihre Integralwerte längs gewisser Mannigfaltigkeiten,” *Berichte über die Verhandlungen der Königlich-Sächsischen Akademie der Wissenschaften zu Leipzig, Mathematisch-Physische Klasse* 69 (1917), 262–277.

[2] Johann Radon, “On the Determination of Functions from Their Integral Values Along Certain Manifolds,” trans. P. C. Parks, *IEEE Transactions on Medical Imaging* 5, no. 4 (1986), 170–176, doi:10.1109/TMI.1986.4307775.

[3] Sigurdur Helgason, *The Radon Transform*, 2nd ed., Progress in Mathematics 5, Birkhäuser, 1999, Chapters I–II.
