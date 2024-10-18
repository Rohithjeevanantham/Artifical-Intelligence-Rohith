def minimax(depth, nodeIndex, isMaximizingPlayer, values):

    # Base case: if maximum depth is reached, return the node value
    if depth == 3:
        return values[nodeIndex]

    if isMaximizingPlayer:
        best = float('-inf')  # Initialize to negative infinity

        # Explore both children nodes
        for i in range(2):
            val = minimax(depth + 1, nodeIndex * 2 + i, False, values)
            best = max(best, val)  # Maximize the score
        return best

    else:
        best = float('inf')  # Initialize to positive infinity

        # Explore both children nodes
        for i in range(2):
            val = minimax(depth + 1, nodeIndex * 2 + i, True, values)
            best = min(best, val)  # Minimize the score
        return best


if __name__ == "__main__":

    # Sample leaf node values
    values = [1, 4, 7, 2, 3, 0, 6, 5]

    # Start the Minimax algorithm with the root node
    optimalValue = minimax(0, 0, True, values)

    print(f"Optimal value using Minimax: {optimalValue}")
