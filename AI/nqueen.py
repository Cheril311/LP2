import random
import numpy as np

def random_state(n):
    """
    Returns a random initial state with n queens on an n x n board.
    """
    return [random.randint(0, n-1) for _ in range(n)]

def attacks(state):
    """
    Returns the number of queen attacks in the given state.
    """
    n = len(state)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if state[i] == state[j] or abs(i-j) == abs(state[i]-state[j]):
                count += 1
    return count

def hill_climbing(n):
    """
    Solves the n-queens problem using hill climbing approach.
    """
    current = random_state(n)
    while True:
        neighbors = []
        for col in range(n):
            for row in range(n):
                if current[col] != row:
                    neighbor = list(current)
                    neighbor[col] = row
                    neighbors.append(neighbor)
        if not neighbors:
            break
        neighbor = min(neighbors, key=attacks)
        if attacks(neighbor) >= attacks(current):
            break
        current = neighbor
    return current

# example usage:
sol = hill_climbing(4)

board = np.zeros((4,4))
for i in range(len(sol)):
    board[sol[i]][i]=1
print(board)
