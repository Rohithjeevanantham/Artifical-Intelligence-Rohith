def branch_and_bound_greedy(graph, start, goal):
    frontier = [(0, start)]
    best_cost = float('inf')

    while frontier:
        frontier.sort(key=lambda x: x[0])  # Sort by cost
        cost, node = frontier.pop(0)
        print(f"Visiting: {node}, Current Cost: {cost}")

        if node == goal:
            print(f"Goal reached with cost: {cost}")
            return cost

        for neighbor, step_cost in graph[node]:
            frontier.append((cost + step_cost, neighbor))

    return float('inf')
# Example Usage
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 4)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 2)],
    'F': []
}
# Example Usage
branch_and_bound_greedy(graph, 'A', 'F')