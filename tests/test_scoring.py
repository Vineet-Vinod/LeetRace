"""
Unit tests for server/scoring.py — ranking and ordering logic.

Tests cover:
- Empty player sets
- Solved players ranking above unsolved
- Tiebreaking by char_count (fewer is better)
- Tiebreaking by locked_at (earlier is better)
- Tiebreaking by tests_passed (more is better)
- Players with no submission at all
- Position numbering (1-indexed, sequential)
"""

from server.rooms import Player
from server.scoring import rank_players


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def make_player(
    name,
    solved=False,
    char_count=999999,
    passed=0,
    total=0,
    locked_at=None,
    submit_time=999999,
    code="def solution(): pass",
):
    """Create a Player with best_submission pre-populated for convenience."""
    p = Player(name=name)
    p.locked_at = locked_at
    if solved or passed > 0:
        p.best_submission = {
            "solved": solved,
            "char_count": char_count,
            "passed": passed,
            "total": total,
            "submit_time": submit_time,
            "error": None,
            "code": code,
        }
    return p


# ---------------------------------------------------------------------------
# Empty / single player
# ---------------------------------------------------------------------------


class TestRankPlayersEmpty:
    def test_empty_dict_returns_empty_list(self):
        result = rank_players({})
        assert result == []

    def test_single_player_no_submission_position_is_1(self):
        players = {"Alice": Player(name="Alice")}
        result = rank_players(players)
        assert len(result) == 1
        assert result[0]["position"] == 1
        assert result[0]["name"] == "Alice"
        assert result[0]["solved"] is False
        assert result[0]["tests_passed"] == 0


# ---------------------------------------------------------------------------
# Solved beats unsolved
# ---------------------------------------------------------------------------


class TestRankPlayersSolvedFirst:
    def test_solved_player_ranks_above_unsolved(self):
        players = {
            "Alice": make_player("Alice", solved=False, passed=2, total=5),
            "Bob": make_player("Bob", solved=True, char_count=100, passed=5, total=5),
        }
        result = rank_players(players)
        assert result[0]["name"] == "Bob"
        assert result[0]["position"] == 1
        assert result[1]["name"] == "Alice"
        assert result[1]["position"] == 2

    def test_all_solved_sorted_by_char_count_ascending(self):
        players = {
            "Alice": make_player(
                "Alice", solved=True, char_count=200, passed=5, total=5
            ),
            "Bob": make_player("Bob", solved=True, char_count=100, passed=5, total=5),
            "Carol": make_player(
                "Carol", solved=True, char_count=150, passed=5, total=5
            ),
        }
        result = rank_players(players)
        names = [e["name"] for e in result]
        assert names == ["Bob", "Carol", "Alice"]

    def test_same_char_count_solved_tiebreak_by_locked_at(self):
        players = {
            "Alice": make_player(
                "Alice", solved=True, char_count=100, passed=5, total=5, locked_at=30.0
            ),
            "Bob": make_player(
                "Bob", solved=True, char_count=100, passed=5, total=5, locked_at=10.0
            ),
        }
        result = rank_players(players)
        # Bob locked in earlier — should rank first
        assert result[0]["name"] == "Bob"
        assert result[1]["name"] == "Alice"

    def test_solved_with_lock_beats_solved_without_lock(self):
        """locked_at=None is treated as infinity, so a player with a lock wins."""
        players = {
            "Alice": make_player(
                "Alice", solved=True, char_count=100, passed=5, total=5, locked_at=None
            ),
            "Bob": make_player(
                "Bob", solved=True, char_count=100, passed=5, total=5, locked_at=20.0
            ),
        }
        result = rank_players(players)
        assert result[0]["name"] == "Bob"

    def test_solved_and_unsolved_mixed_ordering(self):
        players = {
            "A": make_player(
                "A", solved=True, char_count=50, passed=3, total=3, locked_at=5.0
            ),
            "B": make_player("B", solved=False, passed=2, total=3),
            "C": make_player(
                "C", solved=True, char_count=80, passed=3, total=3, locked_at=3.0
            ),
            "D": make_player("D", solved=False, passed=0, total=3),
        }
        result = rank_players(players)
        names = [e["name"] for e in result]
        # Solved first: A (50 chars) < C (80 chars)
        assert names[0] == "A"
        assert names[1] == "C"
        # Unsolved: B (2 passed) > D (0 passed)
        assert names[2] == "B"
        assert names[3] == "D"


# ---------------------------------------------------------------------------
# Unsolved tiebreaks
# ---------------------------------------------------------------------------


class TestRankPlayersUnsolved:
    def test_unsolved_sorted_by_tests_passed_descending(self):
        players = {
            "Alice": make_player("Alice", solved=False, passed=1, total=5),
            "Bob": make_player("Bob", solved=False, passed=4, total=5),
            "Carol": make_player("Carol", solved=False, passed=2, total=5),
        }
        result = rank_players(players)
        names = [e["name"] for e in result]
        assert names == ["Bob", "Carol", "Alice"]

    def test_zero_passed_ranks_last_among_unsolved(self):
        players = {
            "Alice": make_player("Alice", solved=False, passed=3, total=5),
            "Bob": make_player("Bob", solved=False, passed=0, total=5),
        }
        result = rank_players(players)
        assert result[0]["name"] == "Alice"
        assert result[1]["name"] == "Bob"


# ---------------------------------------------------------------------------
# Position numbering
# ---------------------------------------------------------------------------


class TestRankPlayersPositions:
    def test_positions_are_1_indexed_and_sequential(self):
        players = {
            "A": make_player("A", solved=True, char_count=100, passed=5, total=5),
            "B": make_player("B", solved=False, passed=2, total=5),
            "C": make_player("C", solved=False, passed=0, total=5),
        }
        result = rank_players(players)
        assert [e["position"] for e in result] == [1, 2, 3]

    def test_result_entry_contains_all_required_fields(self):
        players = {
            "Alice": make_player("Alice", solved=True, char_count=50, passed=3, total=3)
        }
        result = rank_players(players)
        entry = result[0]
        required = {
            "name",
            "solved",
            "char_count",
            "submit_time",
            "locked_at",
            "tests_passed",
            "tests_total",
            "error",
            "position",
        }
        assert required.issubset(set(entry.keys()))


# ---------------------------------------------------------------------------
# Players with no submission
# ---------------------------------------------------------------------------


class TestRankPlayersNoSubmission:
    def test_no_submission_uses_default_values(self):
        p = Player(name="Ghost")
        result = rank_players({"Ghost": p})
        entry = result[0]
        assert entry["solved"] is False
        assert entry["char_count"] == float("inf")
        assert entry["tests_passed"] == 0
        assert entry["locked_at"] is None

    def test_no_submission_ranks_below_partial_submission(self):
        players = {
            "Ghost": Player(name="Ghost"),
            "Alice": make_player("Alice", solved=False, passed=1, total=5),
        }
        result = rank_players(players)
        assert result[0]["name"] == "Alice"
        assert result[1]["name"] == "Ghost"

    def test_two_players_no_submissions_both_get_positions(self):
        players = {
            "A": Player(name="A"),
            "B": Player(name="B"),
        }
        result = rank_players(players)
        positions = {e["name"]: e["position"] for e in result}
        assert set(positions.values()) == {1, 2}


# ---------------------------------------------------------------------------
# Code field — opponent code reveal feature
# ---------------------------------------------------------------------------


class TestRankPlayersCodeField:
    """rank_players() must include a ``code`` key in every entry.

    Code is only populated when ``include_code=True`` (end-of-game payloads).
    During live gameplay the default ``include_code=False`` ensures opponent
    code is not leaked via WebSocket scoreboard messages.
    """

    def test_code_field_present_for_player_with_submission(self):
        players = {
            "Alice": make_player(
                "Alice", solved=True, char_count=50, passed=3, total=3,
                code="def f(x): return x"
            )
        }
        result = rank_players(players, include_code=True)
        assert "code" in result[0]
        assert result[0]["code"] == "def f(x): return x"

    def test_code_field_hidden_by_default(self):
        """Without include_code, code must be None to prevent mid-game leaking."""
        players = {
            "Alice": make_player(
                "Alice", solved=True, char_count=50, passed=3, total=3,
                code="def f(x): return x"
            )
        }
        result = rank_players(players)
        assert result[0]["code"] is None

    def test_code_field_is_none_when_no_submission(self):
        # A Player with no best_submission should yield code=None so the
        # frontend can show a "No submission" placeholder.
        players = {"Ghost": Player(name="Ghost")}
        result = rank_players(players, include_code=True)
        assert "code" in result[0]
        assert result[0]["code"] is None

    def test_code_field_present_in_all_required_fields_check(self):
        """Extend the existing required-fields test to include 'code'."""
        players = {
            "Alice": make_player(
                "Alice", solved=True, char_count=50, passed=3, total=3
            )
        }
        result = rank_players(players, include_code=True)
        entry = result[0]
        required = {
            "name", "solved", "char_count", "submit_time", "locked_at",
            "tests_passed", "tests_total", "error", "position", "code",
        }
        assert required.issubset(set(entry.keys()))

    def test_code_field_for_unsolved_player_with_partial_submission(self):
        players = {
            "Bob": make_player(
                "Bob", solved=False, passed=2, total=5, code="def g(): pass"
            )
        }
        result = rank_players(players, include_code=True)
        assert result[0]["code"] == "def g(): pass"
