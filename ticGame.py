# Function for printing the board to the terminal
def print_board(board):
    print("Here's the board: ")
    print("---------------------------------------------")
    print("     1  2  3")
    print('')
    print("1   " + board[0][0] + " | " + board[0][1] + "| " + board[0][2])
    print("    --+--+--")
    print("2   " + board[1][0] + " | " + board[1][1] + "| " + board[1][2])
    print("    --+--+--")
    print("3   " + board[2][0] + " | " + board[2][1] + "| " + board[2][2])


# Function for checking if there is a winner in the game.
def check_winning(board, current_player):
    # Start checking from horizontal 1st row
    if board[0][0] == board[0][1] == board[0][2] != ' ':
        print_board(board)
        print("Game Over.")
        print("We have a winner!!!")
        print("#### " + current_player + " won. ####")
        return True
    # checking horizontal 2nd row
    elif board[1][0] == board[1][1] == board[1][2] != ' ':
        print_board(board)
        print("Game Over.")
        print("We have a winner!!!")
        print("#### " + current_player + " won. ####")
        return True
    # checking horizontal 3rd row
    elif board[2][0] == board[2][1] == board[2][2] != ' ':
        print_board(board)
        print("Game Over.")
        print("We have a winner!!!")
        print("#### " + current_player + " won. ####")
        return True
    # checking vertical 1st column
    elif board[0][0] == board[1][0] == board[2][0] != ' ':
        print_board(board)
        print("Game Over.")
        print("We have a winner!!!")
        print("#### " + current_player + " won. ####")
        return True
    # checking vertical 2st column
    elif board[0][1] == board[1][1] == board[2][1] != ' ':
        print_board(board)
        print("Game Over.")
        print("We have a winner!!!")
        print("#### " + current_player + " won. ####")
        return True
    # checking vertical 3st column
    elif board[0][2] == board[1][2] == board[2][2] != ' ':
        print_board(board)
        print("Game Over.")
        print("We have a winner!!!")
        print("#### " + current_player + " won. ####")
        return True
    # check for diagonal bottom left to top right
    elif board[2][0] == board[1][1] == board[0][2] != ' ':
        print_board(board)
        print("Game Over.")
        print("We have a winner!!!")
        print("#### " + current_player + " won. ####")
        return True
    # check for diagonal bottom right to top left
    elif board[0][0] == board[1][1] == board[2][2] != ' ':
        print_board(board)
        print("Game Over.")
        print("We have a winner!!!")
        print("#### " + current_player + " won. ####")
        return True


# Function for the core gameplay
def game_state(board, player1, player2):
    game_over = False
    current_player = player1
    turn_count = 0
    turn = "X"
    while not game_over:
        print_board(board)
        print("It's " + current_player + " turn. Please pick the spot using grid coordinate.")
        print("i.e. 11 or 23. (Start from row first then column)")
        move = input(">> ")

        # this is when player is making a move
        if board[int(move[0]) - 1][int(move[1]) - 1] == ' ':
            board[int(move[0]) - 1][int(move[1]) - 1] = turn
            turn_count += 1
        else:
            print("Someone already picked this position. Please try again")
            continue

        # After total of 5 turns, there should be a possible winner in this game.
        if turn_count >= 5:
            game_over = check_winning(board, current_player)

            if turn_count == '9':
                print("Game Over")
                print("We have a draw.")
                game_over = True

        if turn == 'X':
            turn = 'O'
            current_player = player2
        else:
            turn = 'X'
            current_player = player1


def main():
    # Start by initializing the board for the game.
    # here it's a 3x3 board, so use 2d array for this.
    board = [[' ' for i in range(3)] for j in range(3)]

    # This is the copy of the original board, uses for resetting the game.
    boardCopy = [[' ' for i in range(3)] for j in range(3)]

    print("Welcome to tic-tac-toe game classic edition.")
    print("Please enter both names")
    p1 = input("Player 1.\n>> ")
    p2 = input("Player 2.\n>> ")
    game_state(board, p1, p2)

    restart = input("Do you wish to restart the game.\n(y/n)>> ")
    if restart.lower() == 'y':
        board = list(boardCopy)
        game_state(board, p1, p2)
    else:
        quit()


main()
