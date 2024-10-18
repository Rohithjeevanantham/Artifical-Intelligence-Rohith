import random

def british_museum_search(solution_space, is_solution):
    attempts = 0
    while True:
        state = random.choice(solution_space)
        attempts += 1
        print(f"Attempt {attempts}: Trying state {state}")
        if is_solution(state):
            print(f"Solution found: {state} in {attempts} attempts!")
            return state
        
# Example Usage
solution_space = [1, 2, 3, 4, 5, 6, 42, 7, 8, 9]
is_solution = lambda x: x == 42  # The solution we're looking for is 42

british_museum_search(solution_space, is_solution)
