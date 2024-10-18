from collections import deque

def bfs(graph, start, goal):
    queue = deque([start])
    visited = set([start])

    while queue:
        node = queue.popleft()
        print(f"Visiting: {node}")

        if node == goal:
            print("Goal found!")
            return True

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

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
bfs(graph, 'A', 'F')
