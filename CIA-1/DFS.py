def dfs(graph, start, goal, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(f"Visiting: {start}")

    if start == goal:
        print("Goal found!")
        return True

    for neighbor in graph[start]:
        if neighbor not in visited:
            if dfs(graph, neighbor, goal, visited):
                return True

    return False

# Example usage
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
dfs(graph, 'A', 'F')
