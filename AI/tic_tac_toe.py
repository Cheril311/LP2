import math

# Constants for the players
PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = " "

# Function to print the Tic-Tac-Toe board
def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], end=" | ")
        print("\n-------------")

# Function to check if a player has won
def check_win(board, player):
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True

    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == player:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# Function to check if the board is full
def is_board_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True

# Function to evaluate the score of the board
def evaluate(board):
    if check_win(board, PLAYER_X):
        return 1
    elif check_win(board, PLAYER_O):
        return -1
    else:
        return 0

# Minimax algorithm
def minimax(board, depth, maximizing_player):
    if check_win(board, PLAYER_X):
        return 1
    elif check_win(board, PLAYER_O):
        return -1
    elif is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
        return min_eval

# Function to find the best move using the Minimax algorithm
def find_best_move(board):
    best_eval = -math.inf
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X
                eval = minimax(board, 0, False)
                board[i][j] = EMPTY

                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)

    return best_move

# Main game loop
def play_game():
    board = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]

    print("Tic-Tac-Toe")
    print("Player X: Human")
    print("Player O: AI")

    print_board(board)

    while True:
        # Human player's turn
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        if board[row][col] == EMPTY:
            board[row][col] = PLAYER_O
        else:
            print("Invalid move! Try again.")
            continue

        print_board(board)

        if check_win(board, PLAYER_O):
            print("Player O wins!")
            break

        if is_board_full(board):
            print("It's a draw!")
            break

        # AI player's turn
        print("AI's turn...")
        best_move = find_best_move(board)
        board[best_move[0]][best_move[1]] = PLAYER_X

        print_board(board)

        if check_win(board, PLAYER_X):
            print("Player X wins!")
            break

        if is_board_full(board):
            print("It's a draw!")
            break

# Start the game
play_game()
