"""Scoring and ranking for players."""

from __future__ import annotations

from server.rooms import Player


def rank_players(players: dict[str, Player]) -> list[dict]:
    """
    Rank players by:
    1. solved (True first)
    2. char_count (ascending — fewer chars = better)
    3. submit_time (ascending — faster = better)
    4. tests_passed (descending — more = better)

    Returns a list of dicts with position and player info.
    """
    entries = []
    for name, player in players.items():
        sub = player.submission
        if sub:
            entries.append({
                "name": name,
                "solved": sub.get("solved", False),
                "char_count": sub.get("char_count", 999999),
                "submit_time": sub.get("submit_time", 999999),
                "tests_passed": sub.get("passed", 0),
                "tests_total": sub.get("total", 0),
                "error": sub.get("error"),
            })
        else:
            entries.append({
                "name": name,
                "solved": False,
                "char_count": 999999,
                "submit_time": 999999,
                "tests_passed": 0,
                "tests_total": 0,
                "error": None,
            })

    entries.sort(key=lambda e: (
        not e["solved"],        # solved=True first
        e["char_count"],        # fewer chars better
        e["submit_time"],       # faster better
        -e["tests_passed"],     # more tests better
    ))

    for i, entry in enumerate(entries):
        entry["position"] = i + 1

    return entries
