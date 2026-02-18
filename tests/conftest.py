"""Shared fixtures and configuration for all LeetRace tests."""

import pytest

import server.rooms as rooms_module
import server.problems as problems_module


@pytest.fixture(autouse=True)
def clear_rooms():
    """Clear the global rooms dict before and after each test."""
    rooms_module.rooms.clear()
    yield
    rooms_module.rooms.clear()


@pytest.fixture(autouse=True)
def clear_problems_cache():
    """Clear the problems index cache before each test so mocking works cleanly."""
    problems_module._index = None
    yield
    problems_module._index = None


@pytest.fixture
def client():
    from fastapi.testclient import TestClient
    from server.app import app

    with TestClient(app) as c:
        yield c
