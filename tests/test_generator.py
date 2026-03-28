import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sudoku.generator import generate_puzzle

def test_generate_puzzle():
    puzzle = generate_puzzle("easy")
    
    assert puzzle is not None
    assert len(puzzle) == 9
    assert len(puzzle[0]) == 9