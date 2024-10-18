import math

def branch_and_bound(graph, start, goal):
    frontier = [(0, start)]
    best_cost = math.inf

    while frontier:
        cost, node = frontier.pop(0)
        print(f"Visiting: {node}, Current Cost: {cost}")

        if node == goal:
            best_cost = min(best_cost, cost)
            print(f"Goal found with cost: {best_cost}")

        for neighbor, step_cost in graph[node]:
            total_cost = cost + step_cost
            if total_cost < best_cost:
                frontier.append((total_cost, neighbor))

    print(f"Best Cost to Goal: {best_cost}")
    return best_cost

# Example Usage
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 4)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 2)],
    'F': []
}
branch_and_bound(graph, 'A', 'F')