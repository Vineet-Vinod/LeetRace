import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**data) -> None:
        a, r = data["darts"], data["r"]
        assert 1 <= len(a) <= 100 and 1 <= r <= 5000
        assert all(len(p) == 2 and all(-10000 <= x <= 10000 for x in p) for p in a)
        assert len({tuple(p) for p in a}) == len(a)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in data.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for example in [
        {"darts": [[-2, 0], [2, 0], [0, 2], [0, -2]], "r": 2},
        {"darts": [[-3, 0], [3, 0], [2, 6], [5, 4], [0, 9], [7, 8]], "r": 5},
    ]:
        add(**example)
    add(darts=[[-10000, -10000], [10000, 10000]], r=5000)
    add(darts=[[i, 0] for i in range(100)], r=50)
    add(darts=[[i * 100 - 5000, 0] for i in range(100)], r=5000)
    add(darts=[[-5000, 0], [5000, 0], [0, -5000], [0, 5000]], r=5000)
    while len(calls) < 600:
        n = rng.randint(1, 18)
        r = rng.choice([1, 2, 3, 5, 10, 5000])
        mode = len(calls) % 3
        bound = 10000 if mode == 0 else max(3, min(50, r))
        points = set()
        while len(points) < n:
            points.add((rng.randint(-bound, bound), rng.randint(-bound, bound)))
        add(darts=[list(p) for p in sorted(points)], r=r)
    assert len(calls) == 600
    return calls
