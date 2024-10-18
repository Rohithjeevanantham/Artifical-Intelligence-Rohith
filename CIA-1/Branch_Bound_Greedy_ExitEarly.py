import heapq

def branch_and_bound(start, neighbors, costs, goal):
    # Priority queue to hold paths with their cost, the format will be (cost, node, path)
    pq = [(0, start, [start])]
    # To store the best cost for each node (for pruning)
    best_cost = {start: 0}
    
    while pq:
        # Pop the node with the lowest cost
        current_cost, current_node, path = heapq.heappop(pq)
        
        print(f"Exploring node: {current_node} with current cost: {current_cost}, path: {path}")
        
        # Early exit if the goal is reached
        if current_node == goal:
            print(f"Goal reached with path: {path} and cost: {current_cost}")
            return path, current_cost
        
        # Explore neighbors
        for neighbor in neighbors.get(current_node, []):
            cost = current_cost + costs.get((current_node, neighbor), float('inf'))
            
            # Check if this path to the neighbor is better than any previously found
            if neighbor not in best_cost or cost < best_cost[neighbor]:
                best_cost[neighbor] = cost
                heapq.heappush(pq, (cost, neighbor, path + [neighbor]))
                print(f"Branching to {neighbor} with cost: {cost}, new path: {path + [neighbor]}")
    
    print("Goal not reachable.")
    return None, float('inf')

# Example usage
if __name__ == "__main__":
    neighbors = {
        1: [2, 3],
        2: [4, 5],
        3: [5],
        4: [6],
        5: [6],
        6: []
    }

    # Define costs between nodes
    costs = {
        (1, 2): 1, (1, 3): 4,
        (2, 4): 2, (2, 5): 5,
        (3, 5): 1,
        (4, 6): 3,
        (5, 6): 2
    }

    # Start at node 1, goal is to reach node 6
    path, total_cost = branch_and_bound(1, neighbors, costs, 6)
    print(f"Best path: {path} with total cost: {total_cost}")
