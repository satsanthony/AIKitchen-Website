import os
import sqlite3
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from anthropic import Anthropic, AsyncAnthropic

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
DB_PATH = "mapdb.sqlite"

# Initialize DB
def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            prompt TEXT NOT NULL,
            response TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

app = FastAPI()

# Allow CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    prompt: str

@app.post("/chat")
async def chat_endpoint(req: ChatRequest):
    prompt = req.prompt.strip()
    if not prompt:
        return {"response": "Please enter a question."}

    # Call Claude 3.5 Sonnet
    client = Anthropic(api_key=ANTHROPIC_API_KEY)
    try:
        response = client.messages.create(
            model="claude-3-7-sonnet-latest",
            max_tokens=300,  # ~300 characters, but not exact; will trim below
            messages=[{"role": "user", "content": prompt}]
        )
        output = response.content[0].text.strip()
        output = output[:300]  # Ensure max 300 chars
    except Exception as e:
        output = f"Error: {e}"

    # Store in DB
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO chat_history (prompt, response) VALUES (?, ?)", (prompt, output))
    conn.commit()
    conn.close()

    return {"response": output}

@app.get("/history")
def get_history():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, prompt, response FROM chat_history ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()
    return {"history": [{"id": r[0], "prompt": r[1], "response": r[2]} for r in rows]} 