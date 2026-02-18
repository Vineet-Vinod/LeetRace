"""Room and player state management."""

from __future__ import annotations

import secrets
import time
from dataclasses import dataclass, field
from enum import Enum

from fastapi import WebSocket


class RoomState(str, Enum):
    """Lifecycle states for a game room."""
    LOBBY = "lobby"
    PLAYING = "playing"
    FINISHED = "finished"


@dataclass
class Player:
    """A player connected to a room.

    Attributes:
        name: Display name, unique within a room.
        websocket: Active WebSocket connection, or None if disconnected.
        submission: Most recent submission result dict.
        best_submission: Highest-scoring submission, used for rankings.
        locked_at: Seconds after round start when the player locked in,
                   or None if not yet locked.
    """
    name: str
    websocket: WebSocket | None = None
    submission: dict | None = None
    best_submission: dict | None = None
    locked_at: float | None = None


@dataclass
class Room:
    """A game room holding players and round state.

    Attributes:
        id: 6-character uppercase hex code (e.g. 'A1B2C3').
        host: Name of the player who created the room.
        state: Current lifecycle state.
        players: Map of player name to Player instance.
        problem: Current problem dict loaded from JSON, or None in lobby.
        start_time: Unix timestamp when the current round started.
        time_limit: Round duration in seconds.
        difficulty: Optional difficulty filter ('Easy', 'Medium', 'Hard').
        total_rounds: Number of rounds configured for this room.
        current_round: 1-indexed round currently in progress (0 = lobby).
    """
    id: str
    host: str
    state: RoomState = RoomState.LOBBY
    players: dict[str, Player] = field(default_factory=dict)
    problem: dict | None = None
    start_time: float | None = None
    time_limit: int = 300
    difficulty: str | None = None
    total_rounds: int = 1
    current_round: int = 0


rooms: dict[str, Room] = {}


def _generate_id() -> str:
    """Generate a 6-character room code."""
    return secrets.token_hex(3).upper()


def create_room(host_name: str, time_limit: int = 300, difficulty: str | None = None, rounds: int = 1) -> Room:
    """Create a new room with a unique ID and register it globally."""
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
    """Look up a room by ID. Returns None if not found."""
    return rooms.get(room_id)


def remove_room(room_id: str) -> None:
    """Remove a room from the registry. No-op if the room doesn't exist."""
    rooms.pop(room_id, None)
