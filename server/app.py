"""FastAPI application: REST routes, WebSocket mount, static files."""

from pathlib import Path

from fastapi import FastAPI, WebSocket
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

from server.rooms import create_room, get_room, RoomState
from server.problems import load_index
from server.ws import websocket_handler

STATIC_DIR = Path(__file__).resolve().parent.parent / "static"

app = FastAPI(title="LeetRace")


# --- REST API ---

@app.post("/api/rooms")
async def api_create_room(body: dict | None = None):
    body = body or {}
    host = body.get("host", "Host")
    time_limit = body.get("time_limit", 300)
    difficulty = body.get("difficulty")

    time_limit = max(60, min(600, int(time_limit)))

    room = create_room(host_name=host, time_limit=time_limit, difficulty=difficulty)
    return {"room_id": room.id, "host": room.host}


@app.get("/api/rooms/{room_id}")
async def api_get_room(room_id: str):
    room = get_room(room_id)
    if not room:
        return JSONResponse({"error": "Room not found"}, status_code=404)
    return {
        "room_id": room.id,
        "state": room.state.value,
        "host": room.host,
        "players": list(room.players.keys()),
        "time_limit": room.time_limit,
        "difficulty": room.difficulty,
    }


@app.get("/api/problems")
async def api_list_problems():
    return load_index()


# --- WebSocket ---

@app.websocket("/ws/{room_id}")
async def ws_endpoint(ws: WebSocket, room_id: str):
    await websocket_handler(ws, room_id)


# --- HTML pages ---

@app.get("/")
async def index():
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/room")
async def room_page():
    return FileResponse(STATIC_DIR / "room.html")


# --- Static files (CSS, JS) ---

app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")
