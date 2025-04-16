import pygame

'''
Ideas:
- Instead of coordinates to check mouse click, use rect to check mouse click
'''

# initialize the game
pygame.init()

# constant variables
WIDTH, HEIGHT = 300, 500
ROWS, COLS = 3 ,3
LINE_WIDTH = 5
LINE_COLOR = (0,0,0)
BG_COLOR = (255,255,255)
X_COLOR = (255,0,0)
O_COLOR = (0,0,255)
FONT = pygame.font.Font('BurbankBigCondensed-Black.otf', 80)
BUTTON_FONT = pygame.font.Font('BurbankBigCondensed-Black.otf', 34)
SCORE_FONT = pygame.font.Font('BurbankBigCondensed-Black.otf', 60)

# intialize the screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

# creating main game board
board = []
for i in range(ROWS):
    row = []
    for j in range (COLS):
        row.append(" ")
    board.append(row)

# tracking turns
current_player = "X"

# ----------------- #
# DRAWING FUNCRIONS #
# ----------------- #

# drawing all lines
def drawGrid():

    # draws the horizontal and vertical lines at correct locations
    pygame.draw.line(screen, LINE_COLOR, (100, 100), (100, 400), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (200, 100), (200, 400), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (300, 200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 300), (300, 300), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 100), (300, 100), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (300, 400), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (150, 0), (150, 100), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (150, 400), (150, 500), LINE_WIDTH)

# draws the 'X' and 'O' marks from playerMove
def drawMarks():
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == "X":
                text = FONT.render("X", True, X_COLOR)
                screen.blit(text, (col * 100 + 25, (row + 1) * 100 + 25))
            elif board[row][col] == "O":
                text = FONT.render("O", True, O_COLOR)
                screen.blit(text, (col * 100 + 25, (row + 1) * 100 + 25))

# draws the "Exit" and "Reset" buttons
def drawButtons():

    # pygame.draw.rect(screen, (r, g, b), (x, y, w, h), line thickness)
    pygame.draw.rect(screen, (0, 255, 0), (25, 425, 100, 50))
    pygame.draw.rect(screen, (0, 133, 0), (25, 425, 100, 50), 5)
    pygame.draw.rect(screen, (255, 0, 0), (175, 425, 100, 50))
    pygame.draw.rect(screen, (133, 0, 0), (175, 425, 100, 50), 5)

    # renders the text for buttons
    restart_text = BUTTON_FONT.render("Restart", True, (0,0,0))
    exit_text = BUTTON_FONT.render("Exit", True, (0,0,0))

    # defines the rect for buttons
    restart_rect = restart_text.get_rect(center=(75,450))
    exit_rect = exit_text.get_rect(center=(225,450))

    # places the text over the rect
    screen.blit(restart_text, restart_rect)
    screen.blit(exit_text, exit_rect)
    

# draws the score at top
def drawScore():

    # renders the scores
    x_score_text = SCORE_FONT.render("X: "+str(x_score), True, X_COLOR)
    o_score_text = SCORE_FONT.render("O: "+str(o_score), True, O_COLOR)

    # defines the rect for score
    x_score_rect = x_score_text.get_rect(center=(75,50))
    o_score_rect = o_score_text.get_rect(center=(225,50))

    # places the text over the rect
    screen.blit(x_score_text, x_score_rect)
    screen.blit(o_score_text, o_score_rect)

# fills the screen with (message)
def showEndScreen(message, color):
    screen.fill((255, 255, 255))

    # renders the text from message
    text = FONT.render(message, True, color)

    # defined the rect for the message
    text_rect = text.get_rect(center = (WIDTH // 2, HEIGHT // 2))

    # places the text over the rect
    screen.blit(text, text_rect)

    # updates the screen when finished
    pygame.display.update()
    pygame.time.wait(2000)

# ----------------------- #
# BACKEND LOGIC FUNCTIONS #
# ----------------------- #

# sets the current_player's mark at spot
def playerMove(row, col):
    global current_player

    # checks if spot is empty
    if board[row][col] == " ":

        # puts mark of current_player in spot
        board[row][col] = current_player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

# erases "X" and "O" marks
def resetGame():
    global board
    global current_player

    # set current player to X
    current_player = "X"

    # reset board
    board = []
    for i in range(ROWS):
        row = []
        for j in range (COLS):
            row.append(" ")
        board.append(row)

# checks every possible winner combinations
def checkWinner():
    # rows
    if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] != " ":
        return board[0][0]
    elif board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] != " ":
        return board[1][0]
    elif board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] != " ":
        return board[2][0]
    
    # cols
    if board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] != " ":
        return board[0][0]
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] != " ":
        return board[0][1]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] != " ":
        return board[0][2]
    
    # diagonals
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    elif board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] != " ":
        return board[2][0]
    return None

# checks for tie
def isBoardFull():
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

# main function
def main():
    global current_player, x_score, o_score
    x_score = 0
    o_score = 0
    running = True
    while running:
        screen.fill(BG_COLOR)
        drawGrid()
        drawMarks()
        drawButtons()
        drawScore()

        for event in pygame.event.get():
            # checks for pygame.quit
            if event.type == pygame.QUIT:
                running = False
            # checks where mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos
                # checks if mouse clicked in a square
                if mouseY >= 100 and mouseY < 400:
                    row, col = mouseY // 100, mouseX // 100
                    playerMove(row - 1,col)
                # checks if clicking in bottom area
                elif mouseY >= 425 and mouseY <= 475:
                    # check if "RESET" button clicked
                    if mouseX >= 25 and mouseX <= 125:
                        resetGame()
                        x_score = 0
                        o_score = 0
                    # check if reset "EXIT" clicked
                    elif mouseX >= 175 and mouseX <= 275:
                        print("Game quitted")
                        pygame.quit()
                        return
        
        winner = checkWinner()
        if winner is not None:
            # says who winner is, adds 1 to their score
            if winner == "X":
                showEndScreen("X wins!", X_COLOR)
                x_score += 1
            else:
                showEndScreen("O wins!", O_COLOR)
                o_score += 1
            resetGame()
        # check if board is full
        elif isBoardFull():
            showEndScreen("It's a tie!", (0, 0, 0))
            resetGame() 
                    

        pygame.display.update()
    print("Program closed")
    pygame.quit()

if __name__ == "__main__":
    main()
