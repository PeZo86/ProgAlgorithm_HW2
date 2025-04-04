import random
import pandas as pd


# Újratervezett generáló algoritmus: biztosítja, hogy minden sorban és oszlopban 1, 2, 3 pontosan egyszer szerepeljen

def generate_strict_full_grid():
    size = 6
    numbers = [1, 2, 3]

    # Előre létrehozunk minden sort úgy, hogy mindegyikben 1,2,3 pontosan egyszer szerepel
    # Az oszlopokra is figyelünk
    grid = [[0 for _ in range(size)] for _ in range(size)]
    
    def is_valid_grid(grid):
        for i in range(size):
            col = [grid[r][i] for r in range(size)]
            for num in numbers:
                if col.count(num) > 1:
                    return False
        return True

    def backtrack(row):
        if row == size:
            return is_valid_grid(grid)

        positions = [0, 1, 2, 3, 4, 5]
        for pos_combo in random.sample(list(itertools.combinations(positions, 3)), k=20):
            values = numbers[:]
            random.shuffle(values)
            temp_row = [0] * size
            for col, val in zip(pos_combo, values):
                temp_row[col] = val
            grid[row] = temp_row
            if backtrack(row + 1):
                return True
            grid[row] = [0] * size
        return False

    import itertools
    backtrack(0)
    return grid


# Generate and display the valid grid
strict_valid_grid = generate_strict_full_grid()
df_strict_valid_grid = pd.DataFrame(strict_valid_grid)

print("Szabályos 6x6 mátrix, oszlop és sorban pontosan egyszer van az 1, 2, 3:")
print(df_strict_valid_grid)
