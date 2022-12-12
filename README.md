# Sudoku Solver

This python file uses recursion and backtracking to find all possible solutions for a sudoku puzzle.

Usage

To use this solver, simply pass a 2D list representing your sudoku puzzle to the solve function. The function will return a list of all possible solutions for the puzzle.

Example


# Create an unsolved puzzle
Grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Find all possible solutions for the puzzle
solutions = solve(unsolved_puzzle)

This solver assumes that the provided puzzle is properly formatted (i.e. a 9x9 2D list with numbers in the range 0-9).
The solve function may take a few moments to run for difficult puzzles. This is due to the use of recursion and backtracking.
Helper Functions

The following helper functions are included in this file:

possible(x, y, n) - Returns True if it is possible to place the number n at the given x, y coordinates in the given grid, and False otherwise.
print_grid(x) - Prints the given grid in a human-readable format.
