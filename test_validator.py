import pytest
import validator

def test_ordered_line_validator():
    assert validator.validate_line([1, 2, 3, 4, 5, 6, 7, 8, 9]) == True
    assert validator.validate_line([1, 2, 3, 4, 5, 6]) == True
    assert validator.validate_line([1, 2, 3]) == True


def test_unordered_line_validator():
    assert validator.validate_line([8, 7, 6, 4, 5, 2, 1, 3, 9]) == True
    assert validator.validate_line([6, 4, 5, 2, 1, 3]) == True
    assert validator.validate_line([2, 1, 3]) == True


def test_ordered_duplicate_line_validator():
    assert validator.validate_line([1, 2, 3, 3, 4, 5, 6, 7, 8]) == False
    assert validator.validate_line([1, 2, 3, 4, 5, 5, 6]) == False
    assert validator.validate_line([1, 2, 3, 4, 5, 5, 6, 6]) == False
    assert validator.validate_line([1, 1, 2, 3]) == False


def test_line_validator_negative():
    assert validator.validate_line([-1, 1, 2, 3, 4, 5, 6, 7, 8]) == False
    assert validator.validate_line([1, 2, 3, 4, 5, -6]) == False
    assert validator.validate_line([1, 2, -2]) == False


def test_line_validator_large():
    assert validator.validate_line([1, 2, 3, 3, 4, 5, 6, 7, 10]) == False
    assert validator.validate_line([10, 2, 3, 3, 4, 5, 6, 7, 8]) == False
    assert validator.validate_line([1, 2, 3, 3, 22, 5, 6, 7, 8]) == False
    assert validator.validate_line([1, 2, 3, 3, 5]) == False
    assert validator.validate_line([12, 4, 1, 3]) == False


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
    sv = validator.SudokuValidator(board)
    assert sv.validate_rows() == True
    assert sv.validate_cols() == False


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
    sv = validator.SudokuValidator(board)
    assert sv.validate_rows() == False
    assert sv.validate_cols() == False

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
    sv = validator.SudokuValidator(board)
    assert sv.validate_rows() == False
    assert sv.validate_cols() == False

def test_validate_cols():
    # invalid first col
    board = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [1, 4, 5, 2, 8, 6, 1, 7, 9],
    ]

    sv = validator.SudokuValidator(board)
    assert sv.validate_rows() == False
    assert sv.validate_cols() == False

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
    sv = validator.SudokuValidator(board)
    assert sv.validate_rows() == False
    assert sv.validate_cols() == False

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
    sv = validator.SudokuValidator(board)
    assert sv.validate_rows() == False
    assert sv.validate_cols() == False

def test_validate_boards_4_by_4():
    board = [[4, 2, 1, 3],
             [1, 3, 4, 2], 
             [3, 1, 2, 4], 
             [2, 3, 1, 1]]
    sv = validator.SudokuValidator(board)
    assert sv.valid_board == False

    board = [[1, 3, 4, 2], [3, 1, 2, 4], [2, 4, 3, 1], [4, 2, 1, 3]]
    sv = validator.SudokuValidator(board)
    assert sv.valid_board == False

    board = [[4, 2, 1, 3], [1, 3, 4, 2], [3, 1, 2, 4], [2, 4, 3, 1]]
    sv = validator.SudokuValidator(board)
    assert sv.valid_board == True

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
    sv = validator.SudokuValidator(board)
    assert sv.valid_board == False

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
    sv = validator.SudokuValidator(board)
    assert sv.valid_board == True

def test_num_invalid_rows():
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
    sv = validator.SudokuValidator(board)
    assert len(sv.invalid_rows) == 1
    assert 0 in sv.invalid_rows
    assert 3 not in sv.invalid_rows

    board = [
        [4, 2, 6, 8, 5, 3, 9, 9, 1],  # invalid first row
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [4, 2, 6, 8, 5, 3, 9, 9, 1], # invalid row
    ]
    sv = validator.SudokuValidator(board)
    assert len(sv.invalid_rows) == 2
    assert 0 in sv.invalid_rows
    assert 8 in sv.invalid_rows
    assert 3 not in sv.invalid_rows
    assert sv.invalid_rows[0] == [4, 2, 6, 8, 5, 3, 9, 9, 1]

def test_valid_squares():
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
    sv = validator.SudokuValidator(board)
    assert sv.valid_board == True
    assert sv.validate_squares() == True

    board = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],

    ]
    sv = validator.SudokuValidator(board)
    assert sv.valid_board == False
    assert sv.validate_squares() == False
