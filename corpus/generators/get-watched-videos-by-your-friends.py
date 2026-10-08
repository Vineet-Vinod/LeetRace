import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        (
            (("A", "B"), ("C",), ("B", "C"), ("D",)),
            ((1, 2), (0, 3), (0, 3), (1, 2)),
            0,
            1,
        )
    }
    while len(cases) < 600:
        n = rng.randint(2, 40)
        links = {
            (i, j) for i in range(n) for j in range(i + 1, n) if rng.random() < 0.1
        }
        friends = [set() for _ in range(n)]
        for i, j in links:
            friends[i].add(j)
            friends[j].add(i)
        videos = tuple(
            tuple(f"V{rng.randint(0, 20)}" for _ in range(rng.randint(1, 8)))
            for _ in range(n)
        )
        cases.add(
            (
                videos,
                tuple(tuple(sorted(row)) for row in friends),
                rng.randrange(n),
                rng.randint(1, n - 1),
            )
        )
    return [
        f"candidate(watchedVideos={[list(v) for v in videos]!r}, friends={[list(row) for row in friends]!r}, id={person}, level={level})"
        for videos, friends, person, level in cases
    ]
