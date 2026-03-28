import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sudoku.validator import is_valid_board

def test_valid_board():
    board = [
        [5,3,4,6,7,8,9,1,2],
        [6,7,2,1,9,5,3,4,8],
        [1,9,8,3,4,2,5,6,7],
        [8,5,9,7,6,1,4,2,3],
        [4,2,6,8,5,3,7,9,1],
        [7,1,3,9,2,4,8,5,6],
        [9,6,1,5,3,7,2,8,4],
        [2,8,7,4,1,9,6,3,5],
        [3,4,5,2,8,6,1,7,9]
    ]

    assert is_valid_board(board) == True


def test_invalid_board():
    board = [
        [5,5,0,0,7,0,0,0,0],  # duplicate
    ] * 9

    assert is_valid_board(board) == False