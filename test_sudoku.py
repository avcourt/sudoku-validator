import pytest
import sudoku
import numpy

def test_ordered_line_validator():
    assert sudoku.validate_line([1, 2, 3, 4, 5, 6, 7, 8, 9]) == True
    assert sudoku.validate_line([1, 2, 3, 4, 5, 6]) == True
    assert sudoku.validate_line([1, 2, 3]) == True


def test_unordered_line_validator():
    assert sudoku.validate_line([8, 7, 6, 4, 5, 2, 1, 3, 9]) == True
    assert sudoku.validate_line([6, 4, 5, 2, 1, 3]) == True
    assert sudoku.validate_line([2, 1, 3]) == True


def test_ordered_duplicate_line_validator():
    assert sudoku.validate_line([1, 2, 3, 3, 4, 5, 6, 7, 8]) == False
    assert sudoku.validate_line([1, 2, 3, 4, 5, 5, 6]) == False
    assert sudoku.validate_line([1, 2, 3, 4, 5, 5, 6, 6]) == False
    assert sudoku.validate_line([1, 1, 2, 3]) == False


def test_line_validator_negative():
    assert sudoku.validate_line([-1, 1, 2, 3, 4, 5, 6, 7, 8]) == False
    assert sudoku.validate_line([1, 2, 3, 4, 5, -6]) == False
    assert sudoku.validate_line([1, 2, -2]) == False


def test_line_validator_large():
    assert sudoku.validate_line([1, 2, 3, 3, 4, 5, 6, 7, 10]) == False
    assert sudoku.validate_line([10, 2, 3, 3, 4, 5, 6, 7, 8]) == False
    assert sudoku.validate_line([1, 2, 3, 3, 22, 5, 6, 7, 8]) == False
    assert sudoku.validate_line([1, 2, 3, 3, 5]) == False
    assert sudoku.validate_line([12, 4, 1, 3]) == False


def test_validate_lines_duplicate_rows():
    board = [
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
    ]
    assert sudoku.validate_lines(board) == True


def test_validate_rows():
    board = [
        [4, 2, 6, 8, 5, 3, 9, 9, 1],  # invalid first row
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
    ]
    assert sudoku.validate_lines(board) == False

    board = [
        [4, 2, 6, 8, 5, 3, 7, 9, 1],  # invalid last row
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [4, 2, 6, 8, 5, 3, 9, 9, 1],
    ]
    assert sudoku.validate_lines(board) == False


def test_validate_cols():
    # invalid first col
    board = numpy.array([
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [1, 4, 5, 2, 8, 6, 1, 7, 9],
    ])
    assert sudoku.validate_lines(board) == False

    # invalid last col
    board = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 3],
    ]
    assert sudoku.validate_lines(board) == False

    # invalid middle col
    board = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 1, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 3],
    ]
    assert sudoku.validate_lines(board) == False


def test_validate_boards_4_by_4():
    board = [[4, 2, 1, 3], [1, 3, 4, 2], [3, 1, 2, 4], [2, 3, 1, 1]]
    assert sudoku.validate_grid(board) == False

    board = [[1, 3, 4, 2], [3, 1, 2, 4], [2, 4, 3, 1], [4, 2, 1, 3]]
    assert sudoku.validate_grid(board) == False

    board = [[4, 2, 1, 3], [1, 3, 4, 2], [3, 1, 2, 4], [2, 4, 3, 1]]
    assert sudoku.validate_grid(board) == True


def test_validate_boards_9_by_9():
    board = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 0, 3, 4, 9],
        [1, 0, 0, 3, 4, 2, 5, 6, 0],
        [8, 5, 9, 7, 6, 1, 0, 2, 0],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 0, 1, 5, 3, 7, 2, 1, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 0, 0, 4, 8, 1, 1, 7, 9],
    ]
    assert sudoku.validate_grid(board) == False

    board = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9],
    ]
    assert sudoku.validate_grid(board) == True


def test_validate_square():
    board = numpy.array([
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9],
    ])
    assert sudoku.validate_square(board) == True

