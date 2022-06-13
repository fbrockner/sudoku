# 1. look for empty cell
# 2. fill cell with values 1-9 until acceptable solution
#   use recursion
#   rules:  1. horizontally must have num 1-9
#           2. vertically must have num 1-9
#           3. each 3x3 block must have num 1-9
#   if no acceptable solutions go back step

board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

def displayBoard():
    for i in range(9):
            print(board[i])

#check if there are any empty cells 
def emptyCell():
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    #if there are no empty spaces
    return -1, -1

def validNum(num, emptyCellRow, emptyCellCol):

    #check rows
    #go through each column but keep the same row index
    for k in range(9):
        if board[emptyCellRow][k] == num:
            return False

    #check columns 
    #go down each row but keep the same column index
    for m in range(9):
        if board[m][emptyCellCol] == num:
            return False

    #check 3x3 square
    rowStart = (emptyCellRow // 3) * 3
    colStart = (emptyCellCol // 3) * 3

    for r in range(rowStart, rowStart + 3):
        for c in range(colStart, colStart + 3):
            if board[r][c] == num:
                return False
    
    #if num passes all three checks then the num is correct
    return True

#solver? i barely know her!!
#returns true or false if there is a solution for the board
def solver():

    row, col = emptyCell()

    #if there are no empty cells then the puzzle is finished
    if row == -1 or col == -1:
        return True

    for num in range(1,10):
        if validNum(num, row, col):
            board[row][col] = num
            if solver():
                return True
        board[row][col] = 0
    

displayBoard()
print()
solver()
displayBoard()
