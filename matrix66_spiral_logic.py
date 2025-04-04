import pandas as pd
from typing import List, Tuple
import tools
import matplotlib.pyplot as plt

# Cél: spirál mentén 2 → 3 → 1 → 2 → 3… sorrendet követve töltsük ki a mátrixot úgy,
# hogy minden sorban és oszlopban a számok (1,2,3) maximum egyszer szerepelhetnek,
# ahol ez nem teljesíthető, oda 0 kerüljön.

# Spiral path generator
def generate_edge_spiral_path(n: int) -> List[Tuple[int, int]]:
    path = []
    top, bottom, left, right = 0, n - 1, 0, n - 1
    while top <= bottom and left <= right:
        for j in range(left, right + 1):
            path.append((top, j))
        top += 1
        for i in range(top, bottom + 1):
            path.append((i, right))
        right -= 1
        if top <= bottom:
            for j in range(right, left - 1, -1):
                path.append((bottom, j))
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                path.append((i, left))
            left += 1
    return path

# Ellenőrzés: szerepel-e már a szám a sorban/oszlopban
def is_valid(grid, row, col, num):
    return num not in grid[row] and all(grid[r][col] != num for r in range(len(grid)))

# Kitöltés spirál szerint, szabály betartásával
def fill_spiral_grid_with_rules(sequence, path, size=6):
    grid = [[0 for _ in range(size)] for _ in range(size)]
    seq_len = len(sequence)
    for i, (r, c) in enumerate(path):
        num = sequence[i % seq_len]
        if is_valid(grid, r, c, num):
            grid[r][c] = num
        else:
            num = 0
    return grid
# Generálás és megjelenítés
spiral_sequence = [2, 3, 1]
spiral_path = generate_edge_spiral_path(6)
spiral_grid_rule_based = fill_spiral_grid_with_rules(spiral_sequence, spiral_path)

# Eredmény megjelenítése
df_spiral_grid_rule_based = pd.DataFrame(spiral_grid_rule_based)
print("Spirál + szabályos mátrix (2-3-1-2-3, sor/oszloponként egyszer):")
print(df_spiral_grid_rule_based)

"""
def visualize_clean_grid(grid):
    size = len(grid)
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xticks([])
    ax.set_yticks([])

    # Négyzetrács kirajzolása
    for i in range(size + 1):
        ax.plot([0, size], [i, i], color='black', linewidth=1)
        ax.plot([i, i], [0, size], color='black', linewidth=1)

    # Számok beírása
    for i in range(size):
        for j in range(size):
            val = grid[i][j]
            if val != 0:
                ax.text(j + 0.5, size - i - 0.5, str(val),
                        ha='center', va='center', fontsize=16)

    ax.set_xlim(0, size)
    ax.set_ylim(0, size)
    ax.set_aspect('equal')
    plt.tight_layout()
    plt.show()
git 
# Megjelenítés tiszta négyzetrácsban
visualize_clean_grid(spiral_grid_rule_based)
"""

# Új: A spirálvonal precízen a négyzetrács szélén halad körbe, a bal felső sarokból indulva
# és minden cella szélét követve

def draw_precise_spiral_border(grid, path):
    size = len(grid)
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xticks([])
    ax.set_yticks([])

    # Alaprács
    for i in range(size + 1):
        ax.plot([0, size], [i, i], color='black', linewidth=1)
        ax.plot([i, i], [0, size], color='black', linewidth=1)

    # Számok beírása
    for i in range(size):
        for j in range(size):
            val = grid[i][j]
            if val != 0:
                ax.text(j + 0.5, size - i - 0.5, str(val),
                        ha='center', va='center', fontsize=16)

    # Vonalakat rajzolunk a spirál mentén a cellák éleihez igazítva
    for i in range(len(path) - 1):
        r0, c0 = path[i]
        r1, c1 = path[i + 1]

        # Cellák élszélei spirál mentén: a négyzetháló vonalaihoz illeszkednek
        if r1 == r0:
            if c1 > c0:  # jobbra
                x_start, y_start = c0, size - r0
                x_end, y_end = c1 - 1, size - r1 +1
                x_start, y_start = c0, size - r1
                x_end, y_end = c1 + 1, size - r1
            else:  # balra
                x_start, y_start = c0 - 1, size - r0
                x_end, y_end = c1 - 1, size - r1
        else:
            if r1 > r0:  # le
                x_start, y_start = c1, size - r0
                x_end, y_end = c0, size - r1
                x_start, y_start = c1 + 1, size - r0 + 2
                x_end, y_end = c1 + 1, size - r1 + 2
            else:  # fel
                x_start, y_start = c0, size - r0
                x_end, y_end = c1, size - r1
                x_start, y_start = c0, size - r0 
                x_end, y_end = c1, size - r1

        ax.plot([x_start, x_end], [y_start, y_end], color='red', linewidth=5)

    ax.set_xlim(0, size)
    ax.set_ylim(0, size)
    ax.set_aspect('equal')
    plt.tight_layout()
    plt.show()

# Megjelenítés: pontos spirálvonal a rács élein
draw_precise_spiral_border(spiral_grid_rule_based, spiral_path)

