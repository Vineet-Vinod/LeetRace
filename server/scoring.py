"""Scoring and ranking for players."""

from __future__ import annotations

from server.rooms import Player


_NO_SUBMISSION: dict = {
    "solved": False,
    "char_count": float("inf"),
    "submit_time": float("inf"),
    "passed": 0,
    "total": 0,
    "error": None,
}


def rank_players(players: dict[str, Player]) -> list[dict]:
    """Rank players for the scoreboard.

    Sort order (best first):
      1. Solved (True before False)
      2. More tests passed (descending)
      3. Fewer characters (ascending, only meaningful when solved)
      4. Earlier lock-in time (ascending)

    Returns a list of dicts with ``position`` and player stats.
    """
    entries = []
    for name, player in players.items():
        sub = player.best_submission or _NO_SUBMISSION
        entries.append(
            {
                "name": name,
                "solved": sub.get("solved", False),
                "char_count": sub.get("char_count", float("inf")),
                "submit_time": sub.get("submit_time", float("inf")),
                "locked_at": player.locked_at,
                "tests_passed": sub.get("passed", 0),
                "tests_total": sub.get("total", 0),
                "error": sub.get("error"),
            }
        )

    entries.sort(
        key=lambda e: (
            not e["solved"],  # solved=True first
            -e["tests_passed"],  # more tests better
            e["char_count"]
            if e["solved"]
            else 0,  # fewer chars better (only matters when solved)
            e["locked_at"]
            if e["locked_at"] is not None
            else float("inf"),  # earlier lock wins
        )
    )

    for i, entry in enumerate(entries):
        entry["position"] = i + 1

    return entries
