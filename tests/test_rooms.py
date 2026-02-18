"""
Unit tests for server/rooms.py — room creation, state, and player management.

Tests cover:
- create_room: default and custom parameters, id format, global registry
- get_room: hits and misses
- remove_room: deletion, idempotency, isolation
- RoomState enum values and transitions
- Player dataclass defaults and mutation
"""

from server.rooms import (
    Room,
    Player,
    RoomState,
    create_room,
    get_room,
    remove_room,
    rooms,
)


# ---------------------------------------------------------------------------
# create_room
# ---------------------------------------------------------------------------


class TestCreateRoom:
    def test_returns_room_object(self):
        room = create_room(host_name="Alice")
        assert isinstance(room, Room)

    def test_host_name_stored_correctly(self):
        room = create_room(host_name="Alice")
        assert room.host == "Alice"

    def test_default_state_is_lobby(self):
        room = create_room(host_name="Alice")
        assert room.state == RoomState.LOBBY

    def test_default_time_limit_is_300(self):
        room = create_room(host_name="Alice")
        assert room.time_limit == 300

    def test_custom_time_limit_stored(self):
        room = create_room(host_name="Alice", time_limit=120)
        assert room.time_limit == 120

    def test_default_difficulty_is_none(self):
        room = create_room(host_name="Alice")
        assert room.difficulty is None

    def test_custom_difficulty_stored(self):
        room = create_room(host_name="Alice", difficulty="easy")
        assert room.difficulty == "easy"

    def test_default_rounds_is_1(self):
        room = create_room(host_name="Alice")
        assert room.total_rounds == 1

    def test_custom_rounds_stored(self):
        room = create_room(host_name="Alice", rounds=3)
        assert room.total_rounds == 3

    def test_room_id_is_6_characters(self):
        room = create_room(host_name="Alice")
        assert len(room.id) == 6

    def test_room_id_is_uppercase_hex(self):
        for _ in range(10):
            room = create_room(host_name="Alice")
            assert room.id == room.id.upper()
            # Raises ValueError if not valid hex
            int(room.id, 16)

    def test_room_added_to_global_registry(self):
        room = create_room(host_name="Alice")
        assert room.id in rooms

    def test_players_starts_empty(self):
        room = create_room(host_name="Alice")
        assert room.players == {}

    def test_problem_starts_as_none(self):
        room = create_room(host_name="Alice")
        assert room.problem is None

    def test_start_time_starts_as_none(self):
        room = create_room(host_name="Alice")
        assert room.start_time is None

    def test_current_round_starts_at_zero(self):
        room = create_room(host_name="Alice")
        assert room.current_round == 0

    def test_two_rooms_have_different_ids(self):
        # Create many rooms and ensure no collisions (probabilistic but reliable)
        ids = {create_room(host_name="Alice").id for _ in range(20)}
        assert len(ids) == 20

    def test_all_created_rooms_retrievable(self):
        room1 = create_room(host_name="Alice")
        room2 = create_room(host_name="Bob")
        assert get_room(room1.id) is room1
        assert get_room(room2.id) is room2


# ---------------------------------------------------------------------------
# get_room
# ---------------------------------------------------------------------------


class TestGetRoom:
    def test_returns_correct_room_for_valid_id(self):
        room = create_room(host_name="Alice")
        fetched = get_room(room.id)
        assert fetched is room

    def test_returns_none_for_unknown_id(self):
        assert get_room("ZZZZZZ") is None

    def test_returns_none_for_empty_string(self):
        assert get_room("") is None

    def test_returns_none_after_room_removed(self):
        room = create_room(host_name="Alice")
        room_id = room.id
        remove_room(room_id)
        assert get_room(room_id) is None

    def test_returns_same_object_reference(self):
        """get_room should return the same mutable object, not a copy."""
        room = create_room(host_name="Alice")
        fetched = get_room(room.id)
        fetched.host = "Modified"
        assert room.host == "Modified"


# ---------------------------------------------------------------------------
# remove_room
# ---------------------------------------------------------------------------


class TestRemoveRoom:
    def test_removes_room_from_registry(self):
        room = create_room(host_name="Alice")
        room_id = room.id
        remove_room(room_id)
        assert room_id not in rooms

    def test_nonexistent_id_does_not_raise(self):
        # Must not raise KeyError or any other exception
        remove_room("DOESNT_EXIST_XYZ")

    def test_does_not_affect_other_rooms(self):
        room1 = create_room(host_name="Alice")
        room2 = create_room(host_name="Bob")
        remove_room(room1.id)
        assert get_room(room2.id) is room2

    def test_double_remove_does_not_raise(self):
        room = create_room(host_name="Alice")
        room_id = room.id
        remove_room(room_id)
        remove_room(room_id)  # second call should also be a no-op


# ---------------------------------------------------------------------------
# RoomState enum
# ---------------------------------------------------------------------------


class TestRoomState:
    def test_lobby_value(self):
        assert RoomState.LOBBY.value == "lobby"

    def test_playing_value(self):
        assert RoomState.PLAYING.value == "playing"

    def test_finished_value(self):
        assert RoomState.FINISHED.value == "finished"

    def test_is_string_enum(self):
        assert isinstance(RoomState.LOBBY, str)
        assert RoomState.LOBBY == "lobby"

    def test_state_transitions(self):
        room = create_room(host_name="Alice")
        assert room.state == RoomState.LOBBY
        room.state = RoomState.PLAYING
        assert room.state == RoomState.PLAYING
        room.state = RoomState.FINISHED
        assert room.state == RoomState.FINISHED


# ---------------------------------------------------------------------------
# Player dataclass
# ---------------------------------------------------------------------------


class TestPlayer:
    def test_default_fields(self):
        p = Player(name="Alice")
        assert p.name == "Alice"
        assert p.websocket is None
        assert p.submission is None
        assert p.best_submission is None
        assert p.locked_at is None

    def test_submission_can_be_set(self):
        p = Player(name="Alice")
        sub = {
            "solved": True,
            "passed": 5,
            "total": 5,
            "char_count": 100,
            "error": None,
            "time_ms": 50,
            "submit_time": 10.0,
        }
        p.submission = sub
        assert p.submission["solved"] is True

    def test_best_submission_can_be_set(self):
        p = Player(name="Alice")
        best = {"solved": True, "char_count": 80}
        p.best_submission = best
        assert p.best_submission["char_count"] == 80

    def test_locked_at_can_be_set_to_float(self):
        p = Player(name="Alice")
        p.locked_at = 42.5
        assert p.locked_at == 42.5

    def test_locked_at_can_be_set_to_zero(self):
        p = Player(name="Alice")
        p.locked_at = 0.0
        assert p.locked_at == 0.0

    def test_players_are_independent_objects(self):
        p1 = Player(name="Alice")
        p2 = Player(name="Bob")
        p1.locked_at = 10.0
        assert p2.locked_at is None
