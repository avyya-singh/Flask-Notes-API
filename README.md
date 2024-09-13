Here is a `README.md` file for your Flask Notes application:

---

# NotesApp

This is a simple **Flask-based Notes API** that allows users to create, read, update, and delete (table1) notes. It uses **PostgreSQL** as the database and provides RESTful API endpoints to interact with the notes data.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Database Setup](#database-setup)

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

## Installation

### Prerequisites

- Python 3.x installed.
- PostgreSQL installed and running locally.
- `pip` package manager for Python.
- A text editor or IDE (e.g., VSCode, PyCharm).

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

   - Create a PostgreSQL database named `postgres`.
   - Update the PostgreSQL credentials in `init_db.py` and `repository/NoteRepository.py` files to match your setup.

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
