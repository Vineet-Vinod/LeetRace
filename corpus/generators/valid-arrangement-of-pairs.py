import random

EXAMPLES = [
    "candidate(pairs=[[5, 1], [4, 5], [11, 9], [9, 4]])",
    "candidate(pairs=[[1, 3], [3, 2], [2, 1]])",
    "candidate(pairs=[[1, 2], [1, 3], [2, 1]])",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = list(EXAMPLES)
    seen = set(calls)

    def emit(call: str) -> None:
        if call not in seen:
            calls.append(call)
            seen.add(call)

    def add(pairs):
        assert 1 <= len(pairs) <= 100000 and len({tuple(p) for p in pairs}) == len(
            pairs
        )
        assert all(
            len(p) == 2 and 0 <= p[0] <= 10**9 and 0 <= p[1] <= 10**9 and p[0] != p[1]
            for p in pairs
        )
        # Constructed consecutive trails prove an arrangement exists.
        emit(f"candidate(pairs={pairs!r})")

    add([[i, i + 1] for i in range(100000)])
    add([[10**9, 0]])
    while len(calls) < 600:
        count = rng.randint(1, 35)
        vertices = rng.sample(range(200), rng.randint(3, 15))
        path = [rng.choice(vertices)]
        used = set()
        for _ in range(count):
            options = [
                v for v in vertices if v != path[-1] and (path[-1], v) not in used
            ]
            if not options:
                break
            v = rng.choice(options)
            used.add((path[-1], v))
            path.append(v)
        pairs = [path[i : i + 2] for i in range(len(path) - 1)]
        rng.shuffle(pairs)
        add(pairs)
    return calls
