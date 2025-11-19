from fastapi import FastAPI  # , WebSocket
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
import os
from pydantic import BaseModel


def create_api_app() -> FastAPI:
    DB_PATH = "./data/app.db"
    os.makedirs("./data", exist_ok=True)

    # Init DB
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, text TEXT)"
    )
    conn.commit()
    conn.close()

    api_app = FastAPI()

    # Allow frontend requests
    api_app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:3000",
            "https://test.mgfhub.com",
            "http://frontend-svc:3000",
        ],  # React dev server
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Define a Pydantic model for the request body
    class Message(BaseModel):
        text: str

    @api_app.get("/api/messages")
    def get_messages():
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("SELECT * FROM messages")
        rows = cur.fetchall()
        conn.close()
        return rows

    @api_app.post("/api/messages")
    def add_message(message: Message):
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("INSERT INTO messages(text) VALUES (?)", (message.text,))
        conn.commit()
        conn.close()
        return {"status": "ok"}

    # @api_app.websocket("/_event")
    # async def websocket_endpoint(websocket: WebSocket):
    #     await websocket.accept()
    #     while True:
    #         data = await websocket.receive_text()
    #         await websocket.send_text(f"Message received: {data}")

    return api_app


app = create_api_app()
