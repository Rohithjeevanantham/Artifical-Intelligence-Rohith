import heapq

def a_star(start, neighbors, costs, goal, heuristic):
    # Priority queue for open nodes to explore: (f(n), g(n), current_node, path)
    pq = [(heuristic[start], 0, start, [start])]  # (f(n), g(n), node, path)
    visited = set()  # Set to store visited nodes
    best_cost = {start: 0}  # Best g(n) cost to reach each node
    
    while pq:
        # Pop the node with the lowest f(n) = g(n) + h(n)
        f, g, current_node, path = heapq.heappop(pq)

        # If the goal is reached, return the path and the cost
        if current_node == goal:
            print(f"Goal reached with path: {path} and cost: {g}")
            return path, g
        
        # If the current node is visited, skip
        if current_node in visited:
            continue
        
        # Mark the current node as visited
        visited.add(current_node)
        
        # Explore neighbors
        for neighbor in neighbors.get(current_node, []):
            new_g = g + costs.get((current_node, neighbor), float('inf'))  # g(n) = cost to reach neighbor
            
            # If this path to neighbor is better than any previous one, explore it
            if neighbor not in best_cost or new_g < best_cost[neighbor]:
                best_cost[neighbor] = new_g
                f = new_g + heuristic[neighbor]  # f(n) = g(n) + h(n)
                heapq.heappush(pq, (f, new_g, neighbor, path + [neighbor]))
                print(f"Exploring {neighbor}, f(n): {f}, g(n): {new_g}, path: {path + [neighbor]}")
    
    print("Goal not reachable.")
    return None, float('inf')

# Example usage
if __name__ == "__main__":
    # Graph's neighbors (adjacency list)
    neighbors = {
        1: [2, 3],
        2: [4, 5],
        3: [5],
        4: [6],
        5: [6],
        6: []
    }

    # Cost of moving between nodes (weighted graph)
    costs = {
        (1, 2): 1, (1, 3): 4,
        (2, 4): 2, (2, 5): 5,
        (3, 5): 1,
        (4, 6): 3,
        (5, 6): 2
    }

    # Heuristic values (estimated cost from node to goal)
    heuristic = {
        1: 5,  # Estimated cost from node 1 to goal 6
        2: 4,
        3: 3,
        4: 2,
        5: 1,
        6: 0  # Goal node has heuristic of 0
    }

    # Start at node 1, goal is node 6
    path, total_cost = a_star(1, neighbors, costs, 6, heuristic)
    print(f"Best path: {path} with total cost: {total_cost}")
