# Initialize the board
def create_board():
    return [" " for _ in range(9)]

# Display the board
def display_board(board):
    print("\n")
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("--+---+--")
    print("\n")

# Check for a winner
def check_winner(board, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Check if the board is full
def is_full(board):
    return " " not in board

# Player move
def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Cell is already occupied. Try again.")
        except (IndexError, ValueError):
            print("Invalid move. Enter a number between 1 and 9.")

# AI move (simple random choice)
def ai_move(board):
    import random
    empty_cells = [i for i in range(9) if board[i] == " "]
    move = random.choice(empty_cells)
    board[move] = "O"

# Main game loop
def tic_tac_toe():
    board = create_board()
    print("Welcome to Tic-Tac-Toe!")
    display_board(board)

    while True:
        # Player move
        player_move(board)
        display_board(board)
        if check_winner(board, "X"):
            print("Congratulations! You win!")
            break
        if is_full(board):
            print("It's a tie!")
            break

        # AI move
        print("AI is making its move...")
        ai_move(board)
        display_board(board)
        if check_winner(board, "O"):
            print("AI wins! Better luck next time.")
            break
        if is_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    tic_tac_toe()
