import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import json
from app import app

client = app.test_client()

def test_generate_easy():
    res = client.get("/generate?difficulty=easy")
    assert res.status_code == 200


def test_solve():
    board = [[0]*9 for _ in range(9)]

    res = client.post(
        "/solve",
        data=json.dumps({"board": board}),
        content_type="application/json"
    )

    assert res.status_code == 200


def test_validate():
    board = [[0]*9 for _ in range(9)]

    res = client.post(
        "/validate",
        data=json.dumps({"board": board}),
        content_type="application/json"
    )

    assert res.status_code == 200