"""
Unit tests for pure logic functions in server/ws.py.

Tests cover:
- fix_exponents: all transformation cases
- _is_better: all comparison scenarios
- room_state_msg: message structure
- scoreboard_msg: message structure
"""

import pytest
from server.ws import fix_exponents, _is_better, room_state_msg, scoreboard_msg
from server.rooms import Room, RoomState, Player


# ---------------------------------------------------------------------------
# fix_exponents
# ---------------------------------------------------------------------------

class TestFixExponents:
    # --- Explicit caret notation ---

    def test_explicit_caret_10_to_5(self):
        result = fix_exponents("10^5")
        assert result == "10\u2075"

    def test_explicit_caret_10_to_9(self):
        result = fix_exponents("10^9")
        assert result == "10\u2079"

    def test_explicit_caret_2_to_31(self):
        result = fix_exponents("2^31")
        assert result == "2\u00b3\u00b9"

    def test_explicit_caret_2_to_32(self):
        result = fix_exponents("2^32")
        assert result == "2\u00b3\u00b2"

    def test_explicit_caret_single_digit_exponent(self):
        result = fix_exponents("3^2")
        assert result == "3\u00b2"

    # --- Collapsed base-10 exponents (4-9 range) ---

    def test_collapsed_104_becomes_10_sup4(self):
        result = fix_exponents("104")
        assert result == "10\u2074"

    def test_collapsed_107_becomes_10_sup7(self):
        result = fix_exponents("107")
        assert result == "10\u2077"

    def test_collapsed_109_becomes_10_sup9(self):
        result = fix_exponents("109")
        assert result == "10\u2079"

    def test_collapsed_103_not_transformed(self):
        """Exponents 0-3 are outside the 4-9 range and must not be changed."""
        result = fix_exponents("103")
        assert result == "103"

    def test_collapsed_110_not_transformed(self):
        """110 could naively match '11' + '0', but '0' is outside the 4-9 range."""
        result = fix_exponents("110")
        assert result == "110"

    # --- Collapsed 2^31 and 2^32 ---

    def test_collapsed_231_becomes_2_sup31(self):
        result = fix_exponents("231")
        assert result == "2\u00b3\u00b9"

    def test_collapsed_232_becomes_2_sup32(self):
        result = fix_exponents("232")
        assert result == "2\u00b3\u00b2"

    # --- Negative variants ---

    def test_negative_collapsed_104(self):
        result = fix_exponents("-104")
        assert result == "-10\u2074"

    def test_negative_collapsed_231(self):
        result = fix_exponents("-231")
        assert result == "-2\u00b3\u00b9"

    # --- Text unchanged ---

    def test_plain_text_unchanged(self):
        text = "Given an array of integers"
        assert fix_exponents(text) == text

    def test_empty_string_unchanged(self):
        assert fix_exponents("") == ""

    # --- Mixed content ---

    def test_mixed_text_with_caret_and_collapsed(self):
        text = "Array length up to 10^5 and value up to 2^31"
        result = fix_exponents(text)
        assert "10\u2075" in result
        assert "2\u00b3\u00b9" in result

    def test_multiple_exponents_in_sequence(self):
        text = "Range: 10^4 to 10^9"
        result = fix_exponents(text)
        assert "10\u2074" in result
        assert "10\u2079" in result


# ---------------------------------------------------------------------------
# _is_better
# ---------------------------------------------------------------------------

class TestIsBetter:
    # --- solved vs unsolved ---

    def test_solved_beats_unsolved(self):
        new = {"solved": True,  "char_count": 999, "passed": 5}
        old = {"solved": False, "char_count": 10,  "passed": 4}
        assert _is_better(new, old) is True

    def test_unsolved_does_not_beat_solved(self):
        new = {"solved": False, "char_count": 10,  "passed": 4}
        old = {"solved": True,  "char_count": 999, "passed": 5}
        assert _is_better(new, old) is False

    # --- both solved: fewer chars wins ---

    def test_both_solved_fewer_chars_is_better(self):
        new = {"solved": True, "char_count": 80,  "passed": 5}
        old = {"solved": True, "char_count": 100, "passed": 5}
        assert _is_better(new, old) is True

    def test_both_solved_more_chars_is_not_better(self):
        new = {"solved": True, "char_count": 200, "passed": 5}
        old = {"solved": True, "char_count": 100, "passed": 5}
        assert _is_better(new, old) is False

    def test_both_solved_equal_chars_is_not_better(self):
        new = {"solved": True, "char_count": 100, "passed": 5}
        old = {"solved": True, "char_count": 100, "passed": 5}
        assert _is_better(new, old) is False

    def test_both_solved_fewer_chars_by_one(self):
        new = {"solved": True, "char_count": 99,  "passed": 5}
        old = {"solved": True, "char_count": 100, "passed": 5}
        assert _is_better(new, old) is True

    # --- both unsolved: more tests passed wins ---

    def test_both_unsolved_more_passed_is_better(self):
        new = {"solved": False, "char_count": 50, "passed": 3}
        old = {"solved": False, "char_count": 50, "passed": 1}
        assert _is_better(new, old) is True

    def test_both_unsolved_fewer_passed_is_not_better(self):
        new = {"solved": False, "char_count": 50, "passed": 1}
        old = {"solved": False, "char_count": 50, "passed": 3}
        assert _is_better(new, old) is False

    def test_both_unsolved_equal_passed_is_not_better(self):
        new = {"solved": False, "char_count": 50, "passed": 2}
        old = {"solved": False, "char_count": 50, "passed": 2}
        assert _is_better(new, old) is False

    def test_both_unsolved_zero_vs_zero_is_not_better(self):
        new = {"solved": False, "char_count": 50, "passed": 0}
        old = {"solved": False, "char_count": 50, "passed": 0}
        assert _is_better(new, old) is False


# ---------------------------------------------------------------------------
# room_state_msg
# ---------------------------------------------------------------------------

class TestRoomStateMsg:
    def _make_room(self, **kwargs):
        defaults = dict(
            id="ABCDEF",
            host="Alice",
            state=RoomState.LOBBY,
            time_limit=300,
            difficulty="Easy",
            total_rounds=2,
            current_round=0,
        )
        defaults.update(kwargs)
        return Room(**defaults)

    def test_type_is_room_state(self):
        msg = room_state_msg(self._make_room())
        assert msg["type"] == "room_state"

    def test_room_id_matches(self):
        msg = room_state_msg(self._make_room())
        assert msg["room_id"] == "ABCDEF"

    def test_state_value_is_string(self):
        msg = room_state_msg(self._make_room())
        assert msg["state"] == "lobby"

    def test_state_value_when_playing(self):
        msg = room_state_msg(self._make_room(state=RoomState.PLAYING))
        assert msg["state"] == "playing"

    def test_host_included(self):
        msg = room_state_msg(self._make_room())
        assert msg["host"] == "Alice"

    def test_players_list_when_empty(self):
        msg = room_state_msg(self._make_room())
        assert msg["players"] == []

    def test_players_list_when_populated(self):
        room = self._make_room()
        room.players["Alice"] = Player(name="Alice")
        room.players["Bob"]   = Player(name="Bob")
        msg = room_state_msg(room)
        assert set(msg["players"]) == {"Alice", "Bob"}

    def test_time_limit_included(self):
        msg = room_state_msg(self._make_room())
        assert msg["time_limit"] == 300

    def test_difficulty_included(self):
        msg = room_state_msg(self._make_room())
        assert msg["difficulty"] == "Easy"

    def test_current_round_included(self):
        msg = room_state_msg(self._make_room(current_round=1))
        assert msg["current_round"] == 1

    def test_total_rounds_included(self):
        msg = room_state_msg(self._make_room())
        assert msg["total_rounds"] == 2

    def test_required_keys_all_present(self):
        msg = room_state_msg(self._make_room())
        required = {
            "type", "room_id", "state", "host",
            "players", "time_limit", "difficulty",
            "current_round", "total_rounds",
        }
        assert required.issubset(set(msg.keys()))


# ---------------------------------------------------------------------------
# scoreboard_msg
# ---------------------------------------------------------------------------

class TestScoreboardMsg:
    def test_type_is_scoreboard(self):
        room = Room(id="ABCDEF", host="Alice")
        msg = scoreboard_msg(room)
        assert msg["type"] == "scoreboard"

    def test_rankings_key_present(self):
        room = Room(id="ABCDEF", host="Alice")
        msg = scoreboard_msg(room)
        assert "rankings" in msg

    def test_rankings_is_list(self):
        room = Room(id="ABCDEF", host="Alice")
        msg = scoreboard_msg(room)
        assert isinstance(msg["rankings"], list)

    def test_empty_room_has_empty_rankings(self):
        room = Room(id="ABCDEF", host="Alice")
        msg = scoreboard_msg(room)
        assert msg["rankings"] == []

    def test_rankings_reflect_player_count(self):
        room = Room(id="ABCDEF", host="Alice")
        room.players["Alice"] = Player(name="Alice")
        room.players["Bob"]   = Player(name="Bob")
        msg = scoreboard_msg(room)
        assert len(msg["rankings"]) == 2

    def test_rankings_entries_have_position(self):
        room = Room(id="ABCDEF", host="Alice")
        room.players["Alice"] = Player(name="Alice")
        msg = scoreboard_msg(room)
        assert "position" in msg["rankings"][0]
