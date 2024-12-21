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
    print()

def playerMove():
    print()

def main():
    global current_player

    screen.fill(BG_COLOR)
    drawGrid()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos
                #finish this to update board
        screen.fill(BG_COLOR)
        drawGrid()
        playerMove()
        pygame.display.update()

if __name__ == "__main__":
    main()