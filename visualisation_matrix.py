import numpy as np
import matplotlib.pyplot as plt
from sprial_grid_rule_based import matrix66_spiral_logic

# Frissített vizualizáció: csak a rács, bal felső sarokból induló számozással, koordináták nélkül
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

# Megjelenítés tiszta négyzetrácsban
visualize_clean_grid(spiral_grid_rule_based)
# Számok beírása a spirál mentén
# Megjelenítés tiszta négyzetrácsban
