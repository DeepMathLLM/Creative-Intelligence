# Mathematical Object Origin Archive | Palm Distribution

## 1. Archive Information

- Standard Name: Palm distribution
- Mathematical Field: Probability Theory and Stochastic Processes
- Abstract: The Palm distribution is the probability law of a point process as viewed from one of its typical points. It was formed to analyze event-centered questions in random streams, notably telephone-call traffic, for which the ordinary stationary law describes a typical time rather than a typical arrival and literal conditioning on an arrival at a prescribed continuous time is usually conditioning on a probability-zero event.

## 2. Core Record

### Precise Description

Let \(\Phi\) be a stationary, locally finite, simple point process on \(\mathbb{R}\), regarded as a random counting measure with law \(P\), and suppose its intensity satisfies
\[
0<\lambda=\mathbb{E}\Phi([0,1])<\infty.
\]
Let \(\mathcal N\) denote the configuration space, and define the translation \(\theta_t\varphi\) by
\[
(\theta_t\varphi)(A)=\varphi(A+t),
\]
so that a point of \(\varphi\) at \(t\) is moved to the origin. The Palm distribution \(P^0\) of \(\Phi\) is the probability measure on \(\mathcal N\) characterized, for any bounded Borel set \(B\) of positive Lebesgue measure, by
\[
P^0(C)=\frac{1}{\lambda |B|}\,
\mathbb{E}\!\left[\int_B
\mathbf 1\{\theta_t\Phi\in C\}\,\Phi(dt)\right].
\]
Stationarity makes the right-hand side independent of the choice of \(B\). Equivalently, \(P^0\) is characterized by the refined Campbell formula
\[
\mathbb{E}\!\left[\int_{\mathbb R} f(t,\theta_t\Phi)\,\Phi(dt)\right]
=
\lambda\int_{\mathbb R}\int_{\mathcal N} f(t,\eta)\,P^0(d\eta)\,dt
\]
for every nonnegative measurable \(f\). For a simple process, \(P^0\)-almost every configuration has a point at the origin. The reduced Palm distribution is the law obtained after deleting this distinguished point; it is related to, but is not the same object as, \(P^0\).

More generally, for a point process on a suitable state space with intensity measure \(\Lambda\), Palm kernels \(P^x\) arise by disintegrating its Campbell measure:
\[
\mathbb{E}\!\left[\int h(x,\Phi)\,\Phi(dx)\right]
=
\int\!\int h(x,\varphi)\,P^x(d\varphi)\,\Lambda(dx).
\]
The stationary \(P^0\) above is the translation-normalized version of this construction.

### Mathematical Context and Formation

The motivating problem class is the analysis of stationary random event streams from the viewpoint of an event. In telephone traffic, for example, call initiations may be represented by points \(\{T_n\}\) on the time line. Questions such as the distribution of neighboring calls, the traffic environment encountered by an arrival, or an average quantity recorded once per call require the law seen from a typical \(T_n\), not the law seen at an independently selected clock time. Palm's work on fluctuations in telephone traffic supplied the event-centered viewpoint from which the modern object takes its name [1].

Two linked mathematical obstructions prevent the ordinary stationary law from answering that problem. First, for a stationary point process with diffuse intensity,
\[
\mathbb{P}\{\Phi(\{0\})=1\}=0,
\]
so the phrase “condition on an arrival at time \(0\)” is not defined by the elementary ratio formula for conditional probability. Second, sampling times and sampling events produce different biases. A clock-time observer overweights long interarrival gaps, whereas an arrival-indexed observer samples one configuration per point. Thus stationarity and the scalar intensity \(\lambda\) do not determine the required event-centered law, and simply translating the original distribution to time zero still leaves a typical time rather than a typical event.

The decisive construction is to weight observations by the random counting measure itself. One first forms the Campbell measure by accumulating \((t,\Phi)\) once for every event time \(t\); one then shifts that event to the origin and normalizes by the mean number \(\lambda |B|\) of events in an observation window. This produces the probability measure \(P^0\) above without conditioning on a null event. Modern measure-theoretic Palm theory expresses the same insight as disintegration of the Campbell measure [2][3]. Accordingly, “the law given a point at the origin” is a valid interpretation of \(P^0\), but the event-weighting or disintegration identity—not a literal elementary conditional probability—is its definition.

### Essential Role

The Palm distribution makes the passage from time averages to event averages mathematically tractable. If \(F\) is a statistic of the configuration around an arrival, then
\[
\frac{1}{\lambda |B|}\,
\mathbb E\!\left[\sum_{t\in\Phi\cap B}F(\theta_t\Phi)\right]
=
\mathbb E^0[F(\Phi)].
\]
The left side is directly formulated in terms of observed events, while the right side is expectation under a genuine probability law centered at a typical event. The normalization by \(\lambda |B|\) removes dependence on the observation-window size, the counting-measure weight enforces point sampling rather than clock-time sampling, and the translation \(\theta_t\) puts different arrivals into one common coordinate system. These are exactly the features needed to overcome the null-conditioning and sampling-bias obstructions.

Consequently, distributions of interarrival spacings and other arrival-centered traffic statistics can be defined and compared under \(P^0\), while the refined Campbell formula transfers calculations back to the original stationary process. The deeper structural change is that “typical” is recognized as relative to a sampling measure: Lebesgue measure yields a typical time, whereas \(\Phi(dt)\) yields a typical point. The Palm distribution does not by itself solve a queueing or traffic model; its direct contribution is to supply the correct event-centered probability law and the identity connecting it to ordinary stationary observations.

## 3. Notes

For a stationary Poisson process, the Palm distribution is the law of the original process with an additional point at the origin (Slivnyak's theorem). This special simplification is not valid for general point processes, where conditioning on a typical point may alter the distribution of the surrounding configuration. Palm distributions also differ from arbitrary conditioning on the count in a fixed positive-length interval.

## 4. Sources

[1] C. Palm, *Intensitätsschwankungen im Fernsprechverkehr*, Ericsson Technics, no. 44, 1943, pp. 1–189; English translation: *Intensity Variations in Telephone Traffic*, North-Holland, 1988.

[2] D. J. Daley and D. Vere-Jones, *An Introduction to the Theory of Point Processes, Volume I: Elementary Theory and Methods*, 2nd ed., Springer, 2003, chapters on Campbell measures and Palm theory.

[3] G. Last and M. Penrose, *Lectures on the Poisson Process*, Cambridge University Press, 2018, chapters on Palm distributions and the Mecke equation.
