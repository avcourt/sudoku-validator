# Sudoku Validators

*A Sudoku grid validator written in Python.*

## Notes

- I used numpy in the basic validator `sudoku.py` for ease of grabbing submatrices and its built-in transpose function

- after deciding to write the more advanced SudokuValidator class, I figured I should try it without any external libraries.
  - `SudokuValidator` uses `zip` with a list comprehension for transpose ala:  `[list(i) for i in zip(*board)]`

- these validators should work on any sudoku board that is a perfect square as the game logic does not change for larger/smaller grids as long as they are perfect squares (although I only included tests for 4x4 and 9x9).
  - *note*: there is no board input validation
  - *note*: 16x16 sudoku puzzles often use a bastardized version of hexadecimal (1,2,3,...,9,10,A,B,C,D,E,F,G) to maintain a single character per cell, but this validator expects decimal digits.

- each program contains a small demo of functionality in the main block

## Assumptions

- no real error checking on input
- assumes a perfect square 2D matrix is provided as input

## Dependencies

Python3, pip3, NumPy, PyTest

`$ pip3 install -U numpy pytest`

## Run

`$ python3 sudoku.py`

or

`$ python3 validator.py`

## Tests

`$ pytest`

## Cleanup

`$ pip3 uninstall numpy pytest`

### Author

Andrew Vaillancourt
andrew.vcourt@gmail.com
