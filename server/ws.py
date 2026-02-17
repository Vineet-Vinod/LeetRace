"""WebSocket handler for game rooms."""

from __future__ import annotations

import asyncio
import logging
import re
import time

from fastapi import WebSocket, WebSocketDisconnect

from server.rooms import Player, Room, RoomState, get_room, remove_room
from server.problems import pick_random
from server.sandbox import run_code
from server.scoring import rank_players

logger = logging.getLogger(__name__)

# Superscript digit mapping
_SUP_DIGITS = str.maketrans("0123456789", "\u2070\u00b9\u00b2\u00b3\u2074\u2075\u2076\u2077\u2078\u2079")


def fix_exponents(text: str) -> str:
    """Fix exponent display in problem descriptions.

    Handles two forms:
    - Explicit caret: '10^5' → '10⁵'
    - Collapsed (from HTML scraping): '105' → '10⁵' after <= or >= in constraints
    """
    # Explicit carets: 10^5 → 10⁵, 2^31 → 2³¹
    text = re.sub(
        r"(\d+)\^(\d+)",
        lambda m: m.group(1) + m.group(2).translate(_SUP_DIGITS),
        text,
    )
    # Collapsed base-10 exponents in constraints: <= 105 → <= 10⁵
    # Only 10[4-9] — lower digits (100, 101..103) are likely real numbers
    # Match after <= / >= (right bound) or before <= / >= (left bound)
    text = re.sub(
        r"(?<=[<>=] )(-?)10([4-9])\b",
        lambda m: m.group(1) + "10" + m.group(2).translate(_SUP_DIGITS),
        text,
    )
    text = re.sub(
        r"\b(-?)10([4-9])(?= [<>=])",
        lambda m: m.group(1) + "10" + m.group(2).translate(_SUP_DIGITS),
        text,
    )
    # Collapsed 2^31 / 2^32: <= 231 → <= 2³¹
    text = re.sub(
        r"(?<=[<>=] )(-?)2(3[12])\b",
        lambda m: m.group(1) + "2" + m.group(2).translate(_SUP_DIGITS),
        text,
    )
    text = re.sub(
        r"\b(-?)2(3[12])(?= [<>=])",
        lambda m: m.group(1) + "2" + m.group(2).translate(_SUP_DIGITS),
        text,
    )
    return text


async def broadcast(room: Room, message: dict) -> None:
    """Send a JSON message to all connected players in a room."""
    disconnected = []
    for name, player in room.players.items():
        if player.websocket:
            try:
                await player.websocket.send_json(message)
            except Exception:
                disconnected.append(name)
    for name in disconnected:
        room.players.pop(name, None)


def room_state_msg(room: Room) -> dict:
    """Build a room_state message."""
    return {
        "type": "room_state",
        "room_id": room.id,
        "state": room.state.value,
        "host": room.host,
        "players": list(room.players.keys()),
        "time_limit": room.time_limit,
        "difficulty": room.difficulty,
        "current_round": room.current_round,
        "total_rounds": room.total_rounds,
    }


def scoreboard_msg(room: Room) -> dict:
    """Build a scoreboard message."""
    return {
        "type": "scoreboard",
        "rankings": rank_players(room.players),
    }


async def send_error(ws: WebSocket, msg: str) -> None:
    await ws.send_json({"type": "error", "message": msg})


async def timer_task(room: Room) -> None:
    """Background task that ticks every 5s and ends the game when time runs out."""
    start = room.start_time
    limit = room.time_limit

    while room.state == RoomState.PLAYING:
        elapsed = time.time() - start
        remaining = max(0, limit - elapsed)

        await broadcast(room, {
            "type": "tick",
            "remaining": int(remaining),
            "elapsed": int(elapsed),
        })

        if remaining <= 0:
            await end_game(room)
            return

        await asyncio.sleep(5)


async def end_game(room: Room) -> None:
    """End the current round and either start a break or finish the game."""
    if room.state == RoomState.FINISHED:
        return

    rankings = rank_players(room.players)

    if room.current_round < room.total_rounds:
        # More rounds to play — show round results with a break
        room.state = RoomState.FINISHED  # temporarily, will change to PLAYING on next round
        await broadcast(room, {
            "type": "round_over",
            "rankings": rankings,
            "current_round": room.current_round,
            "total_rounds": room.total_rounds,
            "break_seconds": 30,
        })
        asyncio.create_task(break_task(room))
    else:
        # Final round — game is over
        room.state = RoomState.FINISHED
        await broadcast(room, {
            "type": "game_over",
            "rankings": rankings,
        })


async def break_task(room: Room) -> None:
    """30-second break between rounds, then auto-start next round."""
    for remaining in range(29, -1, -1):
        await asyncio.sleep(1)
        if room.state != RoomState.FINISHED:
            return  # room was manually restarted or cleaned up
        await broadcast(room, {
            "type": "break_tick",
            "remaining": remaining,
        })

    await start_next_round(room)


async def start_next_round(room: Room) -> None:
    """Pick a new problem and start the next round."""
    problem = pick_random(room.difficulty)
    if not problem:
        await broadcast(room, {"type": "error", "message": "No problems available."})
        return

    # Reset player state for new round
    for player in room.players.values():
        player.submission = None
        player.best_submission = None
        player.locked_at = None

    room.problem = problem
    room.state = RoomState.PLAYING
    room.start_time = time.time()
    room.current_round += 1

    await broadcast(room, {
        "type": "game_start",
        "problem": {
            "id": problem["id"],
            "title": problem["title"],
            "difficulty": problem["difficulty"],
            "description": fix_exponents(problem["description"]),
            "entry_point": problem["entry_point"],
            "starter_code": problem["starter_code"],
        },
        "time_limit": room.time_limit,
        "current_round": room.current_round,
        "total_rounds": room.total_rounds,
    })

    asyncio.create_task(timer_task(room))


async def handle_lock(ws: WebSocket, room: Room, player_name: str) -> None:
    """Handle a player locking in their submission."""
    if room.state != RoomState.PLAYING:
        return

    player = room.players.get(player_name)
    if not player:
        return
    if player.locked_at is not None:
        await send_error(ws, "Already locked in")
        return
    if player.best_submission is None or not player.best_submission.get("solved"):
        await send_error(ws, "Solve the problem before locking in")
        return

    player.locked_at = time.time() - room.start_time

    if player.websocket:
        await player.websocket.send_json({"type": "locked"})

    await broadcast(room, scoreboard_msg(room))

    # If all players are locked in, end the round early
    if all(p.locked_at is not None for p in room.players.values()):
        await end_game(room)


async def handle_join(ws: WebSocket, room: Room, data: dict) -> str | None:
    """Handle a player joining a room. Returns player name or None."""
    name = data.get("name", "").strip()
    if not name:
        await send_error(ws, "Name is required")
        return None
    if len(name) > 20:
        await send_error(ws, "Name too long (max 20 chars)")
        return None
    if name in room.players:
        await send_error(ws, f"Name '{name}' is already taken")
        return None
    if room.state != RoomState.LOBBY:
        await send_error(ws, "Game already in progress")
        return None

    room.players[name] = Player(name=name, websocket=ws)
    await broadcast(room, room_state_msg(room))
    return name


async def handle_start(ws: WebSocket, room: Room, player_name: str) -> None:
    """Handle the host starting the game."""
    if player_name != room.host:
        await send_error(ws, "Only the host can start the game")
        return
    if room.state != RoomState.LOBBY:
        await send_error(ws, "Game has already started")
        return
    if len(room.players) < 2:
        await send_error(ws, "Need at least 2 players to start")
        return

    problem = pick_random(room.difficulty)
    if not problem:
        await broadcast(room, {"type": "error", "message": "No problems available. Run build_problems.py first."})
        return

    room.problem = problem
    room.state = RoomState.PLAYING
    room.start_time = time.time()
    room.current_round = 1

    # Send problem to players (without test cases)
    await broadcast(room, {
        "type": "game_start",
        "problem": {
            "id": problem["id"],
            "title": problem["title"],
            "difficulty": problem["difficulty"],
            "description": fix_exponents(problem["description"]),
            "entry_point": problem["entry_point"],
            "starter_code": problem["starter_code"],
        },
        "time_limit": room.time_limit,
        "current_round": room.current_round,
        "total_rounds": room.total_rounds,
    })

    # Start the timer
    asyncio.create_task(timer_task(room))


def _is_better(new: dict, old: dict) -> bool:
    """Return True if the new submission is better than the old one for scoring."""
    if new["solved"] and not old["solved"]:
        return True
    if not new["solved"] and old["solved"]:
        return False
    if new["solved"] and old["solved"]:
        return new["char_count"] < old["char_count"]
    # Both unsolved: more tests passed is better
    return new["passed"] > old["passed"]


async def handle_submit(room: Room, player_name: str, data: dict) -> None:
    """Handle a code submission."""
    if room.state != RoomState.PLAYING:
        return

    player = room.players.get(player_name)
    if not player:
        return
    if player.locked_at is not None:
        if player.websocket:
            await send_error(player.websocket, "You are locked in")
        return

    code = data.get("code", "")
    if not code.strip():
        if player.websocket:
            await send_error(player.websocket, "Empty submission")
        return

    char_count = len(code)
    submit_time = time.time() - room.start_time

    # Run in sandbox
    any_order = "any order" in room.problem.get("description", "").lower()
    result = await run_code(
        code=code,
        entry_point=room.problem["entry_point"],
        test_cases=room.problem["test_cases"],
        preamble=room.problem.get("preamble", ""),
        any_order=any_order,
    )

    solved = result["passed"] == result["total"] and result["total"] > 0

    submission = {
        "code": code,
        "passed": result["passed"],
        "total": result["total"],
        "error": result.get("error"),
        "time_ms": result.get("time_ms", 0),
        "char_count": char_count,
        "solved": solved,
        "submit_time": round(submit_time, 2),
    }

    # Always store latest result
    player.submission = submission

    # Update best submission if this one is better
    best = player.best_submission
    if best is None or _is_better(submission, best):
        player.best_submission = submission

    # Notify the submitter of their result
    if player.websocket:
        await player.websocket.send_json({
            "type": "submit_result",
            "passed": result["passed"],
            "total": result["total"],
            "error": result.get("error"),
            "solved": solved,
            "char_count": char_count,
            "submit_time": round(submit_time, 2),
            "stdout": result.get("stdout", ""),
            "stderr": result.get("stderr", ""),
        })

    # Broadcast updated scoreboard
    await broadcast(room, scoreboard_msg(room))


async def handle_restart(ws: WebSocket, room: Room, player_name: str) -> None:
    """Handle the host restarting the game with a new problem."""
    if player_name != room.host:
        await send_error(ws, "Only the host can restart the game")
        return
    if room.state != RoomState.FINISHED:
        await send_error(ws, "Game is not finished yet")
        return

    # Reset room state
    room.state = RoomState.LOBBY
    room.problem = None
    room.start_time = None
    room.current_round = 0
    for player in room.players.values():
        player.submission = None
        player.best_submission = None
        player.locked_at = None

    await broadcast(room, room_state_msg(room))


async def websocket_handler(ws: WebSocket, room_id: str) -> None:
    """Main WebSocket handler for a room."""
    await ws.accept()

    room = get_room(room_id)
    if not room:
        await send_error(ws, "Room not found")
        await ws.close()
        return

    player_name = None

    try:
        while True:
            data = await ws.receive_json()
            msg_type = data.get("type")

            if msg_type == "join":
                player_name = await handle_join(ws, room, data)

            elif msg_type == "start" and player_name:
                await handle_start(ws, room, player_name)

            elif msg_type == "submit" and player_name:
                await handle_submit(room, player_name, data)

            elif msg_type == "lock" and player_name:
                await handle_lock(ws, room, player_name)

            elif msg_type == "restart" and player_name:
                await handle_restart(ws, room, player_name)

    except WebSocketDisconnect:
        pass
    except Exception:
        logger.exception("WebSocket error in room %s for player %s", room_id, player_name)
        try:
            await send_error(ws, "Something went wrong. Please rejoin.")
        except Exception:
            pass
    finally:
        # Clean up player
        if player_name and player_name in room.players:
            room.players.pop(player_name)

            # If host left, assign new host
            if room.host == player_name and room.players:
                room.host = next(iter(room.players))

            # If room empty, remove it
            if not room.players:
                remove_room(room_id)
            else:
                await broadcast(room, room_state_msg(room))
