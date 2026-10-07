import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, int], ...]] = {
        (
            (1, 3),
            (2, 3),
            (3, 6),
            (5, 6),
            (5, 7),
            (4, 5),
            (4, 8),
            (4, 9),
            (10, 4),
            (10, 9),
        ),
        ((2, 3), (1, 3), (5, 4), (6, 4)),
    }
    cases.add(
        tuple((player, player + 1) for player in range(1, 100_000)) + ((100_000, 1),)
    )
    while len(cases) < 600:
        players = rng.randint(2, 30)
        matches = set()
        for _ in range(rng.randint(1, min(100, players * (players - 1)))):
            winner, loser = rng.sample(range(1, 100_001), 2)
            matches.add((winner, loser))
        cases.add(tuple(sorted(matches)))
    assert all(
        1 <= len(matches) <= 100_000
        and len(set(matches)) == len(matches)
        and all(
            1 <= winner <= 100_000 and 1 <= loser <= 100_000 and winner != loser
            for winner, loser in matches
        )
        for matches in cases
    )
    return [
        f"candidate(matches={[[a, b] for a, b in matches]!r})"
        for matches in sorted(cases)
    ]
