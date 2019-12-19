""" SudokuValidator class definition and static validate_line() function.

SudokuValidator class stores information about invalid cols/rows/squares.

    Invalid rows/cols/square info is stored as a hash where:
        key = invalid row/col/square number
        value = digits contained in invalid row/col/square

    Column and row numbers start at 0.

    Square numbering reads left to right.
    e.g.
        4x4 - Square Numbering
                    0|1
                    2|3 

        9x9 - Square Numbering
                    0|1|2
                    3|4|5
                    6|7|8

    Invalid squares are stored as a 2D array
    e.g.
        0: [[1, 3, 4], [3, 7, 2], [1, 9, 8]]

        represents the invalid square:

            1 3 4
            3 7 2
            1 9 8

        in the top left square of the grid.
"""
import json
import math
import random


def validate_line(line: list) -> bool:
    """Returns True if line is a valid Sudoku row/col"""
    for i in range(1, len(line) + 1):
        if i not in line:
            return False
    return True


class SudokuValidator:
    """A Sudoku grid validator which stores row/col/square validity"""

    def __init__(self, sudoku_grid) -> None:
        self.sudoku_grid = sudoku_grid
        self.grid_dim = len(self.sudoku_grid)
        self.invalid_rows = {}
        self.invalid_cols = {}
        self.invalid_squares = {}
        self.valid_board = self.validate_grid()

    def __str__(self):
        data = {}
        data["valid"] = self.valid_board
        data["dimension"] = self.grid_dim
        if not self.valid_board:
            if self.invalid_rows:
                data["invalid rows"] = self.invalid_rows
            if self.invalid_cols:
                data["invalid columns"] = self.invalid_cols
            if self.invalid_squares:
                data["invalid squares"] = self.invalid_squares
        return "SudokuValidator : " + json.dumps(data)

    def validate_rows(self) -> bool:
        """Checks for and stores invalid rows
        
        :return: True if all rows are valid
        :rtype: bool
        """
        valid = True
        for index, row in enumerate(self.sudoku_grid):
            if not validate_line(row):
                self.invalid_rows[index] = row
                valid = False
        return valid

    def validate_cols(self) -> bool:
        """Checks for and stores invalid columns

        :return: True if all columns are valid
        :rtype: bool
        """
        valid = True
        transpose = [list(i) for i in zip(*self.sudoku_grid)]

        for index, col in enumerate(transpose):
            if not validate_line(col):
                self.invalid_cols[index] = col
                valid = False
        return valid

    def validate_squares(self) -> bool:
        """Checks for and stores invalid squares
        
        :return: True if all squares are valid
        :rtype: bool
        """
        valid = True
        square_dim = int(math.sqrt(self.grid_dim))

        for y_idx in range(0, self.grid_dim, square_dim):
            for x_idx in range(0, self.grid_dim, square_dim):
                square = []
                for row in range(y_idx, square_dim + y_idx):
                    square.append(self.sudoku_grid[row][x_idx : square_dim + x_idx])
                flat_square = [x for y in square for x in y]
                square_num = x_idx // square_dim + y_idx
                if not validate_line(flat_square):
                    self.invalid_squares[square_num] = square
                    valid = False
        return valid

    def validate_grid(self) -> bool:
        """Validates Sudoku solution grid

        :return: True if input grid is valid solution
        :rtype: bool
        """
        rows_valid = self.validate_rows()
        cols_valid = self.validate_cols()
        squares_valid = self.validate_squares()

        return rows_valid and cols_valid and squares_valid

    def print_info(self):
        """Pretty print info about grid including invalid rows/cols/squares"""
        div_len = 45
        
        print(div_len * "=")
        for row in self.sudoku_grid:
            print("  " + " ".join(map(str, row)))
        print(div_len * "-")

        if self.valid_board:
            print("VALID SUDOKU GRID")
        else:
            print("INVALID SUDOKU GRID")
            if self.invalid_rows:
                print("Invalid rows:")
                for key, val in self.invalid_rows.items():
                    print(f"\t{key}: {val}")
            if self.invalid_cols:
                print("Invalid cols:")
                for key, val in self.invalid_cols.items():
                    print(f"\t{key}: {val}")
            if self.invalid_squares:
                print("Invalid squares:")
                for key, val in self.invalid_squares.items():
                    print(f"\t{key}: {val}")
        print(div_len * "=")


def gen_random_matrix(dim):
    """Generate a random 2D matrix
    
    All rows will be valid Sudoku rows, but chances are most columns/squares will not
    :param dim: dimensions of matrix
    :type dim: int
    :return: random 2D matrix
    :rtype: list of lists
    """
    matrix = [[x for x in range(1, dim)] for y in range(dim)]
    for row in matrix:
        random.shuffle(row)
    return matrix


if __name__ == "__main__":

    GRIDS = [
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

    # 16x16 grids
    BIG_GRIDS = [
        gen_random_matrix(16),
        gen_random_matrix(16),
    ]

    print("Basic Validation:")
    for grid in GRIDS + BIG_GRIDS:
        print(SudokuValidator(grid).valid_board)

    print("\nPrint info demo:")
    for grid in GRIDS + BIG_GRIDS:
        print("Grid info:")
        SudokuValidator(grid).print_info()

    print("\nto_string demo:")
    for grid in GRIDS: # ignore the big ones, we get the point
        print(SudokuValidator(grid))
        print("\n")
