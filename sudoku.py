# Predefined Sudoku board (0 represents empty cells)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

# Function to display the Sudoku board
def display_board(board):
    print("\nSudoku Board:")
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j] if board[i][j] != 0 else ".", end=" ")
        print()
    print()

# Check if placing a number is valid
def is_valid(board, row, col, num):
    # Check row
    if num in board[row]:
        return False

    # Check column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

# Main Sudoku game loop
def sudoku_game():
    print("Welcome to Sudoku!")
    display_board(board)

    while True:
        try:
            row = int(input("Enter row (1-9): ")) - 1
            col = int(input("Enter column (1-9): ")) - 1
            num = int(input("Enter number (1-9): "))

            if board[row][col] != 0:
                print("Cell is already filled. Try again.")
                continue

            if is_valid(board, row, col, num):
                board[row][col] = num
                display_board(board)

                # Check if the board is fully solved
                if all(0 not in row for row in board):
                    print("Congratulations! You solved the Sudoku!")
                    break
            else:
                print("Invalid move. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers between 1 and 9.")

if __name__ == "__main__":
    sudoku_game()
