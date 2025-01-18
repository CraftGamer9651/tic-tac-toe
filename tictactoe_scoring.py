import pygame

'''
Ideas:
- Instead of coordinates to check mouse click, use rect to check mouse click
'''

#initialize  game
pygame.init()

#constant variables
WIDTH, HEIGHT = 300, 500
ROWS, COLS = 3 ,3
LINE_WIDTH = 5
LINE_COLOR = (0,0,0)
BG_COLOR = (255,255,255)
X_COLOR = (255,0,0)
O_COLOR = (0,0,255)
FONT = pygame.font.Font('BurbankBigCondensed-Black.otf', 80)
BUTTON_FONT = pygame.font.Font('BurbankBigCondensed-Black.otf', 34)

#intialize screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

#creating main game board
board = []
for i in range(ROWS):
    row = []
    for j in range (COLS):
        row.append(" ")
    board.append(row)

#track turns
current_player = "X"

#DRAWING FUNCRIONS

#drawing screen
def drawGrid():
    #draw 2 horizontal and 2 vertical lines at correct locations
    pygame.draw.line(screen, LINE_COLOR, (100, 100), (100, 400), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (200, 100), (200, 400), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (300, 200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 300), (300, 300), LINE_WIDTH)

def drawMarks():
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == "X":
                text = FONT.render("X", True, X_COLOR)
                screen.blit(text, (col * 100 + 25, (row + 1) * 100 + 25))
            elif board[row][col] == "O":
                text = FONT.render("O", True, O_COLOR)
                screen.blit(text, (col * 100 + 25, (row + 1) * 100 + 25))

def drawButtons():
    #draw horizontal line and the "Exit" and "Reset" buttons
    #pygame.draw.rect(screen, (r, g, b), (x, y, w, h), line thickness)
    pygame.draw.rect(screen, (0, 255, 0), (25, 425, 100, 50))
    pygame.draw.rect(screen, (0, 133, 0), (25, 425, 100, 50), 5)
    pygame.draw.rect(screen, (255, 0, 0), (175, 425, 100, 50))
    pygame.draw.rect(screen, (133, 0, 0), (175, 425, 100, 50), 5)

    restart_text = BUTTON_FONT.render("Restart", True, (0,0,0))
    exit_text = BUTTON_FONT.render("Exit", True, (0,0,0))

    restart_rect = restart_text.get_rect(center=(75,450))
    exit_rect = exit_text.get_rect(center=(225,450))

    screen.blit(restart_text, restart_rect)
    screen.blit(exit_text, exit_rect)

def showEndScreen(message, color):
    screen.fill((255, 255, 255))
    text = FONT.render(message, True, color)
    text_rect = text.get_rect(center = (WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.update()
    pygame.time.wait(2000)

#BACKEND LOGIC FUNCTIONS

def playerMove(row, col):
    global current_player
    #maybe check if spot is empty
    if board[row][col] == " ":
        board[row][col] = current_player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

def resetGame():
    global board
    global current_player
    #reset current player to X
    current_player = "X"
    #reset board
    print("Resetting game board")
    board = []
    for i in range(ROWS):
        row = []
        for j in range (COLS):
            row.append(" ")
        board.append(row)

def quitGame():
    #implement any extra functionality when quitting game

    pygame.quit()
    print("Quitting game...")

def checkWinner():
    #rows
    if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] != " ":
        return board[0][0]
    elif board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] != " ":
        return board[1][0]
    elif board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] != " ":
        return board[2][0]
    
    #cols
    if board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] != " ":
        return board[0][0]
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] != " ":
        return board[0][1]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] != " ":
        return board[0][2]
    
    #diagonals
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    elif board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] != " ":
        return board[2][0]
    return None

def isBoardFull():
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def main():
    global current_player
    running = True
    while running:
        screen.fill(BG_COLOR)
        drawGrid()
        drawMarks()
        drawButtons()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos
                if mouseY >= 100 and mouseY < 400:
                    row, col = mouseY // 100, mouseX // 100
                    playerMove(row - 1,col)
                #Checks if clicking in bottom area
                elif mouseY >= 425 and mouseY <= 475:
                    #if statement to check reset button
                    if mouseX >= 25 and mouseX <= 125:
                        resetGame()
                    elif mouseX >= 175 and mouseX <= 275:
                        pygame.quit()
                        return
                    
        winner = checkWinner()
        if winner is not None:
            print(winner + " wins!!")
            if winner == "X":
                showEndScreen("X wins!", X_COLOR)
            else:
                showEndScreen("O wins!", O_COLOR)
            resetGame()
        #Check if board is full
        elif isBoardFull():
            showEndScreen("It's a tie!", (0, 0, 0))
            resetGame() 
                    

        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()