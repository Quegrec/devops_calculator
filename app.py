from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"result": "This is a simple calculator API"}


@app.get("/add")
def add_numbers(a: int, b: int):
    return {"result": a + b}


@app.get("/subtract")
def subtract_numbers(a: int, b: int):
    return {"result": a - b}


@app.get("/multiply")
def multiply_numbers(a: int, b: int):
    return {"result": a * b}


@app.get("/divide")
def divide_numbers(a: int, b: int):
    if b != 0:
        return {"result": a / b}
    else:
        return {"error": "Cannot divide by zero."}
