"""A quick and dirty Sudoku grid validator

Uses numpy for matrix operations:
 - extracting submatrices in validate_square()
 - transpose

 All functions return immediately upon detecting invalidity.

 Operates correctly on Sudoku grid dimensions that are perfect squares.
"""

import math
import numpy as np


def validate_line(line):
    for i in range(1, len(line) + 1):
        if i not in line:
            return False
    return True


def validate_lines(grid):
    for line in grid:
        if not validate_line(line):
            return False
    return True


def validate_square(grid):
    grid_dim = len(grid)
    square_dim = int(math.sqrt(grid_dim))

    for y_idx in range(0, grid_dim, square_dim):
        for x_idx in range(0, grid_dim, square_dim):
            square = grid[x_idx : (x_idx + square_dim), y_idx : (y_idx + square_dim)]
            flat_square = [x for y in square for x in y]
            if not validate_line(flat_square):
                return False
    return True


def validate_grid(grid):
    grid = np.array(grid)
    return (
        validate_lines(grid)
        and validate_lines(grid.transpose())
        and validate_square(grid)
    )


if __name__ == "__main__":
    GRIDS = [
        [
            [6, 2, 7, 11, 8, 13, 14, 9, 1, 5, 4, 12, 10, 3, 16, 15],
            [13, 9, 5, 10, 6, 14, 11, 1, 3, 4, 2, 7, 8, 15, 16, 12],
            [5, 10, 1, 8, 3, 11, 4, 9, 15, 14, 13, 2, 6, 16, 12, 7],
            [13, 14, 6, 12, 9, 16, 7, 4, 10, 5, 8, 3, 2, 1, 11, 15],
            [11, 9, 3, 6, 8, 16, 2, 15, 1, 13, 4, 7, 12, 14, 5, 10],
            [7, 1, 12, 5, 2, 13, 15, 6, 16, 14, 8, 4, 9, 3, 11, 10],
            [2, 6, 10, 13, 5, 16, 7, 9, 15, 4, 12, 11, 3, 14, 8, 1],
            [12, 3, 5, 4, 10, 8, 13, 9, 6, 2, 7, 14, 16, 11, 1, 15],
            [2, 15, 6, 5, 7, 8, 12, 13, 14, 16, 10, 1, 3, 9, 4, 11],
            [3, 4, 11, 2, 16, 10, 6, 12, 8, 15, 7, 5, 14, 13, 1, 9],
            [13, 6, 9, 15, 5, 10, 11, 8, 1, 14, 2, 16, 12, 4, 7, 3],
            [10, 2, 16, 3, 5, 12, 15, 11, 4, 1, 9, 7, 14, 13, 8, 6],
            [9, 10, 13, 4, 14, 3, 16, 6, 1, 7, 5, 12, 8, 11, 15, 2],
            [2, 13, 9, 12, 11, 14, 15, 1, 7, 6, 3, 10, 16, 5, 8, 4],
            [11, 5, 2, 9, 4, 16, 3, 6, 7, 15, 8, 14, 1, 13, 12, 10],
            [13, 16, 5, 6, 1, 11, 4, 3, 15, 12, 8, 7, 10, 14, 9, 2],
        ],
        [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 4],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9],
        ],
        [
            [1, 3, 4, 6, 7, 8, 9, 1, 2],
            [3, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [1, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9],
        ],
        [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9],
        ],
        [[4, 2, 1, 3], [1, 3, 4, 2], [3, 1, 2, 4], [2, 3, 1, 1]],
        [[4, 2, 1, 3], [1, 3, 4, 2], [3, 1, 2, 4], [2, 4, 3, 1]],
    ]

    for grid in GRIDS:
        print(f"Valid solution: {validate_grid(grid)}")
