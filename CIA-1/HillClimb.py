import random

def hill_climb(start, neighbors, goal):
    current = start
    while True:
        print(f"Current: {current}")

        if current == goal:
            print("Goal reached!")
            return True

        next_states = neighbors[current]
        if not next_states:
            print("Stuck at local optimum.")
            return False

        next_state = random.choice(next_states)
        if next_state > current:
            current = next_state
        else:
            print("No better neighbors found.")
            return False

# New example usage
if __name__ == "__main__":
    neighbors = {
        1: [3, 2],
        2: [4, 8],
        3: [5, 7],
        4: [6],
        5: [8],
        6: [],
        7: [8],
        8: []
    }
    hill_climb(1, neighbors, 8)
