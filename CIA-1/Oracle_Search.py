def oracle_search(solution_space, oracle):
    if not solution_space:
        print("Solution space is empty.")
        return None
    
    visited = set()

    for attempts, state in enumerate(solution_space, start=1):
        if state in visited:
            continue
        visited.add(state)
        
        print(f"Attempt {attempts}: Checking state {state}")
        
        if oracle(state):
            print(f"Oracle found the solution: {state} in {attempts} attempts!")
            return state

    print("No solution found after checking all states.")
    return None

# Example Usage
solution_space = [1, 2, 3, 42, 5]
oracle = lambda x: x == 42  # Oracle knows the answer is 42
oracle_search(solution_space, oracle)
