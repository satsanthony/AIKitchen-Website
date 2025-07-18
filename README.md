# Webpage-SQL Chat Assistant

A simple web-based chat assistant that stores and displays chat history using a SQLite database. The backend is powered by Python and interacts with the Anthropic API. The frontend is built with HTML, CSS, and JavaScript.

---

## Features

- Chat with an AI assistant (Anthropic API).
- Stores chat history in a local SQLite database (`mapdb.sqlite`).
- View chat history in a formatted table on the support page.

---

## Project Structure

| File/Folder      | Description                                      |
|------------------|--------------------------------------------------|
| `main.py`        | Main backend server (FastAPI)                    |
| `pyclass_db.py`  | Database helper classes/functions                |
| `pyclass_def.py` | Additional Python class definitions              |
| `mapdb.sqlite`   | SQLite database storing chat history             |
| `index.html`     | Main chat interface                              |
| `support.html`   | Support page to view chat history                |
| `main.js`        | JavaScript for main chat interface               |
| `support.js`     | JavaScript for support page                      |
| `styles.css`     | Shared CSS styles                                |
| `README.md`      | Project documentation                            |
| `pyproject.toml` | Python project configuration                     |
| `poetry.lock`    | Poetry lock file for dependencies                |

---

## API Key Setup

**Important:**  
Store your Anthropic API key in a `.env` file in the project root:

```
ANTHROPIC_API_KEY=your_api_key_here
```

---

## Python Dependencies

| Package      | Purpose                        |
|--------------|--------------------------------|
| fastapi      | Web framework for backend API  |
| uvicorn      | ASGI server for FastAPI        |
| python-dotenv| Load environment variables     |
| anthropic    | Anthropic API client           |
| sqlite3      | Built-in, for database         |

> **Note:**  
> Install dependencies using [Poetry](https://python-poetry.org/) or `pip` as needed.

---

## Installation & Execution

### 1. Clone the repository

```sh
git clone https://github.com/yourusername/webpage-sql.git
cd webpage-sql
```

### 2. Install Python dependencies

If using Poetry:
```sh
poetry install
```
Or using pip:
```sh
pip install fastapi uvicorn python-dotenv anthropic
```

### 3. Set up your `.env` file

Rename '.env.example to .env' file in the project root and add your Anthropic API key:
```
ANTHROPIC_API_KEY=your_api_key_here
```

### 4. Run the backend server

```sh
uvicorn main:app --reload
```
- The server will start at `http://localhost:8000`.

### 5. Open the frontend

- Open `index.html` in your browser to chat with the assistant.
- Open `support.html` to view chat history.

---

## Usage

- Enter your message in the chat box and submit.
- Click "Display Chat History" on the support page to view all previous chats in a table.

---

## License

MIT License

---


