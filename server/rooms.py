"""Room and player state management."""

from __future__ import annotations

import secrets
import time
from dataclasses import dataclass, field
from enum import Enum

from fastapi import WebSocket


class RoomState(str, Enum):
    LOBBY = "lobby"
    PLAYING = "playing"
    FINISHED = "finished"


@dataclass
class Player:
    name: str
    websocket: WebSocket | None = None
    submission: dict | None = None  # latest: {code, passed, total, error, time_ms, char_count, solved, submit_time}
    best_submission: dict | None = None  # best so far (used for scoring)
    locked_at: float | None = None  # timestamp when player locked in


@dataclass
class Room:
    id: str
    host: str  # player name
    state: RoomState = RoomState.LOBBY
    players: dict[str, Player] = field(default_factory=dict)
    problem: dict | None = None
    start_time: float | None = None
    time_limit: int = 300  # seconds
    difficulty: str | None = None
    total_rounds: int = 1
    current_round: int = 0


rooms: dict[str, Room] = {}


def _generate_id() -> str:
    """Generate a 6-character room code."""
    return secrets.token_hex(3).upper()


def create_room(host_name: str, time_limit: int = 300, difficulty: str | None = None, rounds: int = 1) -> Room:
    room_id = _generate_id()
    while room_id in rooms:
        room_id = _generate_id()

    room = Room(
        id=room_id,
        host=host_name,
        time_limit=time_limit,
        difficulty=difficulty,
        total_rounds=rounds,
    )
    rooms[room_id] = room
    return room


def get_room(room_id: str) -> Room | None:
    return rooms.get(room_id)


def remove_room(room_id: str) -> None:
    rooms.pop(room_id, None)
