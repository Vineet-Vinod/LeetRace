def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(limit=4, queries=[[1, 4], [2, 5], [1, 3], [3, 4]])",
        "candidate(limit=5, queries=[[0, 1], [1, 1], [0, 1], [0, 2], [1, 2], [1, 1], [0, 1], [0, 1], [2, 1], [1, 2]])",
        "candidate(limit=10, queries=[[0, 7], [1, 7], [2, 7], [3, 8], [0, 9], [3, 8], [1, 7], [2, 8], [0, 7]])",
        "candidate(limit=1000000000, queries=[[0, 1], [1000000000, 1000000000], [0, 2], [1000000000, 2], [0, 2]])",
    }

    queries = [[ball, ball % 3 + 1] for ball in range(100000)]
    assert len(queries) == 100000
    assert all(
        0 <= ball <= 1000000000 and 1 <= color <= 1000000000 for ball, color in queries
    )
    cases.add(f"candidate(limit=1000000000, queries={queries!r})")

    while len(cases) < 600:
        limit = rng.randint(1, 1000)
        ball_count = rng.randint(1, min(limit + 1, 15))
        balls = [rng.randint(0, limit) for _ in range(ball_count)]
        palette = [rng.randint(1, 5) for _ in range(rng.randint(1, 5))]
        queries = [[ball, rng.choice(palette)] for ball in balls]
        for _ in range(rng.randint(0, 10)):
            ball = rng.choice(balls)
            color = rng.choice(palette)
            queries.append([ball, color])
        assert 1 <= limit <= 10**9 and 1 <= len(queries) <= 10**5
        assert all(
            0 <= ball <= limit and 1 <= color <= 10**9 for ball, color in queries
        )
        cases.add(f"candidate(limit={limit}, queries={queries!r})")

    assert len(cases) == 600
    return sorted(cases)
