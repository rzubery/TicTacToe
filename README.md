# Tic Tac Toe Game

This is a simple Tic Tac Toe game implemented in Python.

## Overview

The game allows two players to play Tic Tac Toe in the console. Players take turns placing their markers ('X' or 'O') on a 3x3 grid. The game checks for wins and draws, and prompts the players to play again.

## Code Description

The Python code consists of several functions:

-   `display_board(board)`: Prints the current state of the Tic Tac Toe board.
-   `player_input()`: Prompts Player 1 to choose their marker ('X' or 'O') and returns the markers for both players.
-   `place_marker(board, marker, position)`: Places the player's marker on the board at the specified position.
-   `win_check(board, mark)`: Checks if the given marker has won the game.
-   `choose_first()`: Randomly selects which player goes first.
-   `space_check(board, position)`: Checks if a space on the board is empty.
-   `full_board_check(board)`: Checks if the board is full (draw).
-   `player_choice(board)`: Prompts the current player to choose a position (1-9).
-   `replay()`: Asks if the players want to play again.

The main game loop initializes the board, determines the first player, and handles the turns until a player wins or the game ends in a draw.

## How to Run

1.  **Save the code:** Save the provided Python code to a file named `tic_tac_toe.py`.
2.  **Run the script:** Open a terminal or command prompt and navigate to the directory where you saved the file. Then, execute the script using the command:

    ```bash
    python tic_tac_toe.py
    ```

3.  **Follow the prompts:** The game will prompt you to choose your marker and enter positions. Follow the instructions displayed in the console to play the game.

## Game Logic

1.  The game starts by displaying a welcome message.
2.  Player 1 chooses their marker ('X' or 'O').
3.  The game randomly determines who goes first.
4.  The players take turns placing their markers on the board.
5.  After each turn, the game checks for a win or a draw.
6.  If a player wins or the board is full, the game ends.
7.  The players are prompted to play again.
