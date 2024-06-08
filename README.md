# Sudoko
It is a game developed using dynamic programming in python
Sudoku Solver
This is a Python script that solves a given Sudoku puzzle using backtracking. The script includes functions to find empty spaces on the board, check if placing a number is valid according to Sudoku rules, and recursively attempt to solve the puzzle.
************************************************************************************
Getting Started
Prerequisites
Python 3.x
Usage
The Sudoku board is represented as a 2D list, where empty cells are denoted by 0. The script attempts to solve the provided board and prints the solution if one exists.
*************************************************************************************
Example Sudoku Board
The initial Sudoku board is defined as follows:
board = [
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
****************************************************************************************
Functions
find(board)
Finds the first empty space (denoted by 0) on the Sudoku board.
Parameters:
board: A 2D list representing the Sudoku board.
Returns:
A tuple (i, j) representing the row and column indices of the first empty space, or None if the board is full.
isvalid(board, row, col, no)
Checks if placing a number no at position (row, col) on the board is valid according to Sudoku rules.
******************************************************************************************
Parameters:
board: A 2D list representing the Sudoku board.
row: Row index where the number is to be placed.
col: Column index where the number is to be placed.
no: The number to be placed.
Returns:
True if placing the number is valid, False otherwise.
play(board)
Attempts to solve the Sudoku puzzle using backtracking.
*****************************************************************************************************
Parameters:
board: A 2D list representing the Sudoku board.
Returns:
True if the board is solved, False otherwise.
Example Usage
To use the script, simply run it. The initial board will be solved (if possible), and the solution will be printed.
******************************************************************************************************
python
# Example usage
s = play(board)
if s == False:
    print("No solution exists")
else:
    for row in board:
        print(row)
Output
If a solution exists, the solved Sudoku board will be printed:
[5, 3, 4, 6, 7, 8, 9, 1, 2]
[6, 7, 2, 1, 9, 5, 3, 4, 8]
[1, 9, 8, 3, 4, 2, 5, 6, 7]
[8, 5, 9, 7, 6, 1, 4, 2, 3]
[4, 2, 6, 8, 5, 3, 7, 9, 1]
[7, 1, 3, 9, 2, 4, 8, 5, 6]
[9, 6, 1, 5, 3, 7, 2, 8, 4]
[2, 8, 7, 4, 1, 9, 6, 3, 5]
[3, 4, 5, 2, 8, 6, 1, 7, 9]
******************************************************************************************************
If no solution exists, the following message will be printed:
No solution exists
******************************************************************************************************
Notes
Ensure the initial board is a valid Sudoku puzzle for meaningful results.
The script uses a backtracking algorithm, which may not be efficient for very large or complex puzzles.
