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
    # code is absent from the sentinel so the .get() below yields None,
    # which the frontend interprets as "no submission".
}


def rank_players(
    players: dict[str, Player], include_code: bool = False
) -> list[dict]:
    """Rank players for the scoreboard.

    Sort order (best first):
      1. Solved (True before False)
      2. More tests passed (descending)
      3. Fewer characters (ascending, only meaningful when solved)
      4. Earlier lock-in time (ascending)

    Args:
        players: Map of player name to Player instance.
        include_code: If True, include the ``code`` field from each player's
            best submission. Only pass True for end-of-game payloads — live
            scoreboard updates during gameplay must NOT leak opponent code.

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
                # Only include code in end-of-game payloads so opponents
                # cannot inspect WebSocket messages mid-game to cheat.
                "code": sub.get("code") if include_code else None,
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
