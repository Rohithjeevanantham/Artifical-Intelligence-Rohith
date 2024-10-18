import heapq

def branch_and_bound_with_heuristic(start, neighbors, costs, goal, heuristic):
    # Priority queue to store paths with their estimated total cost (cost so far + heuristic)
    pq = [(0 + heuristic[start], 0, start, [start])]  # (estimated total cost, actual cost, node, path)
    best_cost = {start: 0}  # Best cost for each node to prune suboptimal branches
    
    while pq:
        # Get the node with the lowest estimated cost (cost so far + heuristic)
        est_total_cost, current_cost, current_node, path = heapq.heappop(pq)
        
        print(f"Exploring node: {current_node} with current cost: {current_cost}, path: {path}")
        
        # If we've reached the goal, return the path and cost
        if current_node == goal:
            print(f"Goal reached with path: {path} and total cost: {current_cost}")
            return path, current_cost
        
        # Explore each neighbor of the current node
        for neighbor in neighbors.get(current_node, []):
            actual_cost = current_cost + costs.get((current_node, neighbor), float('inf'))
            
            # Calculate total estimated cost using heuristic (cost so far + estimated cost to goal)
            estimated_total_cost = actual_cost + heuristic[neighbor]
            
            # If we find a cheaper path to the neighbor, update best cost and push to the priority queue
            if neighbor not in best_cost or actual_cost < best_cost[neighbor]:
                best_cost[neighbor] = actual_cost
                heapq.heappush(pq, (estimated_total_cost, actual_cost, neighbor, path + [neighbor]))
                print(f"Branching to {neighbor} with new path: {path + [neighbor]} and total cost: {actual_cost}")
    
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

    # Heuristic values (estimated cost from node to the goal)
    heuristic = {
        1: 5,  # Estimated cost from node 1 to goal 6
        2: 4,
        3: 3,
        4: 2,
        5: 1,
        6: 0  # Goal node has a heuristic of 0
    }

    # Start at node 1, goal is node 6
    path, total_cost = branch_and_bound_with_heuristic(1, neighbors, costs, 6, heuristic)
    print(f"Best path: {path} with total cost: {total_cost}")
