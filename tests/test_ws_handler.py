"""
WebSocket handler tests for server/ws.py.

Two layers of tests:
1. TestClient WebSocket tests — full integration through the FastAPI app.
2. Direct async unit tests of handle_join, handle_submit, handle_lock,
   handle_restart, and end_game using mocked WebSocket objects.

These avoid any dependency on real problems by injecting a FAKE_PROBLEM
or mocking pick_random.
"""

import time
import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from fastapi.testclient import TestClient

from server.app import app
from server.rooms import Room, Player, RoomState, create_room
import server.rooms as rooms_module
import server.ws as ws_module


# ---------------------------------------------------------------------------
# Shared fake problem — matches the sandbox runner's requirements
# ---------------------------------------------------------------------------

FAKE_PROBLEM = {
    "id": "two-sum",
    "title": "Two Sum",
    "difficulty": "Easy",
    "description": "Given nums and target, return indices that add to target.",
    "entry_point": "Solution().twoSum",
    "starter_code": "class Solution:\n    def twoSum(self, nums, target): pass",
    "preamble": "from typing import *",
    "test_cases": [
        "assert candidate(nums=[2,7,11,15], target=9) == [0, 1]",
        "assert candidate(nums=[3,2,4], target=6) == [1, 2]",
    ],
    "any_order": False,
}

CORRECT_TWO_SUM = """
class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, n in enumerate(nums):
            if target - n in seen:
                return [seen[target - n], i]
            seen[n] = i
        return None
"""


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


# ===========================================================================
# WebSocket integration tests (TestClient)
# ===========================================================================

class TestWebSocketJoin:
    def test_nonexistent_room_receives_error_message(self, client):
        with client.websocket_connect("/ws/ZZZZZZ") as ws:
            msg = ws.receive_json()
            assert msg["type"] == "error"
            assert "not found" in msg["message"].lower()

    def test_valid_join_receives_room_state(self, client):
        room = create_room(host_name="Alice")
        with client.websocket_connect(f"/ws/{room.id}") as ws:
            ws.send_json({"type": "join", "name": "Alice"})
            msg = ws.receive_json()
            assert msg["type"] == "room_state"
            assert "Alice" in msg["players"]

    def test_join_adds_player_to_room(self, client):
        room = create_room(host_name="Alice")
        with client.websocket_connect(f"/ws/{room.id}") as ws:
            ws.send_json({"type": "join", "name": "Alice"})
            ws.receive_json()
            # Check while the connection is still open (disconnect cleans up players)
            assert "Alice" in room.players

    def test_empty_name_receives_error(self, client):
        room = create_room(host_name="Alice")
        with client.websocket_connect(f"/ws/{room.id}") as ws:
            ws.send_json({"type": "join", "name": ""})
            msg = ws.receive_json()
            assert msg["type"] == "error"
            assert "required" in msg["message"].lower()

    def test_name_too_long_receives_error(self, client):
        room = create_room(host_name="Alice")
        with client.websocket_connect(f"/ws/{room.id}") as ws:
            ws.send_json({"type": "join", "name": "A" * 21})
            msg = ws.receive_json()
            assert msg["type"] == "error"
            assert "long" in msg["message"].lower()

    def test_name_exactly_20_chars_is_accepted(self, client):
        room = create_room(host_name="Alice")
        with client.websocket_connect(f"/ws/{room.id}") as ws:
            ws.send_json({"type": "join", "name": "A" * 20})
            msg = ws.receive_json()
            assert msg["type"] == "room_state"

    def test_duplicate_name_receives_taken_error(self, client):
        room = create_room(host_name="Alice")
        room.players["Alice"] = Player(name="Alice")
        with client.websocket_connect(f"/ws/{room.id}") as ws:
            ws.send_json({"type": "join", "name": "Alice"})
            msg = ws.receive_json()
            assert msg["type"] == "error"
            assert "taken" in msg["message"].lower()

    def test_join_playing_room_receives_error(self, client):
        room = create_room(host_name="Alice")
        room.state = RoomState.PLAYING
        with client.websocket_connect(f"/ws/{room.id}") as ws:
            ws.send_json({"type": "join", "name": "Bob"})
            msg = ws.receive_json()
            assert msg["type"] == "error"
            assert "progress" in msg["message"].lower()


class TestWebSocketStart:
    def test_non_host_cannot_start(self, client):
        room = create_room(host_name="Alice")
        room.players["Bob"] = Player(name="Bob")
        room.players["Carol"] = Player(name="Carol")
        with client.websocket_connect(f"/ws/{room.id}") as ws:
            ws.send_json({"type": "join", "name": "Dave"})
            ws.receive_json()  # room_state
            ws.send_json({"type": "start"})
            msg = ws.receive_json()
            assert msg["type"] == "error"
            assert "host" in msg["message"].lower()

    def test_start_with_only_one_player_receives_error(self, client):
        room = create_room(host_name="Alice")
        with client.websocket_connect(f"/ws/{room.id}") as ws:
            ws.send_json({"type": "join", "name": "Alice"})
            ws.receive_json()  # room_state
            ws.send_json({"type": "start"})
            msg = ws.receive_json()
            assert msg["type"] == "error"
            assert any(kw in msg["message"].lower() for kw in ["2 player", "least 2", "at least"])

    def test_host_can_start_with_two_players(self, client):
        room = create_room(host_name="Alice")
        room.players["Bob"] = Player(name="Bob")

        with patch.object(ws_module, "pick_random", return_value=FAKE_PROBLEM):
            with client.websocket_connect(f"/ws/{room.id}") as ws:
                ws.send_json({"type": "join", "name": "Alice"})
                ws.receive_json()  # room_state
                ws.send_json({"type": "start"})
                msg = ws.receive_json()
                assert msg["type"] == "game_start"
                assert msg["problem"]["id"] == "two-sum"

    def test_start_changes_room_state_to_playing(self, client):
        room = create_room(host_name="Alice")
        room.players["Bob"] = Player(name="Bob")

        with patch.object(ws_module, "pick_random", return_value=FAKE_PROBLEM):
            with client.websocket_connect(f"/ws/{room.id}") as ws:
                ws.send_json({"type": "join", "name": "Alice"})
                ws.receive_json()
                ws.send_json({"type": "start"})
                ws.receive_json()  # game_start

        assert room.state == RoomState.PLAYING

    def test_start_sends_problem_info_in_game_start(self, client):
        room = create_room(host_name="Alice")
        room.players["Bob"] = Player(name="Bob")

        with patch.object(ws_module, "pick_random", return_value=FAKE_PROBLEM):
            with client.websocket_connect(f"/ws/{room.id}") as ws:
                ws.send_json({"type": "join", "name": "Alice"})
                ws.receive_json()
                ws.send_json({"type": "start"})
                msg = ws.receive_json()

        problem = msg["problem"]
        assert "id" in problem
        assert "title" in problem
        assert "description" in problem
        assert "entry_point" in problem
        assert "starter_code" in problem
        # Test cases must NOT be sent to the client
        assert "test_cases" not in problem

    def test_no_problems_available_sends_error(self, client):
        room = create_room(host_name="Alice")
        room.players["Bob"] = Player(name="Bob")

        with patch.object(ws_module, "pick_random", return_value=None):
            with client.websocket_connect(f"/ws/{room.id}") as ws:
                ws.send_json({"type": "join", "name": "Alice"})
                ws.receive_json()
                ws.send_json({"type": "start"})
                msg = ws.receive_json()
                assert msg["type"] == "error"

    def test_game_start_message_includes_time_limit(self, client):
        room = create_room(host_name="Alice", time_limit=120)
        room.players["Bob"] = Player(name="Bob")

        with patch.object(ws_module, "pick_random", return_value=FAKE_PROBLEM):
            with client.websocket_connect(f"/ws/{room.id}") as ws:
                ws.send_json({"type": "join", "name": "Alice"})
                ws.receive_json()
                ws.send_json({"type": "start"})
                msg = ws.receive_json()
                assert msg["time_limit"] == 120

    def test_game_start_sets_current_round_to_1(self, client):
        room = create_room(host_name="Alice")
        room.players["Bob"] = Player(name="Bob")

        with patch.object(ws_module, "pick_random", return_value=FAKE_PROBLEM):
            with client.websocket_connect(f"/ws/{room.id}") as ws:
                ws.send_json({"type": "join", "name": "Alice"})
                ws.receive_json()
                ws.send_json({"type": "start"})
                ws.receive_json()

        assert room.current_round == 1


# ===========================================================================
# Direct async unit tests — handle_join
# ===========================================================================

class TestHandleJoinDirect:
    @pytest.mark.asyncio
    async def test_successful_join_adds_player(self):
        room = create_room(host_name="Alice")
        mock_ws = AsyncMock()
        with patch.object(ws_module, "broadcast", new_callable=AsyncMock):
            name = await ws_module.handle_join(mock_ws, room, {"name": "Alice"})
        assert name == "Alice"
        assert "Alice" in room.players

    @pytest.mark.asyncio
    async def test_join_assigns_websocket_to_player(self):
        room = create_room(host_name="Alice")
        mock_ws = AsyncMock()
        with patch.object(ws_module, "broadcast", new_callable=AsyncMock):
            await ws_module.handle_join(mock_ws, room, {"name": "Alice"})
        assert room.players["Alice"].websocket is mock_ws

    @pytest.mark.asyncio
    async def test_join_strips_whitespace(self):
        room = create_room(host_name="Alice")
        mock_ws = AsyncMock()
        with patch.object(ws_module, "broadcast", new_callable=AsyncMock):
            name = await ws_module.handle_join(mock_ws, room, {"name": "  Alice  "})
        assert name == "Alice"
        assert "Alice" in room.players

    @pytest.mark.asyncio
    async def test_join_empty_after_strip_returns_none(self):
        room = create_room(host_name="Alice")
        mock_ws = AsyncMock()
        name = await ws_module.handle_join(mock_ws, room, {"name": "   "})
        assert name is None
        assert room.players == {}

    @pytest.mark.asyncio
    async def test_join_name_too_long_returns_none(self):
        room = create_room(host_name="Alice")
        mock_ws = AsyncMock()
        name = await ws_module.handle_join(mock_ws, room, {"name": "X" * 21})
        assert name is None

    @pytest.mark.asyncio
    async def test_join_duplicate_name_returns_none(self):
        room = create_room(host_name="Alice")
        room.players["Alice"] = Player(name="Alice")
        mock_ws = AsyncMock()
        name = await ws_module.handle_join(mock_ws, room, {"name": "Alice"})
        assert name is None

    @pytest.mark.asyncio
    async def test_join_non_lobby_room_returns_none(self):
        room = create_room(host_name="Alice")
        room.state = RoomState.PLAYING
        mock_ws = AsyncMock()
        name = await ws_module.handle_join(mock_ws, room, {"name": "Bob"})
        assert name is None

    @pytest.mark.asyncio
    async def test_join_broadcasts_room_state(self):
        room = create_room(host_name="Alice")
        mock_ws = AsyncMock()
        with patch.object(ws_module, "broadcast", new_callable=AsyncMock) as mock_bc:
            await ws_module.handle_join(mock_ws, room, {"name": "Alice"})
        mock_bc.assert_called_once()
        msg = mock_bc.call_args[0][1]
        assert msg["type"] == "room_state"


# ===========================================================================
# Direct async unit tests — handle_submit
# ===========================================================================

class TestHandleSubmitDirect:
    def _playing_room(self):
        room = create_room(host_name="Alice")
        room.state = RoomState.PLAYING
        room.problem = FAKE_PROBLEM
        room.start_time = time.time()
        return room

    @pytest.mark.asyncio
    async def test_correct_solution_marks_solved(self):
        room = self._playing_room()
        mock_ws = AsyncMock()
        room.players["Alice"] = Player(name="Alice", websocket=mock_ws)

        with patch.object(ws_module, "broadcast", new_callable=AsyncMock):
            await ws_module.handle_submit(room, "Alice", {"code": CORRECT_TWO_SUM})

        assert room.players["Alice"].best_submission is not None
        assert room.players["Alice"].best_submission["solved"] is True

    @pytest.mark.asyncio
    async def test_correct_solution_all_tests_pass(self):
        room = self._playing_room()
        mock_ws = AsyncMock()
        room.players["Alice"] = Player(name="Alice", websocket=mock_ws)

        with patch.object(ws_module, "broadcast", new_callable=AsyncMock):
            await ws_module.handle_submit(room, "Alice", {"code": CORRECT_TWO_SUM})

        sub = room.players["Alice"].best_submission
        assert sub["passed"] == sub["total"]
        assert sub["total"] > 0

    @pytest.mark.asyncio
    async def test_correct_solution_sends_submit_result(self):
        room = self._playing_room()
        mock_ws = AsyncMock()
        room.players["Alice"] = Player(name="Alice", websocket=mock_ws)

        with patch.object(ws_module, "broadcast", new_callable=AsyncMock):
            await ws_module.handle_submit(room, "Alice", {"code": CORRECT_TWO_SUM})

        calls = [c[0][0] for c in mock_ws.send_json.call_args_list]
        types = [c["type"] for c in calls]
        assert "submit_result" in types

    @pytest.mark.asyncio
    async def test_submit_result_contains_solved_flag(self):
        room = self._playing_room()
        mock_ws = AsyncMock()
        room.players["Alice"] = Player(name="Alice", websocket=mock_ws)

        with patch.object(ws_module, "broadcast", new_callable=AsyncMock):
            await ws_module.handle_submit(room, "Alice", {"code": CORRECT_TWO_SUM})

        sr = next(c[0][0] for c in mock_ws.send_json.call_args_list
                  if c[0][0]["type"] == "submit_result")
        assert "solved" in sr
        assert sr["solved"] is True

    @pytest.mark.asyncio
    async def test_empty_code_sends_error_not_run(self):
        room = self._playing_room()
        mock_ws = AsyncMock()
        room.players["Alice"] = Player(name="Alice", websocket=mock_ws)

        await ws_module.handle_submit(room, "Alice", {"code": "   "})

        mock_ws.send_json.assert_called_once()
        msg = mock_ws.send_json.call_args[0][0]
        assert msg["type"] == "error"
        assert "empty" in msg["message"].lower()

    @pytest.mark.asyncio
    async def test_locked_player_cannot_submit(self):
        room = self._playing_room()
        mock_ws = AsyncMock()
        player = Player(name="Alice", websocket=mock_ws, locked_at=5.0)
        room.players["Alice"] = player

        await ws_module.handle_submit(room, "Alice", {"code": CORRECT_TWO_SUM})

        mock_ws.send_json.assert_called_once()
        msg = mock_ws.send_json.call_args[0][0]
        assert msg["type"] == "error"
        assert "locked" in msg["message"].lower()

    @pytest.mark.asyncio
    async def test_submit_in_non_playing_room_silently_ignored(self):
        room = create_room(host_name="Alice")
        room.state = RoomState.LOBBY
        room.problem = FAKE_PROBLEM
        room.start_time = time.time()
        mock_ws = AsyncMock()
        room.players["Alice"] = Player(name="Alice", websocket=mock_ws)

        await ws_module.handle_submit(room, "Alice", {"code": CORRECT_TWO_SUM})
        mock_ws.send_json.assert_not_called()

    @pytest.mark.asyncio
    async def test_wrong_solution_does_not_mark_solved(self):
        room = self._playing_room()
        mock_ws = AsyncMock()
        room.players["Alice"] = Player(name="Alice", websocket=mock_ws)
        wrong_code = "class Solution:\n    def twoSum(self, nums, target):\n        return [0, 0]"

        with patch.object(ws_module, "broadcast", new_callable=AsyncMock):
            await ws_module.handle_submit(room, "Alice", {"code": wrong_code})

        sub = room.players["Alice"].best_submission
        # If any submission stored, it should NOT be solved (0,0 is wrong for most cases)
        if sub is not None:
            assert sub["solved"] is False

    @pytest.mark.asyncio
    async def test_better_submission_replaces_best(self):
        """A solved submission with fewer chars should replace a solved one with more chars."""
        room = self._playing_room()
        mock_ws = AsyncMock()
        player = Player(name="Alice", websocket=mock_ws)
        player.best_submission = {
            "solved": True, "char_count": 1000, "passed": 2, "total": 2,
            "error": None, "time_ms": 50, "submit_time": 5.0, "code": "x" * 1000,
        }
        room.players["Alice"] = player

        # Submit a much shorter correct solution
        short_correct = (
            "class Solution:\n"
            "    def twoSum(self, nums, target):\n"
            "        seen = {}\n"
            "        for i, v in enumerate(nums):\n"
            "            if target-v in seen: return [seen[target-v], i]\n"
            "            seen[v] = i\n"
        )
        with patch.object(ws_module, "broadcast", new_callable=AsyncMock):
            await ws_module.handle_submit(room, "Alice", {"code": short_correct})

        best = player.best_submission
        if best["solved"]:
            assert best["char_count"] < 1000

    @pytest.mark.asyncio
    async def test_char_count_equals_len_of_code(self):
        room = self._playing_room()
        mock_ws = AsyncMock()
        room.players["Alice"] = Player(name="Alice", websocket=mock_ws)

        with patch.object(ws_module, "broadcast", new_callable=AsyncMock):
            await ws_module.handle_submit(room, "Alice", {"code": CORRECT_TWO_SUM})

        sub = room.players["Alice"].submission
        assert sub["char_count"] == len(CORRECT_TWO_SUM)

    @pytest.mark.asyncio
    async def test_submit_broadcasts_scoreboard(self):
        room = self._playing_room()
        mock_ws = AsyncMock()
        room.players["Alice"] = Player(name="Alice", websocket=mock_ws)

        with patch.object(ws_module, "broadcast", new_callable=AsyncMock) as mock_bc:
            await ws_module.handle_submit(room, "Alice", {"code": CORRECT_TWO_SUM})

        # broadcast should have been called (at least once) with a scoreboard message
        assert mock_bc.called
        msgs = [c[0][1] for c in mock_bc.call_args_list]
        types = [m["type"] for m in msgs]
        assert "scoreboard" in types


# ===========================================================================
# Direct async unit tests — handle_lock
# ===========================================================================

class TestHandleLockDirect:
    def _playing_room_with_solved_player(self):
        room = create_room(host_name="Alice")
        room.state = RoomState.PLAYING
        room.start_time = time.time()
        mock_ws = AsyncMock()
        player = Player(name="Alice", websocket=mock_ws)
        player.best_submission = {
            "solved": True, "char_count": 100, "passed": 2, "total": 2,
            "error": None, "time_ms": 50, "submit_time": 5.0, "code": "",
        }
        room.players["Alice"] = player
        return room, player, mock_ws

    @pytest.mark.asyncio
    async def test_lock_success_sets_locked_at(self):
        room, player, mock_ws = self._playing_room_with_solved_player()
        with patch.object(ws_module, "broadcast", new_callable=AsyncMock):
            await ws_module.handle_lock(mock_ws, room, "Alice")
        assert player.locked_at is not None
        assert isinstance(player.locked_at, float)

    @pytest.mark.asyncio
    async def test_lock_sends_locked_message_to_player(self):
        room, player, mock_ws = self._playing_room_with_solved_player()
        with patch.object(ws_module, "broadcast", new_callable=AsyncMock):
            await ws_module.handle_lock(mock_ws, room, "Alice")
        calls = [c[0][0] for c in mock_ws.send_json.call_args_list]
        types = [c["type"] for c in calls]
        assert "locked" in types

    @pytest.mark.asyncio
    async def test_lock_broadcasts_scoreboard(self):
        room, player, mock_ws = self._playing_room_with_solved_player()
        with patch.object(ws_module, "broadcast", new_callable=AsyncMock) as mock_bc:
            await ws_module.handle_lock(mock_ws, room, "Alice")
        assert mock_bc.called

    @pytest.mark.asyncio
    async def test_lock_without_submission_sends_error(self):
        room = create_room(host_name="Alice")
        room.state = RoomState.PLAYING
        room.start_time = time.time()
        mock_ws = AsyncMock()
        player = Player(name="Alice", websocket=mock_ws)
        player.best_submission = None
        room.players["Alice"] = player

        await ws_module.handle_lock(mock_ws, room, "Alice")

        mock_ws.send_json.assert_called_once()
        assert mock_ws.send_json.call_args[0][0]["type"] == "error"

    @pytest.mark.asyncio
    async def test_lock_with_unsolved_submission_sends_error(self):
        room = create_room(host_name="Alice")
        room.state = RoomState.PLAYING
        room.start_time = time.time()
        mock_ws = AsyncMock()
        player = Player(name="Alice", websocket=mock_ws)
        player.best_submission = {
            "solved": False, "char_count": 100, "passed": 1, "total": 2,
            "error": "wrong", "time_ms": 50, "submit_time": 3.0, "code": "",
        }
        room.players["Alice"] = player

        await ws_module.handle_lock(mock_ws, room, "Alice")

        msg = mock_ws.send_json.call_args[0][0]
        assert msg["type"] == "error"
        assert "solve" in msg["message"].lower()

    @pytest.mark.asyncio
    async def test_double_lock_sends_error(self):
        room, player, mock_ws = self._playing_room_with_solved_player()
        player.locked_at = 5.0  # already locked

        await ws_module.handle_lock(mock_ws, room, "Alice")

        msg = mock_ws.send_json.call_args[0][0]
        assert msg["type"] == "error"
        assert "locked" in msg["message"].lower()

    @pytest.mark.asyncio
    async def test_lock_in_lobby_state_is_ignored(self):
        room = create_room(host_name="Alice")
        room.state = RoomState.LOBBY
        mock_ws = AsyncMock()
        player = Player(name="Alice", websocket=mock_ws)
        player.best_submission = {
            "solved": True, "char_count": 100, "passed": 2, "total": 2,
            "error": None, "time_ms": 50, "submit_time": 3.0, "code": "",
        }
        room.players["Alice"] = player

        await ws_module.handle_lock(mock_ws, room, "Alice")

        mock_ws.send_json.assert_not_called()
        assert player.locked_at is None

    @pytest.mark.asyncio
    async def test_all_locked_triggers_end_game(self):
        """When all players lock in, end_game should be called."""
        room = create_room(host_name="Alice")
        room.state = RoomState.PLAYING
        room.start_time = time.time()
        room.total_rounds = 1
        room.current_round = 1

        mock_ws_alice = AsyncMock()
        mock_ws_bob = AsyncMock()

        alice = Player(name="Alice", websocket=mock_ws_alice)
        alice.best_submission = {
            "solved": True, "char_count": 100, "passed": 2, "total": 2,
            "error": None, "time_ms": 50, "submit_time": 3.0, "code": "",
        }
        bob = Player(name="Bob", websocket=mock_ws_bob)
        bob.best_submission = {
            "solved": True, "char_count": 120, "passed": 2, "total": 2,
            "error": None, "time_ms": 60, "submit_time": 8.0, "code": "",
        }
        bob.locked_at = 8.0  # Bob is already locked

        room.players["Alice"] = alice
        room.players["Bob"] = bob

        with patch.object(ws_module, "end_game", new_callable=AsyncMock) as mock_end:
            with patch.object(ws_module, "broadcast", new_callable=AsyncMock):
                await ws_module.handle_lock(mock_ws_alice, room, "Alice")

        mock_end.assert_called_once_with(room)


# ===========================================================================
# Direct async unit tests — handle_restart
# ===========================================================================

class TestHandleRestartDirect:
    @pytest.mark.asyncio
    async def test_non_host_cannot_restart(self):
        room = create_room(host_name="Alice")
        room.state = RoomState.FINISHED
        mock_ws = AsyncMock()
        await ws_module.handle_restart(mock_ws, room, "Bob")
        msg = mock_ws.send_json.call_args[0][0]
        assert msg["type"] == "error"
        assert "host" in msg["message"].lower()

    @pytest.mark.asyncio
    async def test_restart_when_not_finished_sends_error(self):
        room = create_room(host_name="Alice")
        room.state = RoomState.PLAYING
        mock_ws = AsyncMock()
        await ws_module.handle_restart(mock_ws, room, "Alice")
        msg = mock_ws.send_json.call_args[0][0]
        assert msg["type"] == "error"
        assert "finished" in msg["message"].lower()

    @pytest.mark.asyncio
    async def test_restart_resets_state_to_lobby(self):
        room = create_room(host_name="Alice")
        room.state = RoomState.FINISHED
        mock_ws = AsyncMock()
        with patch.object(ws_module, "broadcast", new_callable=AsyncMock):
            await ws_module.handle_restart(mock_ws, room, "Alice")
        assert room.state == RoomState.LOBBY

    @pytest.mark.asyncio
    async def test_restart_clears_problem(self):
        room = create_room(host_name="Alice")
        room.state = RoomState.FINISHED
        room.problem = FAKE_PROBLEM
        mock_ws = AsyncMock()
        with patch.object(ws_module, "broadcast", new_callable=AsyncMock):
            await ws_module.handle_restart(mock_ws, room, "Alice")
        assert room.problem is None

    @pytest.mark.asyncio
    async def test_restart_clears_start_time(self):
        room = create_room(host_name="Alice")
        room.state = RoomState.FINISHED
        room.start_time = 12345.0
        mock_ws = AsyncMock()
        with patch.object(ws_module, "broadcast", new_callable=AsyncMock):
            await ws_module.handle_restart(mock_ws, room, "Alice")
        assert room.start_time is None

    @pytest.mark.asyncio
    async def test_restart_resets_current_round_to_zero(self):
        room = create_room(host_name="Alice")
        room.state = RoomState.FINISHED
        room.current_round = 3
        mock_ws = AsyncMock()
        with patch.object(ws_module, "broadcast", new_callable=AsyncMock):
            await ws_module.handle_restart(mock_ws, room, "Alice")
        assert room.current_round == 0

    @pytest.mark.asyncio
    async def test_restart_clears_all_player_submission_data(self):
        room = create_room(host_name="Alice")
        room.state = RoomState.FINISHED

        player = Player(name="Alice")
        player.submission = {"solved": True}
        player.best_submission = {"solved": True}
        player.locked_at = 10.0
        room.players["Alice"] = player

        mock_ws = AsyncMock()
        with patch.object(ws_module, "broadcast", new_callable=AsyncMock):
            await ws_module.handle_restart(mock_ws, room, "Alice")

        assert player.submission is None
        assert player.best_submission is None
        assert player.locked_at is None

    @pytest.mark.asyncio
    async def test_restart_broadcasts_room_state(self):
        room = create_room(host_name="Alice")
        room.state = RoomState.FINISHED
        mock_ws = AsyncMock()
        with patch.object(ws_module, "broadcast", new_callable=AsyncMock) as mock_bc:
            await ws_module.handle_restart(mock_ws, room, "Alice")
        mock_bc.assert_called_once()
        msg = mock_bc.call_args[0][1]
        assert msg["type"] == "room_state"


# ===========================================================================
# Direct async unit tests — end_game
# ===========================================================================

class TestEndGame:
    @pytest.mark.asyncio
    async def test_already_finished_room_is_noop(self):
        room = create_room(host_name="Alice")
        room.state = RoomState.FINISHED
        with patch.object(ws_module, "broadcast", new_callable=AsyncMock) as mock_bc:
            await ws_module.end_game(room)
        mock_bc.assert_not_called()

    @pytest.mark.asyncio
    async def test_final_round_sends_game_over(self):
        room = create_room(host_name="Alice")
        room.state = RoomState.PLAYING
        room.total_rounds = 1
        room.current_round = 1

        with patch.object(ws_module, "broadcast", new_callable=AsyncMock) as mock_bc:
            await ws_module.end_game(room)

        assert room.state == RoomState.FINISHED
        types = [c[0][1]["type"] for c in mock_bc.call_args_list]
        assert "game_over" in types

    @pytest.mark.asyncio
    async def test_game_over_message_contains_rankings(self):
        room = create_room(host_name="Alice")
        room.state = RoomState.PLAYING
        room.total_rounds = 1
        room.current_round = 1
        room.players["Alice"] = Player(name="Alice")

        with patch.object(ws_module, "broadcast", new_callable=AsyncMock) as mock_bc:
            await ws_module.end_game(room)

        msgs = [c[0][1] for c in mock_bc.call_args_list if c[0][1]["type"] == "game_over"]
        assert len(msgs) == 1
        assert "rankings" in msgs[0]

    @pytest.mark.asyncio
    async def test_non_final_round_sends_round_over(self):
        room = create_room(host_name="Alice")
        room.state = RoomState.PLAYING
        room.total_rounds = 3
        room.current_round = 1

        with patch.object(ws_module, "broadcast", new_callable=AsyncMock) as mock_bc:
            with patch("asyncio.create_task"):  # prevent background break_task
                await ws_module.end_game(room)

        types = [c[0][1]["type"] for c in mock_bc.call_args_list]
        assert "round_over" in types

    @pytest.mark.asyncio
    async def test_non_final_round_sets_state_to_finished_temporarily(self):
        room = create_room(host_name="Alice")
        room.state = RoomState.PLAYING
        room.total_rounds = 3
        room.current_round = 1

        with patch.object(ws_module, "broadcast", new_callable=AsyncMock):
            with patch("asyncio.create_task"):
                await ws_module.end_game(room)

        assert room.state == RoomState.FINISHED

    @pytest.mark.asyncio
    async def test_round_over_message_contains_break_seconds(self):
        room = create_room(host_name="Alice")
        room.state = RoomState.PLAYING
        room.total_rounds = 2
        room.current_round = 1

        with patch.object(ws_module, "broadcast", new_callable=AsyncMock) as mock_bc:
            with patch("asyncio.create_task"):
                await ws_module.end_game(room)

        msgs = [c[0][1] for c in mock_bc.call_args_list if c[0][1]["type"] == "round_over"]
        assert len(msgs) == 1
        assert "break_seconds" in msgs[0]
