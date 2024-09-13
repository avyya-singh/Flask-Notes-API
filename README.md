# Flask NotesApp

This is a simple **Flask-based Notes API** that allows users to create, read, update, and delete (CRUD) notes. It uses **PostgreSQL** as the database and provides RESTful API endpoints to interact with the notes data.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Database Setup](#database-setup)
- [Using Docker](#using-docker)
- [Testing the API with Postman](#testing-the-api-with-postman)
- [Using DataGrip](#using-datagrip)

## Features

- Create a new note with a name and description.
- Retrieve all notes or a specific note by ID.
- Update an existing note.
- Delete a note.

## Technologies Used

- **Python**: The main programming language used.
- **Flask**: Micro web framework to create the REST API.
- **PostgreSQL**: Relational database used to store the notes.
- **psycopg2**: PostgreSQL adapter for Python to connect and interact with the database.
- **Docker**: Used for containerizing the application and the database.
- **DataGrip**: SQL IDE for managing and visualizing the database.
- **Postman**: API testing tool to interact with the API endpoints.

## Installation

### Prerequisites

- Python 3.x installed.
- PostgreSQL installed and running locally or via Docker.
- `pip` package manager for Python.
- Docker (optional, for containerization).
- Postman (optional, for testing API).
- DataGrip (optional, for managing the database).

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/NotesApp.git
   cd NotesApp
   ```

2. Create a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up PostgreSQL:

   - **Option 1**: Install PostgreSQL locally and create a database named `postgres`.
   - **Option 2**: Use Docker to run PostgreSQL (instructions below).

5. Initialize the database:
   ```bash
   python init_db.py
   ```

## Running the Application

To start the Flask server:

```bash
python app.py
```

The application will run on `http://localhost:5000`.

## API Endpoints

### 1. **GET** `/api/v1/notes`

- Retrieves a list of all notes.
- **Response**:
  ```json
  {
    "notes": [
      { "id": 1, "name": "Note1", "description": "Description1" },
      { "id": 2, "name": "Note2", "description": "Description2" }
    ]
  }
  ```

### 2. **GET** `/api/v1/notes/<int:note_id>`

- Retrieves a specific note by ID.
- **Response**:
  ```json
  {
    "note": { "id": 1, "name": "Note1", "description": "Description1" }
  }
  ```

### 3. **POST** `/api/v1/notes`

- Creates a new note.
- **Request Body**:
  ```json
  {
    "name": "New Note",
    "description": "New description"
  }
  ```
- **Response**:
  ```json
  {
    "message": "Note created successfully",
    "note_id": 3
  }
  ```

### 4. **PUT** `/api/v1/notes/<int:note_id>`

- Updates an existing note by ID.
- **Request Body**:
  ```json
  {
    "name": "Updated Note",
    "description": "Updated description"
  }
  ```
- **Response**:
  ```json
  {
    "message": "Note updated successfully",
    "note_id": 1
  }
  ```

### 5. **DELETE** `/api/v1/notes/<int:note_id>`

- Deletes a specific note by ID.
- **Response**:
  ```json
  {
    "message": "Note deleted successfully"
  }
  ```

## Database Setup

1. The PostgreSQL table is automatically created if it doesn't already exist when running the app.
2. You can manually insert data into the `table1` using the `init_db.py` script.

The table schema for `table1` is:

```sql
CREATE TABLE IF NOT EXISTS table1 (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    description VARCHAR(1000)
);
```

## Using Docker

To simplify setting up the PostgreSQL database, you can use Docker to run PostgreSQL in a container.

1. Pull the PostgreSQL image from Docker Hub:

   ```bash
   docker pull postgres
   ```

2. Run the PostgreSQL container:

   ```bash
   docker run --name postgres-container -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres
   ```

3. You can now connect your Flask app to this PostgreSQL instance by updating the database credentials in `repository/NoteRepository.py` and `init_db.py` to:
   - Host: `localhost`
   - Port: `5432`
   - Database: `postgres`
   - Username: `postgres`
   - Password: `mysecretpassword`

## Testing the API with Postman

You can use **Postman** to test the API endpoints.

1. **Install Postman** if you don't have it: [Download Postman](https://www.postman.com/downloads/).
2. Create a new request and specify the API method (GET, POST, PUT, DELETE).
3. For POST/PUT requests, provide the required JSON body in the **Body** tab of Postman.
4. Test the API by sending requests to `http://localhost:5000/api/v1/notes`.

Examples:

- **GET all notes**: `GET http://localhost:5000/api/v1/notes`
- **Create a note**: `POST http://localhost:5000/api/v1/notes` with a body like:
  ```json
  {
    "name": "New Note",
    "description": "Note description"
  }
  ```

## Using DataGrip

You can manage and inspect your PostgreSQL database using **DataGrip**:

1. Open DataGrip and create a new PostgreSQL data source.
2. Provide the connection details (e.g., `localhost`, port `5432`, user `postgres`, password `mysecretpassword`).
3. Once connected, you can view and manage the `table1` table, execute queries, and inspect the data in your database.

## Project Structure

```
├── app.py               # Flask application entry point
├── init_db.py           # Initializes the PostgreSQL database
├── models
│   └── Note.py          # Note model
├── repository
│   └── NoteRepository.py # Repository layer for database interactions
├── routes
│   └── NoteRoutes.py    # Flask routes for handling HTTP requests
├── servicess
│   └── Service.py       # Business logic for handling notes
├── requirements.txt     # Dependencies
```
