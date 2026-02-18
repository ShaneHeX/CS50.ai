# Review

[Bayes' Theorem](https://www.mathsisfun.com/data/bayes-theorem.html)

[Joint Probability - GeeksforGeeks](https://www.geeksforgeeks.org/engineering-mathematics/joint-probability-concept-formula-and-examples/)

[Probability mass function](https://en.wikipedia.org/wiki/Probability_mass_function)

[Joint probability distribution](https://en.wikipedia.org/wiki/Joint_probability_distribution)

[3Blue1Brown](https://www.3blue1brown.com/topics/probability#probability)

## **Probability mass function**

A **probability mass function** (sometimes called *probability function* or *frequency function)* is a function that gives the probability that a discrete random variable is exactly equal to some value.

> Formal definition: $P(X=x)=p$
> 

The probabilities associated with all (hypothetical) values must be non-negative and sum up to 1,

$$
\sum_xP(x)=1 \\
and \\
P(x)\ge 0
$$

## **Joint probability distribution**

### Discrete case

Given random variables $X,Y,...$, that are defined on the same probability space, the **multivariate** or **joint probability distribution** for $X,Y,…$ is a probability distribution that gives the probability that each of X,Y,… falls in discrete set of values specified for that variable.

The joint probability mass function of two discrete random variables $X, Y$ is:

$$

\mathbb{P}_{X,Y}(x, y) = \mathbb{P}(X = x \text{ and } Y = y)

$$

Written in terms of conditional distributions:

$$
\mathbb{P}_{X,Y}(x, y) = \mathbb{P}(Y = y \mid X = x) \cdot \mathbb{P}(X = x) = \mathbb{P}(X = x \mid Y = y) \cdot \mathbb{P}(Y = y)
$$

where $\mathbb{P}(Y = y \mid X = x)$ is the probability of $Y = y$ given that $X = x$.

*For independent variables:*

Two discrete random variables $X$ and $Y$ are independent if and only if the joint probability mass function satisfies

$$
\mathbb P(X = x \text{ and } Y = y) = \mathbb P(X = x) \cdot \mathbb P(Y = y)
$$

for all $x$ and $y$.

## **Bayesian network**

A Bayesian network (also known as a Bayes network, Bayes net, belief network, or decision network) is a probabilistic graphical model that represents a set of variables and their conditional dependencies via a directed acyclic graph (DAG).

Bayesian networks are ideal for taking an event that occurred and predicting the likelihood that any one of several possible known causes was the contributing factor.

### **Definitions and concepts**

For the following, let $*G = (V,E)*$ be a directed acyclic graph (DAG) and let $*X = (X_v),v ∈ V*$be a set of random variables indexed by $*V*$.

Factorization definition:

$*X*$ is a Bayesian network with respect to $*G*$ if its joint probability mass function (with respect to a product measure) can be written as a product of the individual probability mass functions, conditional on their parent variables.

$$
P(X) = \prod_{v \in V} P\left(X_v \mid X_{pa(v)}\right)
$$