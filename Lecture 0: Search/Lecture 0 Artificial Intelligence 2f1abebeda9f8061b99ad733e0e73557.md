# Lecture 0: Artificial Intelligence

Date: 2026年1月26日 → 2026年1月27日

# Lecture 0: Introduction to Artificial Intelligence

## 1. What is AI?

- AI simulates intelligent behavior in computers.
- Examples:
    - Face recognition in photos
    - Chess-playing programs beating world champions
    - Speech recognition (Siri, Alexa)

## 2. Core Topics in AI

- **Search**: Finding solutions (e.g., navigation apps, puzzles).
- **Knowledge**: Representing information and making inferences.
- **Uncertainty**: Handling probabilistic events.
- **Optimization**: Finding the best solution, not just any solution.
- **Learning**: Improving performance from data (e.g., spam detection).
- **Neural Networks**: Brain-inspired structures for tasks.
- **Language**: Processing human natural language.

## 3. Search Fundamentals

- **Agent**: Entity that perceives and acts in environment.
- **State**: Configuration of agent/environment.
- **Initial State**: Starting point.
- **Actions**: Possible moves from a state.
- **Transition Model**: Defines results of actions.
- **State Space**: All reachable states.
- **Goal Test**: Determines if a state is the goal.
- **Path Cost**: Numerical cost of a path.

## 4. Solving Search Problems

- **Solution**: Sequence of actions from initial to goal state.
- **Optimal Solution**: Lowest path cost among all solutions.
- **Nodes**: Data structures storing state, parent, action, path cost.
- **Frontier**: Mechanism managing nodes during search.
- **Explored Set**: Tracks visited states.

## 5. Search Algorithms

- **Depth-First Search (DFS)**
    - Frontier as stack (LIFO).
    - Pros: Can be fastest if lucky.
    - Cons: May not find optimal solution.
- **Breadth-First Search (BFS)**
    - Frontier as queue (FIFO).
    - Pros: Guaranteed optimal solution.
    - Cons: Slower, may take longer.
- **Greedy Best-First Search**
    - Uses heuristic h(n) estimating closeness to goal.
    - Example: Manhattan distance in mazes.
    - Pros: Faster with good heuristics.
    - Cons: Can mislead if heuristic is poor.
- *A* Search*
    - Combines g(n) (cost so far) + h(n) (estimated cost to goal).
    - Optimal if heuristic is admissible and consistent.

## 6. Adversarial Search (Games)

- **Minimax Algorithm**
    - Models two-player games (e.g., Tic-Tac-Toe).
    - Maximizer seeks highest utility, minimizer seeks lowest.
    - Recursive evaluation of all possible moves.
- **Alpha-Beta Pruning**
    - Optimizes Minimax by skipping irrelevant branches.
    - Reduces computation without affecting correctness.
- **Depth-Limited Minimax**
    - Stops after fixed depth (useful for complex games like Chess).
    - Relies on evaluation functions to estimate utility of states.

## Key Takeaways

- Search is fundamental to AI problem-solving.
- Different algorithms balance speed vs. optimality.
- Heuristics improve efficiency but must be carefully designed.
- Adversarial search enables AI to play competitive games.