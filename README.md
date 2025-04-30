Pour lancer le projet, merci de lancer docker et d'utiliser la commande suivante:
  Si vous êtes sur Windows 
   ```shell
   .\bin\start.bat
   ```
   Si vous êtes sur macOS / Linux
   ```shell
   .\bin\start.sh
   ```
Cela installera les dépendances nécessaires au projet et lancera automatiquement le conteneur docker.

# Calculator API

This is a simple calculator API built with FastAPI in Python. It allows you to perform basic arithmetic operations such as addition, subtraction, multiplication, and division.

## Getting Started

To run the calculator API, follow these steps:

1. Install the required dependencies. You can use pip to install the dependencies listed in the `requirements.txt` file:

   ```shell
   pip install -r requirements.txt
   ```

2. Start the server by running the following command:

   ```shell
   uvicorn app:app --reload
   ```

   The server will start running on `http://localhost:8000`.

## Endpoints

The following endpoints are available in the API:

### `/`

- Method: GET
- Description: Home endpoint that provides a simple message about the calculator API.
- Example Response:

  ```json
  {"result": "This is a simple calculator API"}
  ```

### `/add`

- Method: GET
- Description: Performs addition of two numbers.
- Query Parameters:
  - `a` (integer): The first number.
  - `b` (integer): The second number.
- Example Request: `http://localhost:8000/add?a=2&b=3`
- Example Response:

  ```json
  {"result": 5}
  ```

### `/subtract`

- Method: GET
- Description: Performs subtraction of two numbers.
- Query Parameters:
  - `a` (integer): The first number.
  - `b` (integer): The second number.
- Example Request: `http://localhost:8000/subtract?a=5&b=2`
- Example Response:

  ```json
  {"result": 3}
  ```

### `/multiply`

- Method: GET
- Description: Performs multiplication of two numbers.
- Query Parameters:
  - `a` (integer): The first number.
  - `b` (integer): The second number.
- Example Request: `http://localhost:8000/multiply?a=4&b=5`
- Example Response:

  ```json
  {"result": 20}
  ```

### `/divide`

- Method: GET
- Description: Performs division of two numbers.
- Query Parameters:
  - `a` (integer): The first number.
  - `b` (integer): The second number.
- Example Request: `http://localhost:8000/divide?a=10&b=2`
- Example Response:

  ```json
  {"result": 5}
  ```

  Note: If the second number (divisor) is zero, an error response will be returned:

  ```json
  {"error": "Cannot divide by zero."}
  ```

## Contributing

Contributions to the calculator API are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).