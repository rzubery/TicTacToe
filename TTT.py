def display_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])


def player_input():
    marker = ""
    while marker not in ["X", "O"]:
        marker = input("Player 1, choose X or O: ").upper()
    if marker == "X":
        return ("X", "O")
    else:
        return ("O", "X")


def place_marker(board, marker, position):
    board[position - 1] = marker


def win_check(board, mark):
    return (
        (board[0] == mark and board[1] == mark and board[2] == mark)
        or (board[3] == mark and board[4] == mark and board[5] == mark)
        or (board[6] == mark and board[7] == mark and board[8] == mark)
        or (board[0] == mark and board[3] == mark and board[6] == mark)
        or (board[1] == mark and board[4] == mark and board[7] == mark)
        or (board[2] == mark and board[5] == mark and board[8] == mark)
        or (board[0] == mark and board[4] == mark and board[8] == mark)
        or (board[2] == mark and board[4] == mark and board[6] == mark)
    )


def choose_first():
    import random

    if random.randint(0, 1) == 0:
        return "Player 1"
    else:
        return "Player 2"


def space_check(board, position):
    return board[position - 1] == " "


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0
    while position not in range(1, 10) or not space_check(board, position):
        try:
            position = int(input("Choose a position (1-9): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
    return position


def replay():
    return input("Do you want to play again? Enter Yes or No: ").lower().startswith("y")


print("Welcome to Tic Tac Toe!")

while True:
    the_board = [" "] * 9
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + " will go first.")

    game_on = True

    while game_on:
        if turn == "Player 1":
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)

            if win_check(the_board, player1_marker):
                print("GG you win!")
                exit()
