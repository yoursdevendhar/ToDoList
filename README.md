# 📝 ToDoList API — FastAPI + MySQL

A simple **REST API** for managing a To-Do list, built with **FastAPI** and **MySQL** using **SQLAlchemy** as the ORM.

---

## 🗂️ Project Structure

```
project/
│
├── main.py          # API routes (Create, Read, Update, Delete)
├── models.py        # Database table definition
├── schemas.py       # Request/Response data shapes (Pydantic)
├── database.py      # Database connection setup
└── index.html       # Frontend UI (plain HTML/JS)
```

---

## ⚙️ How It Works

```
Client (Browser / Postman)
        │
        ▼
   FastAPI App  (main.py)
        │
        ├── schemas.py  →  Validates incoming JSON data
        │
        ├── models.py   →  Maps Python objects to DB tables
        │
        └── database.py →  Connects to MySQL
```

---

## 🗄️ Database Configuration

**File:** `database.py`

- Connects to a **MySQL** database named `todolistdb`
- Default credentials: `root` / `system` on `localhost:3306`
- Uses **SQLAlchemy** to communicate with the database

> ⚠️ Change the `DATABASE_URL` in `database.py` if your MySQL username, password, or database name is different.

```python
DATABASE_URL = "mysql+pymysql://root:system@localhost:3306/todolistdb"
```

---

## 🧱 Database Model

**File:** `models.py`

Table name: `todolist`

| Column       | Type      | Description                     |
|--------------|-----------|---------------------------------|
| `id`         | Integer   | Primary key, auto-incremented   |
| `title`      | String    | Name/title of the task          |
| `status`     | String    | Task status (e.g. pending/done) |
| `created_at` | DateTime  | Timestamp when task was created |

---

## 📐 Data Schemas

**File:** `schemas.py`

- **`ToDoListCreate`** — shape of data expected when creating or updating a task
- **`ToDoListResponse`** — shape of data returned by the API (includes `id`)

---

## 🚀 API Endpoints

Base URL: `http://localhost:8000`

| Method   | Endpoint      | Description             |
|----------|---------------|-------------------------|
| `POST`   | `/list`       | Create a new task       |
| `GET`    | `/list`       | Get all tasks           |
| `PUT`    | `/list/{id}`  | Update a task by ID     |
| `DELETE` | `/list/{id}`  | Delete a task by ID     |

### Example Request — Create a Task

```http
POST /list
Content-Type: application/json

{
  "title": "Buy groceries",
  "status": "pending",
  "created_at": "2024-01-01T10:00:00"
}
```

### Example Response

```json
{
  "id": 1,
  "title": "Buy groceries",
  "status": "pending",
  "created_at": "2024-01-01T10:00:00"
}
```

---

## 🛠️ Setup & Installation

### 1. Prerequisites

- Python 3.8+
- MySQL Server running locally
- pip

### 2. Install Dependencies

```bash
pip install fastapi uvicorn sqlalchemy pymysql pydantic
```

### 3. Setup MySQL Database

Log in to MySQL and create the database:

```sql
CREATE DATABASE todolistdb;
```

> The tables will be created **automatically** when you run the app.

### 4. Run the App

```bash
uvicorn main:app --reload
```

The API will be available at: **http://localhost:8000**

### 5. Open the Frontend

Open `index.html` in your browser to use the UI.

---

## 📖 Interactive API Docs

FastAPI generates automatic documentation:

| Tool     | URL                                      |
|----------|------------------------------------------|
| Swagger  | http://localhost:8000/docs               |
| ReDoc    | http://localhost:8000/redoc              |

---

## 🔒 CORS

The app is configured to allow requests from **all origins** (`*`). This is fine for local development. Before deploying to production, restrict it to your frontend's domain:

```python
allow_origins=["https://your-frontend-domain.com"]
```

---

## 📦 Dependencies Summary

| Package      | Purpose                              |
|--------------|--------------------------------------|
| `fastapi`    | Web framework for building the API   |
| `uvicorn`    | ASGI server to run the app           |
| `sqlalchemy` | ORM for database interaction         |
| `pymysql`    | MySQL database driver                |
| `pydantic`   | Data validation via schemas          |

---

