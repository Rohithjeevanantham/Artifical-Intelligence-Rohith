# Minimax function with Alpha-Beta Pruning
def minimax_ab(depth, nodeIndex, isMaximizingPlayer, values, alpha, beta):
    """
    Parameters:
    - depth: Current depth in the tree (how far we are from the root).
    - nodeIndex: Index of the current node in the 'values' list.
    - isMaximizingPlayer: Boolean to check if it's maximizing player's turn.
    - values: List of terminal nodes (leaf values) in the game tree.
    - alpha: The best value that the maximizing player can guarantee so far.
    - beta: The best value that the minimizing player can guarantee so far.
    """

    # Base case: If we've reached the maximum depth, return the leaf node value.
    if depth == 3:
        return values[nodeIndex]

    # If it's the Maximizing Player's turn
    if isMaximizingPlayer:
        maxEval = float('-inf')  # Initialize maxEval to negative infinity.

        # Explore both child nodes (since it's a binary tree, there are 2 children per node).
        for i in range(2):  
            # Recursive call for the child node.
            eval = minimax_ab(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)

            # Update the maximum evaluation for this level.
            maxEval = max(maxEval, eval)

            # Update the alpha value.
            alpha = max(alpha, eval)

            # Pruning: If beta <= alpha, stop further exploration.
            if beta <= alpha:
                print(f"Pruning at depth {depth} for node {nodeIndex}.")
                break  # Skip remaining branches as they won't be useful.

        return maxEval  # Return the best evaluation found for the maximizing player.

    # If it's the Minimizing Player's turn
    else:
        minEval = float('inf')  # Initialize minEval to positive infinity.

        # Explore both child nodes.
        for i in range(2):
            # Recursive call for the child node.
            eval = minimax_ab(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)

            # Update the minimum evaluation for this level.
            minEval = min(minEval, eval)

            # Update the beta value.
            beta = min(beta, eval)

            # Pruning: If beta <= alpha, stop further exploration.
            if beta <= alpha:
                print(f"Pruning at depth {depth} for node {nodeIndex}.")
                break  # Skip remaining branches.

        return minEval  # Return the best evaluation found for the minimizing player.

# Driver code to run the Minimax Algorithm
if __name__ == "__main__":
    # Example game tree with leaf node values.
    values = [1, 4, 7, 2, 3, 0, 6, 5]  # This represents terminal node values.

    # Initialize alpha and beta to their extreme values.
    alpha = float('-inf')  # Start with the worst possible score for the maximizer.
    beta = float('inf')    # Start with the worst possible score for the minimizer.

    # Call the minimax function for the root of the tree (depth=0, nodeIndex=0).
    optimalValue = minimax_ab(0, 0, True, values, alpha, beta)

    # Print the result: The optimal value obtained by playing optimally.
    print(f"Optimal value using Alpha-Beta Pruning: {optimalValue}")
