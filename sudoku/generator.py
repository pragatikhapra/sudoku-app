import random
from sudoku.solver import solve_sudoku

# create a fully solved board
def generate_full_board():
    board = [[0 for _ in range(9)] for _ in range(9)]
    solve_sudoku(board)
    return board

# remove cells based on difficulty
def remove_cells(board, difficulty):
    if difficulty == "easy":
        remove_count = 35
    elif difficulty == "medium":
        remove_count = 45
    else:
        remove_count = 55

    removed = 0
    while removed < remove_count:
        row = random.randint(0, 8)
        col = random.randint(0, 8)

        if board[row][col] != 0:
            board[row][col] = 0
            removed += 1

    return board

# generate final puzzle
def generate_puzzle(difficulty="easy"):
    board = generate_full_board()
    puzzle = remove_cells(board, difficulty)
    return puzzle