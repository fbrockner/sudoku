#set up pygame
import pygame, sys

backgroundColor = (251,247,245)
originalElementColor = (52, 31, 151)

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

#prints sudoku board
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

#input cell from board and check if it is 0 o
def isEmpty(num):
    if (num == 0):
        return True
    return False

#check is guess is a valid solution
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



def main():
    pygame.init()
    screen = pygame.display.set_mode((550,550))
    pygame.display.set_caption("Sudoku")
    screen.fill(backgroundColor)
    myfont = pygame.font.SysFont("Comic Sans MS",35)
    #create grid
    for i in range(10):
        #bold lines for each 3x3 square
        if (i % 3 == 0):
            #vertical lines
            pygame.draw.line(screen, (0,0,0), (50 + 50 * i, 50), (50 + 50 * i, 500), 4)
            #horizontal lines
            pygame.draw.line(screen, (0,0,0), (50, 50 + 50 * i), (500, 50 + 50 * i), 4)

        #vertical lines
        pygame.draw.line(screen, (0,0,0), (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
        #horizontal lines
        pygame.draw.line(screen, (0,0,0), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)
    pygame.display.update()
    

    for i in range(0,9):
        for j in range(0,9):
            if (board[i][j] < 10 and board[i][j] > 0):
                value = myfont.render(str(board[i][j]), True, originalElementColor)
                screen.blit(value, ((j + 1) * 50 + 15, (i + 1) * 50))
    pygame.display.update()

    solver()

    pygame.display.update()   

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

main()