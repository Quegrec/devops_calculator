import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_add_then_divide():
    # 1. On additionne 8 + 2 = 10
    add_response = client.get("/add?a=8&b=2")
    assert add_response.status_code == 200
    sum_result = add_response.json()["result"]
    assert sum_result == 10

    # 2. On divise 10 / 2 = 5
    divide_response = client.get("/divide?a={}&b=2".format(sum_result))
    assert divide_response.status_code == 200
    assert divide_response.json()["result"] == 5
