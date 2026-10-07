import random

EXAMPLES = [
    "candidate(n=3, maxDistance=5, roads=[[0, 1, 2], [1, 2, 10], [0, 2, 10]])",
    "candidate(n=3, maxDistance=5, roads=[[0, 1, 20], [0, 1, 10], [1, 2, 2], [0, 2, 2]])",
    "candidate(n=1, maxDistance=10, roads=[])",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = list(EXAMPLES)
    seen = set(calls)

    def emit(call: str) -> None:
        if call not in seen:
            calls.append(call)
            seen.add(call)

    def add(n, distance, roads):
        assert 1 <= n <= 10 and 1 <= distance <= 100000 and 0 <= len(roads) <= 1000
        assert all(
            len(row) == 3
            and 0 <= row[0] < n
            and 0 <= row[1] < n
            and row[0] != row[1]
            and 1 <= row[2] <= 1000
            for row in roads
        )
        reached = {0}
        while True:
            more = {v for u, v, _ in roads if u in reached} | {
                u for u, v, _ in roads if v in reached
            }
            if more <= reached:
                break
            reached |= more
        assert len(reached) == n
        emit(f"candidate(n={n}, maxDistance={distance}, roads={roads!r})")

    add(10, 100000, [[i % 10, (i + 1) % 10, 1000] for i in range(1000)])
    add(10, 1, [[i, i + 1, 1000] for i in range(9)])
    add(10, 100000, [[u, v, 1] for u in range(10) for v in range(u)])
    while len(calls) < 600:
        n = rng.randint(1, 7)
        roads = [[rng.randrange(v), v, rng.randint(1, 1000)] for v in range(1, n)]
        if n > 1:
            for _ in range(rng.randint(0, 15)):
                u, v = rng.sample(range(n), 2)
                roads.append([u, v, rng.randint(1, 1000)])
        add(n, rng.choice([1, 100000, rng.randint(1, 2000)]), roads)
    return calls
