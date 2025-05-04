import os
import sys

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)  # Ajouter le répertoire racine au chemin Python

from fastapi.testclient import TestClient

from app import app  # Importing the FastAPI app object directly

client = TestClient(app)


def test_add():
    response = client.get("/add?a=5&b=3")
    assert response.status_code == 200
    assert response.json()["result"] == 8


def test_subtract():
    response = client.get("/subtract?a=5&b=3")
    assert response.status_code == 200
    assert response.json()["result"] == 2


def test_multiply():
    response = client.get("/multiply?a=5&b=3")
    assert response.status_code == 200
    assert response.json()["result"] == 15


def test_divide():
    response = client.get("/divide?a=6&b=3")
    assert response.status_code == 200
    assert response.json()["result"] == 2


def test_divide_by_zero():
    response = client.get("/divide?a=5&b=0")
    assert response.status_code == 200
    assert response.json()["error"] == "Cannot divide by zero."
