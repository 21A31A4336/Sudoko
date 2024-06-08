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

def find(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

def isvalid(board, row, col, no):
    # Check the row
    for i in range(len(board[0])):
        if board[row][i] == no:
            return False
    
    # Check the column
    for j in range(len(board)):
        if j >= len(board) or col >= len(board[0]):
            print(f"Index out of range: j={j}, col={col}")
            return False
        if board[j][col] == no:
            return False
    
    # Check the 3x3 sub-grid
    startrow = 3 * (row // 3)
    startcol = 3 * (col // 3)
    for i in range(startrow, startrow + 3):
        for j in range(startcol, startcol + 3):
            if board[i][j] == no:
                return False
    
    return True

def play(board):
    empty = find(board)
    if empty is None:
        return True
    
    i, j = empty
    for no in range(1, 10):
        if isvalid(board, i, j, no):
            board[i][j] = no
            if play(board):
                return True
            board[i][j] = 0
    
    return False

# Example usage
s = play(board)
if s == False:
    print("No solution exists")
else:
    for row in board:
        print(row)