# Lecture 2: Uncertainty

Date: 2026年2月5日 → 2026年2月18日

[Review](Lecture%202%20Uncertainty/Review%202feabebeda9f80d48ed1c07ffc6b504e.md)

# **Uncertainty**

Last lecture, we discussed how AI can represent and derive new knowledge. However, often, in reality, the AI has only partial knowledge of the world, leaving space for uncertainty. Still, we would like our AI to make the best possible decision in these situations. For example, when predicting weather, the AI has information about the weather today, but there is no way to predict with $100\%$ accuracy the weather tomorrow. Still, we can do better than chance, and today’s lecture is about how we can create AI that makes optimal decisions given limited information and uncertainty.

## **Probability**

Uncertainty can be represented as a number of events and the likelihood, or probability, of each of them happening.

### **Possible Worlds**

Every possible situation can be thought of as a world, represented by the lowercase Greek letter omega $\omega$.

### **Axioms in Probability**

- $0 \le P(\omega) \le 1$: every value representing probability must range between $0$ and $1$.
    - ***Zero*** is an impossible event, like rolling a standard die and getting a $7$.
    - ***One*** is an event that is certain to happen, like rolling a standard die and getting a value less than $10$.
    - In general, the higher the value, the more likely the event is to happen.
- The probabilities of every possible event, when summed together, are equal to $1$.

$$
\sum_{\omega \in \Omega} P(\omega) = 1
$$

### **Unconditional Probability**

Unconditional probability is the degree of belief in a proposition in the absence of any other evidence.

## **Random Variables**

A random variable is a variable in probability theory with a domain of possible values that it can take on.
For example, to represent possible outcomes when rolling a die, we can define a random variable **$*Roll*$**, that can take on the values $\left\{ 1, 2, 3, 4, 5, 6 \right\}$. To represent the status of a flight, we can define a variable **$*Flight*$** that takes on the values $\left\{on time, delayed, canceled\right\}$.

### Probability Distribution

Often, we are interested in the probability with which each value occurs. We represent this using a probability distribution. For example,

$$
P(Flight=\text{on time})=0.6 \\
P(Flight=\text{delayed})=0.3 \\
P(Flight=\text{canceled})=0.1
$$

To interpret the probability distribution with words, this means that there is a $60\%$ chance that the flight is on time, $30\%$ chance that it is delayed, and $10\%$ chance that it is canceled. Note that, as shown previously, the sum the probabilities of all possible outcomes is $1$.

A probability distribution can be represented more succinctly as a vector. For example, **$P(Flight) = \left<0.6, 0.3, 0.1\right>$**. For this notation to be interpretable, the values have a set order (in our case, ***on time, delayed, canceled***).

### **Independence**

Independence is the knowledge that the occurrence of one event does not affect the probability of the other event.

<aside>
❗

Independence can be defined mathematically: events $*a*$ and $*b*$ are independent if and only if the probability of $*a*$ and $*b*$ is equal to the probability of $*a*$ times the probability of $*b*$: $P(a \land b) = P(a)P(b)$.

</aside>

## **Conditional Probability**

Conditional probability is the degree of belief in a proposition given some evidence that has already been revealed.

Conditional probability is expressed using the following notation: $P(a \mid b)$, meaning “the probability of event $*a*$ occurring given that we know event $*b*$ to have occurred,” or, more succinctly, “*the probability of $a$ given $b$.*”

Mathematically, to compute the *conditional* *probability of $a$ given $b$*, we use the following formula:

$$
P(a \mid b) = \frac{P(a \land b)}{P(b)}
$$

> To put it in words, the probability that $*a*$ given $*b*$ is true is equal to the *probability of $a$ and $b$ being true*, divided by *the probability of $b$*. An intuitive way of reasoning about this is the thought “we are interested in the events where both $*a*$ and $*b*$ are true (the numerator), but only from the worlds where we know $*b*$ to be true (the denominator).” ***Dividing by $b$ restricts the possible worlds to the ones where $b$ is true.***
> 

## **Joint Probability**

Joint probability is the likelihood of multiple events all occurring.

### **1. For Independent Events**

When events $a$ and $b$ are independent, meaning that the occurrence of one event does not impact the other, probability of $*a*$ and $*b$* is equal to **the probability of $*a*$ times the probability of $b*b$$P(a \land b) = P(a)\cdot P(b)$*

### **2. For Dependent Events**

Events are often dependent on each other, meaning that one event's occurrence influences the likelihood of the other.

$$
P(a \land b) = P(b)P(a \mid b) \\
Or \\
P(a \land b) = P(a)P(b \mid a)
$$

The [above formula](Lecture%202%20Uncertainty%202f7abebeda9f800b9fedf4bca411c9ee.md) are algebraically equivalent forms to the [conditional probability formula](Lecture%202%20Uncertainty%202f7abebeda9f800b9fedf4bca411c9ee.md):

## **Bayes’ Rule**

Bayes’ rule is commonly used in probability theory to compute conditional probability. In words, Bayes’ rule says that the *probability of $b$ given $a$* is equal to the *probability of $a$ given $b$*, times the *probability of $b$*, divided by the *probability of $a$*.

$$
P(b \mid a) = \frac{P(b) P(a \mid b)}{P(a)}
$$

<aside>
❗

It can be derived from the [joint probability for dependent events formula](Lecture%202%20Uncertainty%202f7abebeda9f800b9fedf4bca411c9ee.md).

</aside>

Knowing $P\left(a \mid b\right)$, in addition to $P\left(a\right)$ and $P\left(b\right)$, allows us to calculate $P\left(b \mid a\right)$. This is helpful, because knowing the conditional probability of a visible effect given an unknown cause, $P(\text{visible effect} \mid \text{unknown cause})$, allows us to calculate the probability of the unknown cause given the visible effect, $P\left(\text{unknown cause} \mid \text{visible effect}\right)$.

## **Joint Probability Distribution**

### **Joint distribution for independent variables**

$$
\mathbb P(X = x \text{ and } Y = y) = \mathbb P(X = x) \cdot \mathbb P(Y = y)
$$

### **Joint distribution for conditionally dependent variables**

$$
\mathbb{P}_{X,Y}(x, y) = \mathbb{P}(Y = y \mid X = x) \cdot \mathbb{P}(X = x) = \mathbb{P}(X = x \mid Y = y) \cdot \mathbb{P}(Y = y)
$$

## **Probability Rules**

- **Negation**: $P(\neg a) = 1 - P(a)$. This stems from the fact that the sum of the probabilities of all the possible worlds is 1, and the complementary literals $*a*$ and $*¬a*$ include all the possible worlds.
- **Inclusion-Exclusion**: $P(a ∨ b) = P(a) + P(b) - P(a ∧ b)$. This can interpreted in the following way: the worlds in which $*a*$ or $*b*$ are true are equal to all the worlds where $*a*$ is true, plus the worlds where $*b*$ is true. However, in this case, some worlds are counted twice (the worlds where both $*a*$ and $*b*$ are true)). To get rid of this overlap, we subtract once the worlds where both $*a*$ and $*b*$ are true (since they were counted twice).
- **Marginalization**: $P(a) = P(a, b) + P(a, \neg b)$. The idea here is that $*b*$ and $*\neg b*$ are disjoint probabilities. That is, the probability of $*b*$ and $*\neg b*$ occurring at the same time is $0$. We also know $*b*$ and $*\neg b*$ sum up to $1$. Thus, when $*a*$ happens, $*b*$ can either happen or not. When we take the probability of both $*a*$ and $*b*$ happening in addition to the probability of $*a*$ and $*\neg b*$, we end up with simply the probability of $*a*$.
- **Conditioning**: $P(a) = P(a \mid b)P(b) + P(a \mid \neg b)P(\neg b)$. This is a similar idea to marginalization. The probability of event $*a*$ occurring is equal to the probability of $*a*$ given $*b*$ times the probability of $*b*$, plus the probability of *a* given $*\neg b*$ time the probability of $*\neg b*$.

## **Bayesian Networks**

A Bayesian network is a data structure that represents the dependencies among random variables. Bayesian networks have the following properties:

- They are directed acyclic graph (**DAG**).
- Each node on the graph represent a random variable.
- An arrow from $X$ to $Y$ represents that $X$ is a parent of $Y$. That is, the probability distribution of $Y$ depends on the value of $X$.
- Each node $X$ has probability distribution $P(X \mid Parents(X))$.

Bayesian networks are ideal for taking an event that occurred and predicting the likelihood that any one of several possible known causes was the contributing factor.

Factorization definition:

For the following, let $*G = (V,E)*$ be a directed acyclic graph (DAG) and let $*X = (X_v),v ∈ V*$be a set of random variables indexed by $*V*$.

$*X*$ is a Bayesian network with respect to $*G*$ if its joint probability mass function (with respect to a product measure) can be written as a product of the individual probability mass functions, conditional on their parent variables.

$$
P(X) = \prod_{v \in V} P\left(X_v \mid X_{pa(v)}\right)
$$

## **Inference**

At the last lecture, we looked at inference through entailment. This means that we could definitively conclude new information based on the information that we already had. We can also infer new information based on probabilities. While this does not allow us to know new information for certain, it allows us to figure out the ***probability distributions for some values***. Inference has multiple properties.

- Query **$X$**: the variable for which we want to compute the probability distribution.
- Evidence variables **$E$**: one or more variables that have been observed for event **$e$**. For example, we might have observed that there is light rain, and this observation helps us compute the probability that the train is delayed.
- Hidden variables **$Y$**: variables that aren’t the query and also haven’t been observed. For example, standing at the train station, we can observe whether there is rain, but we can’t know if there is maintenance on the track further down the road. Thus, Maintenance would be a hidden variable in this situation.
- The goal: calculate **$P(X \mid e)$**. For example, compute the probability distribution of the Train variable (the query) based on the evidence **$e$** that we know there is light rain.

### **Inference by Enumeration**

[courses.cs.washington.edu](https://courses.cs.washington.edu/courses/cse573/24au/slides/cse573au24-BNInference.pdf)

BN Inference

Inference by enumeration is a process of finding the probability distribution of variable $X$ given observed evidence $e$ and some hidden variables $Y$.

$$
P(X \mid e)=\alpha P(X, e)=\alpha \sum_{y}{P(X, e, Y)}
$$

In this equation, $X$ stand for the query variable, $e$ for the observed evidence, $y$ for all the values of the hidden variables, and $\alpha$ normalizes the result such that we end up with probabilities that add up to $1$.

<aside>
👉

Entries $P(X,e,Y)$ from the joint distribution can be obtained from a BN by [multiplying the corresponding conditional probabilities](Lecture%202%20Uncertainty%202f7abebeda9f800b9fedf4bca411c9ee.md).

</aside>

To explain the equation in words, it is saying that the probability distribution of $X$ given $e$ is equal to a normalized probability distribution of $X$ and $e$. To get to this distribution, we sum the normalized probability of $X$, $e$, and $y$, where $y$ takes each time a different value of the hidden variables $Y$.

<aside>
❗

However, this way of computing probability is inefficient, especially when there are many variables in the model.

</aside>

## **Sampling in Bayesian Networks**

Sampling is a technique for **approximate inference** in probabilistic models like Bayesian networks.

<aside>
👉

Sampling trades off **exact precision** for **computational scalability**, making it feasible to perform inference in complex real-world models.

</aside>

**Core Idea**:

Generate a large number of **random samples** (or "scenarios") from the joint probability distribution defined by the Bayesian network. The frequency of outcomes in these samples approximates their true probabilities.

**How It Works**:

1. **Order Matters**: Variables are sampled in **topological order** (parents before children).
2. **Root Nodes (Independent)**: Sampled directly from their **prior probability distribution** $P(X)$.
3. **Non-Root Nodes (Conditionally Dependent)**: Sampled from their **conditional probability distribution** $P(X \mid \text{Parents}(X))$, using the **already-sampled values** of their parent nodes.

**Using Samples for Inference**:

- To estimate $P(X)$: Count how often the query variable takes a certain value across all samples, then divide by the total number of samples.
- To estimate **conditional probability** $P(X \mid E)$: Use **rejection sampling** — discard all samples that do not match the observed evidence, then compute the distribution over the remaining samples.

## **Likelihood Weighting**

Likelihood weighting is an **approximate inference** technique for Bayesian networks that improves upon the inefficiency of **rejection sampling**. Rejection sampling wastes computation by discarding any sample that doesn't match the observed evidence. Likelihood weighting solves this by **forcing every sample to be consistent with the evidence** and then **weighting the sample** by the probability that the evidence would have occurred in that specific scenario.

<aside>
👉

Likelihood weighting ensures that **no computational effort is wasted** on samples that contradict the evidence, making it a much more efficient method for performing inference when evidence is present.

</aside>

### How it Works

The algorithm generates samples while traversing the network in **topological order** (from parents to children):

1. **Initialize** a `weight` variable to `1`.
2. For each variable in the network:
    - **If the variable is part of the observed evidence**, its value is **not sampled**. Instead, it is **fixed to its observed value**.
        - The algorithm then calculates the probability of observing this fixed value **given the values already assigned to its parent nodes**.
        - This probability is **multiplied into the sample's** `weight`.
    - **If the variable is not evidence**, it is **sampled normally** from its conditional probability distribution based on its (already sampled or fixed) parents.
3. The final result is a **weighted sample**.

### Final Estimation

To estimate a probability distribution (e.g., for a query variable), the algorithm **sums the weights** of all samples where the query variable has a specific value, rather than simply counting them. These weighted totals are then normalized to produce the final probability distribution.

## **Markov Models**

### **The Markov Assumption**

The Markov assumption is an assumption that the current state depends on only a finite fixed number of previous states.

### **Markov Chain**

A Markov chain is a sequence of random variables where the distribution of each variable follows the Markov assumption. That is, each event in the chain occurs based on the probability of the event before it.

$$
P(q_i \mid q_1 \cdots q_{i−1}) = P(q_i \mid q_{i−1})
$$

To start constructing a Markov chain, we need a **transition model** that will specify the the probability distributions of the next event based on the possible values of the current event.

### **Hidden Markov Models**

A hidden Markov model(HMM) is a type of a Markov model for a system with hidden states that generate some observed event. This means that sometimes, the AI has some measurement of the world but no access to the precise state of the world. In these cases, the state of the world is called the **hidden state** and whatever data the AI has access to are the **observations**.

**A first-order hidden Markov model instantiates two simplifying assumptions:**

1. As with a first-order Markov chain, the probability of a particular state depends only on the previous state:
    
    $$
    \text{Markov Assumption: } P(q_i
    \mid q_1 \cdots q_{i−1}) = P(q_i
    \mid q_{i−1})
    $$
    
2. The probability of an output observation $o_i$ depends only on the state that produced the observation $q_i$ and not on any other states or any other observations:
    
    $$
    \text{Output Independence: } P(o_i
    \mid q_1 \cdots q_i
    , \cdots , q_T ,o_1 , \cdots ,o_i
    , \cdots ,o_T ) = P(o_i
    \mid q_i)
    $$
    

**An HMM is specified by the following components:**

| $Q=q_1q_2 \cdots q_N$ | a set of $N$ states. |
| --- | --- |
| $A = a_{11} \cdots a_{ij} \cdots a_{NN}$ | a transition probability matrix $A$, each $a_{ij}$ representing the probability of moving from state $i$ to state $j$, s.t. $\sum_{j=1}^N a_{ij}=1 \space \forall i$. |
| $B=b_i(o_t)$ | a sequence of **observation likelihoods**, also called **emission probabilities**, each expressing the probability of an observation $o_t$ being generated from a state $q_i$. |
| $π = π_1,π_2,\cdots,π_N$ | an **initial probability distribution** over states. $π_i$
is the probability that the Markov chain will start in state $i$. Some states $j$ may have $π_j = 0$, meaning that they cannot be initial states. Also, $\sum_{i=1}^{n}π_i=1$. |

**Hidden Markov models should be characterized by three fundamental problems:**

- Problem 1 (**Likelihood**): Given an HMM $λ = (A,B)$ and an observation sequence $O$, determine the likelihood $P(O \mid λ)$.
- Problem 2 (**Decoding**): Given an observation sequence $O$ and an HMM $λ =
(A,B)$, discover the best hidden state sequence $Q$.
- Problem 3 (**Learning**): Given an observation sequence $O$ and the set of states in the HMM, learn the HMM parameters $A$ and $B$.

#### Extension Reading

[Hidden Markov Models](https://web.stanford.edu/~jurafsky/slp3/A.pdf)