import pygame, sys

backgroundColor = (255,255,255)
originalElementColor = (255,0,0)
elementColor =  (255, 181, 194)
isSolved = 0
board = [
[7,0,0,0,0,0,0,8,0],
[0,5,0,0,7,0,0,0,0],
[9,0,0,5,0,8,0,4,0],
[0,2,0,0,9,0,4,6,0],
[8,0,6,0,0,0,7,0,5],
[0,9,4,0,8,0,0,2,0],
[0,8,0,7,0,6,0,0,1],
[0,0,0,0,2,0,0,3,0],
[0,1,0,0,0,0,0,0,9]
]

#check if cell is empty, denoted by 0
def isEmpty(num):
    if (num == 0):
        return True
    return False

#check is guess is a valid solution
def isValidNum(num, emptyCellRow, emptyCellCol):
    #check if num is unique in row
    for k in range(0,9):
        if (board[emptyCellRow][k] == num):
            return False

    #check if num is unique in column
    for m in range(0,9):
        if (board[m][emptyCellCol] == num):
            return False

    #check if num is unique in 3x3 square
    rowStart = (emptyCellRow // 3) * 3
    colStart = (emptyCellCol // 3) * 3
    for r in range(rowStart, rowStart + 3):
        for c in range(colStart, colStart + 3):
            if (board[r][c] == num):
                return False
    
    #if num passes all three checks then the num is correct
    return True

#display and solve backtracking algorithm in real-time
def solver(screen):
    myfont = pygame.font.SysFont("Futura",35)
    buffer = 5

    #test out numbers 1-9 in empty cell
    for i in range(0,9):
        for j in range(0,9):
            if isEmpty(board[i][j]): 
                for num in range(1,10):
                    if (isValidNum(num, i, j)):
                        board[i][j] = num
                        pygame.draw.rect(screen, backgroundColor, ((j + 1) * 50 + buffer, (i + 1) * 50 + buffer,50 - 2 * buffer, 50 - 2 * buffer))
                        value = myfont.render(str(num), True, elementColor)
                        screen.blit(value, ((j + 1) * 50 + 15, (i + 1) * 50))
                        pygame.display.update()
                        pygame.time.delay(25)
                        solver(screen)

                        global isSolved
                        if (isSolved == 1):
                            return

                        #if solver() returns then num tested in wrong, set it back to zero
                        board[i][j] = 0
                        pygame.draw.rect(screen, backgroundColor, ((j + 1) * 50 + buffer, (i +1) * 50 + buffer, 50 - 2 * buffer , 50 - 2 * buffer))
                        pygame.display.update()
                return
    isSolved = 1

def main():
    #intialize pygame window, font, caption, background color
    pygame.init()
    screen = pygame.display.set_mode((550,550))
    pygame.display.set_caption("Sudoku Solver")
    screen.fill(backgroundColor)
    myfont = pygame.font.SysFont("Futura",35)

    #create 9x9 grid
    for i in range(10):
        #bold lines for each 3x3 square
        if (i % 3 == 0):
            pygame.draw.line(screen, (0,0,0), (50 + 50 * i, 50), (50 + 50 * i, 500), 4)
            pygame.draw.line(screen, (0,0,0), (50, 50 + 50 * i), (500, 50 + 50 * i), 4)

        pygame.draw.line(screen, (0,0,0), (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
        pygame.draw.line(screen, (0,0,0), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)

    pygame.display.update()
    
    #display original sudoku puzzle values
    for i in range(0,9):
        for j in range(0,9):
            if (board[i][j] != 0):
                value = myfont.render(str(board[i][j]), True, originalElementColor)
                screen.blit(value, ((j + 1) * 50 + 15, (i + 1) * 50))
    pygame.display.update()

    #run backtracking algorithm
    solver(screen)

    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                return False

main()