"""
Integration tests for FastAPI REST endpoints via TestClient.

Tests cover:
- POST /api/rooms: creation, defaults, clamping, round/difficulty storage
- GET /api/rooms/{room_id}: existing rooms, missing rooms, response shape
- GET /api/problems: list format, non-empty, required fields
- GET /  and  GET /room: HTML pages served
"""

import pytest
from fastapi.testclient import TestClient

from server.app import app
import server.rooms as rooms_module


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


# ---------------------------------------------------------------------------
# POST /api/rooms
# ---------------------------------------------------------------------------


class TestCreateRoomEndpoint:
    def test_success_returns_200(self, client):
        resp = client.post("/api/rooms", json={"host": "Alice"})
        assert resp.status_code == 200

    def test_response_contains_room_id(self, client):
        data = client.post("/api/rooms", json={"host": "Alice"}).json()
        assert "room_id" in data

    def test_response_contains_host(self, client):
        data = client.post("/api/rooms", json={"host": "Alice"}).json()
        assert data["host"] == "Alice"

    def test_room_id_is_6_characters(self, client):
        data = client.post("/api/rooms", json={"host": "Alice"}).json()
        assert len(data["room_id"]) == 6

    def test_room_id_is_uppercase_hex(self, client):
        data = client.post("/api/rooms", json={"host": "Alice"}).json()
        room_id = data["room_id"]
        assert room_id == room_id.upper()
        int(room_id, 16)  # validates hex — raises ValueError if not

    def test_empty_json_body_uses_default_host(self, client):
        data = client.post("/api/rooms", json={}).json()
        assert data["host"] == "Host"

    def test_no_body_uses_default_host(self, client):
        data = client.post("/api/rooms").json()
        assert data["host"] == "Host"

    def test_custom_time_limit_stored_in_room(self, client):
        resp = client.post("/api/rooms", json={"host": "Alice", "time_limit": 120})
        room_id = resp.json()["room_id"]
        room = rooms_module.get_room(room_id)
        assert room.time_limit == 120

    def test_rounds_clamped_to_max_10(self, client):
        resp = client.post("/api/rooms", json={"host": "Alice", "rounds": 999})
        room_id = resp.json()["room_id"]
        room = rooms_module.get_room(room_id)
        assert room.total_rounds == 10

    def test_rounds_clamped_to_min_1(self, client):
        resp = client.post("/api/rooms", json={"host": "Alice", "rounds": 0})
        room_id = resp.json()["room_id"]
        room = rooms_module.get_room(room_id)
        assert room.total_rounds == 1

    def test_rounds_negative_clamped_to_1(self, client):
        resp = client.post("/api/rooms", json={"host": "Alice", "rounds": -5})
        room_id = resp.json()["room_id"]
        room = rooms_module.get_room(room_id)
        assert room.total_rounds == 1

    def test_difficulty_stored_in_room(self, client):
        resp = client.post("/api/rooms", json={"host": "Alice", "difficulty": "Hard"})
        room_id = resp.json()["room_id"]
        get_resp = client.get(f"/api/rooms/{room_id}")
        assert get_resp.json()["difficulty"] == "Hard"

    def test_two_rooms_have_different_ids(self, client):
        id1 = client.post("/api/rooms", json={"host": "Alice"}).json()["room_id"]
        id2 = client.post("/api/rooms", json={"host": "Bob"}).json()["room_id"]
        assert id1 != id2

    def test_many_rooms_all_have_unique_ids(self, client):
        ids = [
            client.post("/api/rooms", json={"host": f"User{i}"}).json()["room_id"]
            for i in range(10)
        ]
        assert len(set(ids)) == 10

    def test_room_state_starts_as_lobby(self, client):
        resp = client.post("/api/rooms", json={"host": "Alice"})
        room_id = resp.json()["room_id"]
        get_resp = client.get(f"/api/rooms/{room_id}")
        assert get_resp.json()["state"] == "lobby"


# ---------------------------------------------------------------------------
# GET /api/rooms/{room_id}
# ---------------------------------------------------------------------------


class TestGetRoomEndpoint:
    def test_existing_room_returns_200(self, client):
        room_id = client.post("/api/rooms", json={"host": "Alice"}).json()["room_id"]
        assert client.get(f"/api/rooms/{room_id}").status_code == 200

    def test_response_has_room_id_field(self, client):
        room_id = client.post("/api/rooms", json={"host": "Alice"}).json()["room_id"]
        data = client.get(f"/api/rooms/{room_id}").json()
        assert data["room_id"] == room_id

    def test_response_has_state_field(self, client):
        room_id = client.post("/api/rooms", json={"host": "Alice"}).json()["room_id"]
        data = client.get(f"/api/rooms/{room_id}").json()
        assert "state" in data

    def test_response_has_host_field(self, client):
        room_id = client.post("/api/rooms", json={"host": "Alice"}).json()["room_id"]
        data = client.get(f"/api/rooms/{room_id}").json()
        assert data["host"] == "Alice"

    def test_response_has_all_required_fields(self, client):
        room_id = client.post("/api/rooms", json={"host": "Alice"}).json()["room_id"]
        data = client.get(f"/api/rooms/{room_id}").json()
        required = {"room_id", "state", "host", "players", "time_limit", "difficulty"}
        assert required.issubset(set(data.keys()))

    def test_players_starts_as_empty_list(self, client):
        room_id = client.post("/api/rooms", json={"host": "Alice"}).json()["room_id"]
        data = client.get(f"/api/rooms/{room_id}").json()
        assert data["players"] == []

    def test_nonexistent_room_returns_404(self, client):
        resp = client.get("/api/rooms/ZZZZZZ")
        assert resp.status_code == 404

    def test_nonexistent_room_response_has_error_field(self, client):
        data = client.get("/api/rooms/ZZZZZZ").json()
        assert "error" in data

    def test_unknown_room_id_returns_404(self, client):
        resp = client.get("/api/rooms/INVALID_ID_XYZ")
        assert resp.status_code == 404

    def test_time_limit_reflected_in_get(self, client):
        room_id = client.post(
            "/api/rooms", json={"host": "A", "time_limit": 60}
        ).json()["room_id"]
        data = client.get(f"/api/rooms/{room_id}").json()
        assert data["time_limit"] == 60

    def test_difficulty_none_when_not_set(self, client):
        room_id = client.post("/api/rooms", json={"host": "A"}).json()["room_id"]
        data = client.get(f"/api/rooms/{room_id}").json()
        assert data["difficulty"] is None


# ---------------------------------------------------------------------------
# GET /api/problems
# ---------------------------------------------------------------------------


class TestListProblemsEndpoint:
    def test_returns_200(self, client):
        assert client.get("/api/problems").status_code == 200

    def test_response_is_a_list(self, client):
        data = client.get("/api/problems").json()
        assert isinstance(data, list)

    def test_list_is_non_empty(self, client):
        data = client.get("/api/problems").json()
        assert len(data) > 0

    def test_entries_have_id(self, client):
        data = client.get("/api/problems").json()
        for entry in data[:5]:
            assert "id" in entry

    def test_entries_have_title(self, client):
        data = client.get("/api/problems").json()
        for entry in data[:5]:
            assert "title" in entry

    def test_entries_have_difficulty(self, client):
        data = client.get("/api/problems").json()
        for entry in data[:5]:
            assert "difficulty" in entry

    def test_two_sum_is_in_the_list(self, client):
        data = client.get("/api/problems").json()
        ids = [entry["id"] for entry in data]
        assert "two-sum" in ids


# ---------------------------------------------------------------------------
# Static HTML pages
# ---------------------------------------------------------------------------


class TestStaticPages:
    def test_index_returns_200(self, client):
        assert client.get("/").status_code == 200

    def test_index_returns_html(self, client):
        resp = client.get("/")
        assert "text/html" in resp.headers["content-type"]

    def test_room_page_returns_200(self, client):
        assert client.get("/room").status_code == 200

    def test_room_page_returns_html(self, client):
        resp = client.get("/room")
        assert "text/html" in resp.headers["content-type"]
