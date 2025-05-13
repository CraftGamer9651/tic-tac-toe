How to Play:
 - Make sure that "BurbankBigCondensedBlack.otf" is in the sam folder as 

Functions:
 - drawGrid() - Draws all the lines for the playing grid
 - drawMarks() - Draws the "X" player and the "O" player in the grid lines
 - drawButtons() - Draws the "Restart" and "Exit" buttons on the bottom of the screen
 - showEndScreen() - Draws the text for who wins
 - playerMove() - Calculates if the player is "X" or "O" and if the player's spot choice is full or empty
 - resetGame() - Resets the game score, the position of the players, and whose turn it is
 - quitGame() - Quits the game
 - checkWinner() - Checks every combination to see if "X" or "O" wins
 - isBoardFull() - Checks if the board is full, if so it is a tie
 - main() - The main function

MVP:
 - Multiplayer tic-tac-toe game where two players take turns clicking on the square that they want to play in
 - Not checking for winners
 - Not checking for placing in the same spot

Potential Functions:
 - drawBoard(): A function to draw the playing board
 - playerMove(): A function to detect player input and update the board

Extra Post MVP:
 - checkWinner(): Checks for a winner
 - checkBoardFull(): Checks if board is full
 - AIPlayer(): Implements ad AI player option

MVP presudocode:
1. Initializing the game
2. Create constant variables
3. Create main board for the game
4. Create a variable to keep track of the player movements
5. Draw the grid / working on drawBoard()
6. Main game loop
    a. Check for player click and then update the board
    b. Redraw the screen
