# Lecture 1: Knowledge Representation & Logic

Date: 2026年1月28日 → 2026年1月29日

# Lecture 1: Knowledge Representation & Logic

## 1. Introduction

- AI relies on **knowledge** and **reasoning** to make decisions.
- Knowledge-based agents use stored information to infer new conclusions.

## 2. Propositional Logic

- **Propositions**: Statements that are either true or false.
- **Symbols**: Represent propositions (P, Q, R).
- **Logical Connectives**:
    - Negation (¬)
    - Conjunction (∧)
    - Disjunction (∨)
    - Implication (→)
    - Biconditional (↔)
- **Truth Tables**: Show outcomes of logical operations.

## 3. Knowledge Representation

- **Models**: Assign truth values to propositions.
- **Knowledge Base (KB)**: Collection of known facts.
- **Entailment (⊨)**: If KB ⊨ α, then α must be true given KB.
- **Inference**: Deriving new facts from KB.

## 4. Algorithms for Reasoning

- **Model Checking**: Enumerate all possible models to test entailment.
- **Python Implementation**: Represent propositions and evaluate truth values programmatically.

## 5. Applications & Examples

- **Harry Potter Example**: Logical reasoning about whether it is raining.
- **Clue Game**: Deduction of murderer, weapon, and location.
- **Logic Puzzles & Mastermind**: Using propositional logic to solve structured problems.

## 6. Rules of Inference

- **Modus Ponens**: If P → Q and P, then Q.
- **Double Negation**: ¬(¬P) ≡ P.
- **De Morgan’s Laws**: ¬(P ∧ Q) ≡ (¬P ∨ ¬Q).
- **Distribution Laws**: Logical equivalences for simplification.
- **Resolution**: Combining clauses to infer new knowledge.

## 7. First-Order Logic (FOL)

- Extends propositional logic with **objects and relations**.
- **Quantifiers**:
    - Universal (∀): “For all…”
    - Existential (∃): “There exists…”
- Enables richer representation of knowledge.

## Key Takeaways

- Logic provides a **formal foundation** for AI reasoning.
- Propositional logic is powerful but limited; FOL expands expressiveness.
- Model checking and inference rules are essential for automated reasoning.