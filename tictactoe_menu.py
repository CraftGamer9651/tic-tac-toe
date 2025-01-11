import pygame

#initialize  game
pygame.init()

#constant variables
WIDTH, HEIGHT = 300, 400
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

#drawing screen
def drawGrid():
    #draw 2 horizontal and 2 vertical lines at correct locations
    pygame.draw.line(screen, LINE_COLOR, (100, 0), (100, 300), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 300), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 100), (300, 100), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (300, 200), LINE_WIDTH)

def drawMarks():
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == "X":
                text = FONT.render("X", True, X_COLOR)
                screen.blit(text, (col * 100 + 25, row * 100 + 25))
            elif board[row][col] == "O":
                text = FONT.render("O", True, O_COLOR)
                screen.blit(text, (col * 100 + 25, row * 100 + 25))

def drawButtons():
    #draw horizontal line and the "Exit" and "Reset" buttons
    pygame.draw.rect(screen, (0, 255, 0), (25, 325, 100, 50), 5)
    pygame.draw.rect(screen, (255, 0, 0), (175, 325, 100, 50), 5)

    restart_text = BUTTON_FONT.render("Restart", True, (0,0,0))
    exit_text = BUTTON_FONT.render("Exit", True, (0,0,0))

    restart_rect = restart_text.get_rect(center=(75,350))
    exit_rect = exit_text.get_rect(center=(225,350))

    screen.blit(restart_text, restart_rect)
    screen.blit(exit_text, exit_rect)

def playerMove(row, col):
    global current_player
    #maybe check if spot is empty
    board[row][col] = current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

def resetGame():
    global board
    global current_player
    #reset current player to X
    
    #reset board








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
                if mouseY < 300:
                    row, col = mouseY // 100, mouseX // 100
                    playerMove(row,col)
                elif mouseY > 300 and mouseY <= 400:
                    #if statement to check reset button
                    resetGame()

        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()