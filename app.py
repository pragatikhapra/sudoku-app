from flask import Flask, request, jsonify, render_template
from sudoku.solver import solve_sudoku
from sudoku.generator import generate_puzzle
from sudoku.validator import is_valid_board

app = Flask(__name__)

@app.route("/")
def home():
    return "Sudoku API is running!"

# NEW UI ROUTE
@app.route("/ui")
def ui():
    return render_template("index.html")

@app.route("/generate", methods=["GET"])
def generate():
    difficulty = request.args.get("difficulty", "easy")
    puzzle = generate_puzzle(difficulty)
    return jsonify({"difficulty": difficulty, "puzzle": puzzle})

@app.route("/solve", methods=["POST"])
def solve():
    data = request.get_json()
    board = data["board"]
    solution = solve_sudoku(board)
    return jsonify({"solution": solution})

@app.route("/validate", methods=["POST"])
def validate():
    data = request.get_json()
    board = data["board"]
    valid = is_valid_board(board)
    return jsonify({"valid": valid})

if __name__ == "__main__":
    app.run(debug=True)