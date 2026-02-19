"""FastAPI application: REST routes, WebSocket mount, static files."""

import asyncio
import logging
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Literal

from fastapi import FastAPI, WebSocket
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, field_validator

from server.rooms import create_room, get_room, get_expired_rooms, remove_room, rooms
from server.problems import load_index
from server.ws import websocket_handler

STATIC_DIR = Path(__file__).resolve().parent.parent / "static"

logger = logging.getLogger(__name__)

# How often the GC loop wakes up to check for expired rooms (seconds).
_GC_INTERVAL_SECONDS = 60

# Finished rooms are kept for 1 hour after the game ends before being pruned.
_FINISHED_ROOM_MAX_AGE_SECONDS = 3600


async def _gc_loop() -> None:
    """Background task: periodically remove expired/abandoned rooms.

    Runs every ``_GC_INTERVAL_SECONDS`` seconds.  Errors are caught and logged
    so a transient bug cannot permanently stop the GC loop.

    Safety note: ``get_expired_rooms`` iterates the ``rooms`` dict and returns a
    list of IDs.  ``remove_room`` then mutates the dict.  This is safe because
    there is no ``await`` between the two calls, so no other coroutine can modify
    the dict concurrently within the same event-loop tick.
    """
    while True:
        await asyncio.sleep(_GC_INTERVAL_SECONDS)
        try:
            expired = get_expired_rooms(max_age_seconds=_FINISHED_ROOM_MAX_AGE_SECONDS)
            for room_id in expired:
                remove_room(room_id)
                logger.info("GC: removed expired room %s", room_id)
            if expired:
                logger.info(
                    "GC: pruned %d room(s); %d remaining", len(expired), len(rooms)
                )
        except Exception:
            logger.exception(
                "GC: unexpected error during room cleanup — will retry next cycle"
            )


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Start background tasks on startup and clean them up on shutdown."""
    gc_task = asyncio.create_task(_gc_loop())
    logger.info(
        "GC: room garbage-collection loop started (interval=%ds)", _GC_INTERVAL_SECONDS
    )
    try:
        yield
    finally:
        gc_task.cancel()
        try:
            await gc_task
        except asyncio.CancelledError:
            pass
        logger.info("GC: room garbage-collection loop stopped")


app = FastAPI(title="LeetRace", lifespan=lifespan)


class CreateRoomRequest(BaseModel):
    host: str = "Host"
    time_limit: int = 300
    difficulty: Literal["Easy", "Medium", "Hard"] | None = None
    rounds: int = 1

    @field_validator("time_limit")
    @classmethod
    def clamp_time_limit(cls, v: int) -> int:
        return max(30, min(3600, v))

    @field_validator("rounds")
    @classmethod
    def clamp_rounds(cls, v: int) -> int:
        return max(1, min(10, v))


# --- REST API ---


@app.post("/api/rooms")
async def api_create_room(body: CreateRoomRequest = CreateRoomRequest()):
    room = create_room(
        host_name=body.host,
        time_limit=body.time_limit,
        difficulty=body.difficulty,
        rounds=body.rounds,
    )
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
