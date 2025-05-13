#create a nested list for the board
board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
#keep track of player (variable)
player = 'X'
#Welcome message
print("Welcome to the Tic-Tak-Toe Game!")
#main game loop

while True:
  #display board w/ nested loops
  empty = 0
  for r in range(len(board)):
    row = board[r]
    for c in range(len(row)):
      if board[r][c] == ' ': empty += 1
      cell = row[c]
      if c < 2:
        print(cell, end=" | ")
    else:
      print(cell, end='')
    if r < 2:
      print('\n---------')
    else:
      print()

  if empty == 0: 
    print("No one won :-(")
    break

  row = input("Player "+ player +", enter row (1-3): ")
  row = int(row) - 1
  col = input("Enter a column (1-3): ")
  col = int(col) - 1

  if board[row][col] == " ":
    board[row][col] = player
  else:
    print("Cell is occupied. Try again!")
    continue

  if (board[0][0] == board[0][1] and board[0][1] == board[0][2]) or \
    (board[1][0] == board[1][1] and board[1][1] == board[1][2]) or \
    (board[2][0] == board[2][1] and board[2][1] == board[2][2]) or \
    (board[0][0] == board[1][1] and board[1][1] == board[2][2]) or \
    (board[0][2] == board[1][1] and board[1][1] == board[2][0]):
    print("You won!")
    
  if player == "X":
    player = "O"
  else:
    player = "X"
    break
