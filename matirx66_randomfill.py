import random
import numpy as np

def generate_random_grid():
    n = 6
    grid = [[0 for _ in range(n)] for _ in range(n)]

    # Soronként helyezzük el a 3 számot (1, 2, 3)
    cols_used = {1: set(), 2: set(), 3: set()}
    for row in range(n):
        numbers = [1, 2, 3]
        random.shuffle(numbers)
        positions = random.sample(range(n), 3)
        for num, col in zip(numbers, positions):
            # Ha az adott szám már szerepel ebben az oszlopban, próbálj új pozíciót
            attempts = 0
            while col in cols_used[num] and attempts < 10:
                col = random.choice(range(n))
                attempts += 1
            grid[row][col] = num
            cols_used[num].add(col)

    return grid

random_grid = generate_random_grid()
for row in random_grid:
    print(row)
