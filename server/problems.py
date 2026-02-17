"""Load and pick random problems from bundled JSON files."""

import json
import random
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


EXCLUDED_TAGS = {"Tree", "Binary Tree", "Binary Search Tree", "Linked List"}


def pick_random(difficulty: str | None = None) -> dict | None:
    """Pick a random problem, optionally filtered by difficulty."""
    index = load_index()
    if not index:
        return None

    filtered = [p for p in index if not EXCLUDED_TAGS & set(p.get("tags", []))]

    if difficulty:
        filtered = [p for p in filtered if p["difficulty"].lower() == difficulty.lower()]

    if not filtered:
        return None

    choice = random.choice(filtered)
    return load_problem(choice["id"])
