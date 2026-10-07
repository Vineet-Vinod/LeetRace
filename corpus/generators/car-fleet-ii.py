import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**data) -> None:
        a = data["cars"]
        assert 1 <= len(a) <= 100000
        assert all(len(car) == 2 and all(1 <= x <= 1000000 for x in car) for car in a)
        assert all(a[i][0] < a[i + 1][0] for i in range(len(a) - 1))
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in data.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for example in [
        {"cars": [[1, 2], [2, 1], [4, 3], [7, 2]]},
        {"cars": [[3, 4], [5, 4], [6, 3], [9, 1]]},
    ]:
        add(**example)
    add(cars=[[i + 1, 1000000 - i] for i in range(100000)])
    add(cars=[[i + 1, 1] for i in range(100000)])
    add(cars=[[1, 1000000], [1000000, 1]])
    while len(calls) < 600:
        n = rng.randint(1, 60)
        positions = sorted(rng.sample(range(1, 1000001), n))
        speeds = [rng.randint(1, 1000000) for _ in range(n)]
        mode = len(calls) % 5
        if mode == 0:
            speeds.sort()
        if mode == 1:
            speeds.sort(reverse=True)
        if mode == 2:
            speeds = [rng.choice([1, 2, 3, 1000000]) for _ in range(n)]
        if mode == 3:
            speeds = [rng.randint(1, 1000000)] * n
        add(cars=[list(pair) for pair in zip(positions, speeds)])
    assert len(calls) == 600
    return calls
