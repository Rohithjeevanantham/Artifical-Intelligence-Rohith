import heapq

def beam_search(graph, start, goal, beam_width=2):
    frontier = [(0, start)]
    while frontier:
        level = []

        for _ in range(min(beam_width, len(frontier))):
            cost, node = heapq.heappop(frontier)
            print(f"Visiting: {node}")

            if node == goal:
                print("Goal found!")
                return True

            for neighbor, step_cost in graph[node]:
                heapq.heappush(level, (cost + step_cost, neighbor))

        frontier = level

    print("Goal not found.")
    return False

# Example Usage
graph = {
    'A': [('B', 1), ('C', 2)],
    'B': [('D', 2), ('E', 3)],
    'C': [('F', 4)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}
beam_search(graph, 'A', 'F', beam_width=2)