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
    resigned: bool = False


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
        created_at: Unix timestamp when the room was created (for GC).
        finished_at: Unix timestamp when the final game ended, or None (for GC).
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
    # Timestamps used by garbage collection to identify stale rooms.
    created_at: float = field(default_factory=time.time)
    finished_at: float | None = None


rooms: dict[str, Room] = {}


def _generate_id() -> str:
    """Generate a 6-character room code."""
    return secrets.token_hex(3).upper()


def create_room(
    host_name: str,
    time_limit: int = 300,
    difficulty: str | None = None,
    rounds: int = 1,
) -> Room:
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


# Catch-all maximum age for any room regardless of state.  Lobbies that were
# created but never started will be pruned after this many seconds.
_MAX_ROOM_AGE_SECONDS = 7200  # 2 hours


def get_expired_rooms(max_age_seconds: int = 3600) -> list[str]:
    """Return IDs of rooms that are eligible for garbage collection.

    A room is expired if either condition is true:
    - It is FINISHED and ``finished_at`` was recorded more than
      ``max_age_seconds`` ago.
    - Its ``created_at`` timestamp is older than ``_MAX_ROOM_AGE_SECONDS``
      (catch-all for abandoned lobbies or rooms stuck in any state).

    Rooms that are currently PLAYING are never returned, even if they are
    somehow very old, to avoid disrupting active games.

    Args:
        max_age_seconds: How many seconds a finished room is kept before it
            is considered expired. Defaults to 3600 (1 hour).

    Returns:
        List of room ID strings that should be removed.
    """
    now = time.time()
    expired: list[str] = []

    for room_id, room in rooms.items():
        # Never expire a room mid-game — players are actively using it.
        if room.state == RoomState.PLAYING:
            continue

        # Finished rooms: expire after max_age_seconds have passed since the
        # game ended.  finished_at may be None for rooms that transitioned to
        # FINISHED via old code paths; fall back to created_at in that case.
        if room.state == RoomState.FINISHED:
            end_ts = (
                room.finished_at if room.finished_at is not None else room.created_at
            )
            if now - end_ts >= max_age_seconds:
                expired.append(room_id)
            continue

        # Catch-all: lobby (or any unexpected state) rooms older than 2 hours.
        if now - room.created_at >= _MAX_ROOM_AGE_SECONDS:
            expired.append(room_id)

    return expired
