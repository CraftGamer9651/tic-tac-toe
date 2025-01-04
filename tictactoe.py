import pygame

#initialize  game
pygame.init()

#constant variables
WIDTH, HEIGHT = 300, 300
ROWS, COLS = 3 ,3
LINE_WIDTH = 5
LINE_COLOR = (0,0,0)
BG_COLOR = (255,255,255)
X_COLOR = (255,0,0)
O_COLOR = (0,0,255)
FONT = pygame.font.SysFont(None, 80)

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

#draw grid function
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

def showEndScreen(message, color):
    screen.fill((255, 255, 255))
    text = FONT.render(message, True, color)
    text_rect = text.get_rect(center = (WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.update()
    pygame.time.wait(2000)

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

def playerMove(row, col):
    global current_player
    #maybe check if spot is empty
    board[row][col] = current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

def main():
    global current_player

    screen.fill(BG_COLOR)
    drawGrid()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos
                #finish this to update board
                row = mouseY // 100
                col = mouseX // 100
                if board[row][col] == " ":
                    playerMove(row, col)
        
        #check winner
        winner = checkWinner()
        if winner is not None:
            print(winner + " wins!!")
            running = False
            if winner == "X":
                showEndScreen("X wins!", X_COLOR)
            else:
                showEndScreen("O wins!", O_COLOR)
        #Check if board is full
        elif isBoardFull():
            showEndScreen("It's a tie!", (0, 0, 0))
            running = False
        screen.fill(BG_COLOR)
        drawGrid()
        drawMarks()
        pygame.display.update()

if __name__ == "__main__":
    main()