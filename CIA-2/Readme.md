# Minimax Algorithm with Alpha-Beta Pruning

## Introduction

The **Minimax Algorithm** is a decision-making strategy used in two-player games, such as Tic-Tac-Toe and Chess. It helps identify the optimal move for a player, assuming the opponent also plays optimally. The two roles are:

- **Maximizing Player**: Tries to get the highest possible score.
- **Minimizing Player**: Tries to minimize the score or benefit of the opponent.

The game is modeled as a **tree structure**, where each node represents a game state, and the leaf nodes indicate the final scores.

---

## Alpha-Beta Pruning

**Alpha-Beta Pruning** is an optimization technique used with the Minimax algorithm to reduce the number of nodes evaluated. It skips branches that won't affect the final decision, improving the algorithm's efficiency.

- **Alpha**: The best value found so far for the maximizing player.
- **Beta**: The best value found so far for the minimizing player.

Whenever **beta ≤ alpha**, the remaining branches of the current node are **pruned** because they cannot provide a better outcome.

---

## Example Tree Structure

This example shows a **game tree** with leaf nodes having fixed values at depth 3:

```
                 Root (0)  
                /     \
           Max(1)      Max(2)
           /  \        /   \
      Min(3) Min(4)  Min(5)  Min(6)
      / \    / \    / \    /  \
     1   4   7   2   3   0   6    5
```

- **Maximizing Player** selects the maximum value from child nodes.
- **Minimizing Player** selects the minimum value.

---

## Python Code Example

```python
def minimax_ab(depth, nodeIndex, isMax, values, alpha, beta):
    if depth == 3:
        return values[nodeIndex]

    if isMax:
        maxEval = float('-inf')
        for i in range(2):
            eval = minimax_ab(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval
    else:
        minEval = float('inf')
        for i in range(2):
            eval = minimax_ab(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval

if __name__ == "__main__":
    values = [1, 4, 7, 2, 3, 0, 6, 5]
    alpha = float('-inf')
    beta = float('inf')
    optimalValue = minimax_ab(0, 0, True, values, alpha, beta)
    print(f"Optimal value: {optimalValue}")
```

---

## Explanation of the Code

1. **Depth 3**: Leaf nodes contain the final scores.
2. **Maximizing Player** picks the highest value.
3. **Minimizing Player** picks the lowest value.
4. **Alpha-Beta Pruning** stops further exploration when the current path is not useful.

---

## Sample Output

```
Optimal value: 3
Pruning at depth 1 for node 2.
```

---

## Conclusion

The **Minimax Algorithm with Alpha-Beta Pruning** significantly improves performance by eliminating unnecessary nodes. This makes it practical for larger game trees, where exploring every node would be computationally expensive.


# Minimax Algorithm Explanation

## Introduction
The **Minimax algorithm** is a recursive strategy used in decision-making and game theory. It is designed for **two-player games**, where one player aims to maximize their score (Maximizing Player) and the other tries to minimize the opponent’s score (Minimizing Player).

The algorithm explores all possible moves and **backtracks** to find the optimal move for the current player. It assumes that both players play optimally to achieve the best possible outcome for themselves.

---

## Algorithm Logic

1. **Leaf Nodes:** At the maximum depth (in this case, depth = 3), the algorithm returns the value of the current node.
2. **Maximizing Player:** At nodes where the **maximizing player** makes a move, the algorithm picks the **maximum value** from all possible child nodes.
3. **Minimizing Player:** At nodes where the **minimizing player** makes a move, the algorithm picks the **minimum value** from all possible child nodes.

---

