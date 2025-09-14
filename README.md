# Todo API

This is a simple Todo API built with FastAPI and Tortoise-ORM. It allows users to register, login, and manage their todos.

## Features

*   User registration and authentication with JWT.
*   CRUD operations for todos (Create, Read, Update, Delete).
*   Password hashing.
*   Async support.
*   SQLite database.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/todo-api.git
    cd todo-api
    ```

2.  **Install dependencies:**

    Make sure you have Python 3.12+ and Poetry installed.

    ```bash
    poetry install
    ```

## Running the Application

To run the development server, use the following command:

```bash
poetry run uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## API Endpoints

The base URL for all endpoints is `/`.

### Authentication

#### `POST /login`

Authenticates a user and returns a JWT token.

**Request body:**

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

**Response:**

```json
{
  "access_token": "your_access_token",
  "token_type": "bearer"
}
```

### Users

#### `POST /register`

Registers a new user.

**Request body:**

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

**Response:**

```json
{
  "id": 1,
  "username": "your_username"
}
```

#### `GET /users/me`

Returns the current authenticated user's information.

**Authentication:** Bearer token required.

**Response:**

```json
{
  "id": 1,
  "username": "your_username"
}
```

#### `PUT /users/me`

Updates the current authenticated user's information.

**Authentication:** Bearer token required.

**Request body:**

```json
{
  "username": "new_username",
  "password": "new_password"
}
```

**Response:**

```json
{
  "id": 1,
  "username": "new_username"
}
```

### Todos

#### `POST /todos`

Creates a new todo for the authenticated user.

**Authentication:** Bearer token required.

**Request body:**

```json
{
  "title": "My first todo",
  "description": "This is a description of my first todo."
}
```

**Response:**

```json
{
  "id": 1,
  "title": "My first todo",
  "description": "This is a description of my first todo.",
  "done": false
}
```

#### `GET /todos`

Returns a list of all todos for the authenticated user.

**Authentication:** Bearer token required.

**Response:**

```json
[
  {
    "id": 1,
    "title": "My first todo",
    "description": "This is a description of my first todo.",
    "done": false
  }
]
```

#### `GET /todos/{todo_id}`

Returns a single todo by its ID.

**Authentication:** Bearer token required.

**Response:**

```json
{
  "id": 1,
  "title": "My first todo",
  "description": "This is a description of my first todo.",
  "done": false
}
```

#### `PUT /todos/{todo_id}`

Updates a todo by its ID.

**Authentication:** Bearer token required.

**Request body:**

```json
{
  "title": "Updated title",
  "description": "Updated description.",
  "done": true
}
```

**Response:**

```json
{
  "id": 1,
  "title": "Updated title",
  "description": "Updated description.",
  "done": true
}
```

#### `DELETE /todos/{todo_id}`

Deletes a todo by its ID.

**Authentication:** Bearer token required.

**Response:**

`204 No Content`

## Running Tests

To run the tests, use the following command:

```bash
poetry run pytest
```

## Project Structure

```
├── app/
│   ├── api/
│   │   ├── endpoints/
│   │   │   ├── login.py
│   │   │   ├── todos.py
│   │   │   └── users.py
│   │   └── api.py
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   ├── crud/
│   │   ├── crud_todo.py
│   │   └── crud_user.py
│   ├── db/
│   │   ├── base.py
│   │   └── session.py
│   ├── models/
│   │   ├── todo.py
│   │   └── user.py
│   ├── schemas/
│   │   ├── todo.py
│   │   ├── token.py
│   │   └── user.py
│   ├── auth.py
│   ├── dependencies.py
│   └── main.py
├── tests/
│   ├── test_login.py
│   ├── test_todos.py
│   └── test_users.py
├── .gitignore
├── poetry.lock
├── poetry.toml
└── pyproject.toml
```

## Dependencies

*   [FastAPI](https.fastapi.tiangolo.com/): A modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
*   [Tortoise-ORM](https://tortoise.github.io/): An easy-to-use asyncio ORM (Object Relational Mapper) inspired by Django.
*   [Uvicorn](https://www.uvicorn.org/): A lightning-fast ASGI server implementation, using uvloop and httptools.
*   [Pydantic](https://pydantic-docs.helpmanual.io/): Data validation and settings management using python type annotations.
*   [Passlib](https://passlib.readthedocs.io/en/stable/): A password hashing library for Python.
*   [python-jose](https://python-jose.readthedocs.io/en/latest/): A JOSE implementation in Python.
*   [Poetry](https://python-poetry.org/): A tool for dependency management and packaging in Python.
