import heapq

def branch_and_bound_greedy_heuristic(start, neighbors, costs, goal, heuristic):
    # Priority queue to store paths with their estimated total cost (cost + heuristic)
    pq = [(0 + heuristic[start], 0, start, [start])]  # (estimated total cost, actual cost, node, path)
    # Best cost for each node to prune suboptimal branches
    best_cost = {start: 0}
    
    while pq:
        # Pop the node with the lowest estimated total cost
        est_total_cost, current_cost, current_node, path = heapq.heappop(pq)
        
        print(f"Exploring node: {current_node} with current cost: {current_cost}, path: {path}")
        
        # Early exit if the goal is reached
        if current_node == goal:
            print(f"Goal reached with path: {path} and cost: {current_cost}")
            return path, current_cost
        
        # Explore neighbors
        for neighbor in neighbors.get(current_node, []):
            actual_cost = current_cost + costs.get((current_node, neighbor), float('inf'))
            
            # Use the heuristic to estimate the total cost from neighbor to goal
            estimated_total_cost = actual_cost + heuristic[neighbor]
            
            # Check if this path to the neighbor is better than any previously found
            if neighbor not in best_cost or actual_cost < best_cost[neighbor]:
                best_cost[neighbor] = actual_cost
                heapq.heappush(pq, (estimated_total_cost, actual_cost, neighbor, path + [neighbor]))
                print(f"Branching to {neighbor} with cost: {actual_cost}, heuristic: {heuristic[neighbor]}, total estimated cost: {estimated_total_cost}, new path: {path + [neighbor]}")
    
    print("Goal not reachable.")
    return None, float('inf')

# Example usage
if __name__ == "__main__":
    # Neighbors representing the graph
    neighbors = {
        1: [2, 3],
        2: [4, 5],
        3: [5],
        4: [6],
        5: [6],
        6: []
    }

    # Define costs between nodes (weighted graph)
    costs = {
        (1, 2): 1, (1, 3): 4,
        (2, 4): 2, (2, 5): 5,
        (3, 5): 1,
        (4, 6): 3,
        (5, 6): 2
    }

    # Define heuristic (estimated cost from each node to the goal)
    heuristic = {
        1: 5,  # Estimated cost from node 1 to goal 6
        2: 4,
        3: 3,
        4: 2,
        5: 1,
        6: 0  # Heuristic for the goal is 0
    }

    # Start at node 1, goal is to reach node 6
    path, total_cost = branch_and_bound_greedy_heuristic(1, neighbors, costs, 6, heuristic)
    print(f"Best path: {path} with total cost: {total_cost}")
