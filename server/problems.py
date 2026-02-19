"""Load and pick random problems from bundled JSON files."""

import json
import random
import re
from pathlib import Path

PROBLEMS_DIR = Path(__file__).resolve().parent.parent / "problems"

_index: list[dict] | None = None


def load_index() -> list[dict]:
    """Return the problem metadata list, caching on first load."""
    global _index
    if _index is None:
        index_path = PROBLEMS_DIR / "index.json"
        if not index_path.exists():
            return []
        _index = json.loads(index_path.read_text())
    return _index


def load_problem(problem_id: str) -> dict | None:
    """Return full problem data for a given id."""
    path = PROBLEMS_DIR / f"{problem_id}.json"
    if not path.exists():
        return None
    return json.loads(path.read_text())


def _has_valid_tests(problem: dict) -> bool:
    """Return True if the problem has at least one non-None test case."""
    test_cases = problem.get("test_cases", [])
    if not test_cases:
        return False
    # Reject problems where every assertion expects None (in-place mutation)
    for tc in test_cases:
        if not re.search(r"==\s*None\s*$", tc.strip()):
            return True
    return False


def pick_random(difficulty: str | None = None) -> dict | None:
    """Pick a random problem, optionally filtered by difficulty."""
    index = load_index()
    if not index:
        return None

    filtered = index
    if difficulty:
        filtered = [
            p for p in filtered if p["difficulty"].lower() == difficulty.lower()
        ]

    if not filtered:
        return None

    # Shuffle and pick the first problem with valid test cases
    candidates = filtered.copy()
    random.shuffle(candidates)
    for entry in candidates:
        problem = load_problem(entry["id"])
        if problem and _has_valid_tests(problem):
            return problem

    return None
