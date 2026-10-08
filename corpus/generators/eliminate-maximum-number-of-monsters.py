def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases: set[str] = set()

    def add(dist: list[int], speed: list[int]) -> None:
        assert 1 <= len(dist) == len(speed) <= 100_000
        assert all(1 <= value <= 100_000 for value in dist)
        assert all(1 <= value <= 100_000 for value in speed)
        cases.add(f"candidate(dist={dist!r}, speed={speed!r})")

    add([1, 3, 4], [1, 1, 1])
    add([100_000], [100_000])
    add([1, 1, 2, 3], [1, 1, 1, 1])
    add([3, 2, 4], [5, 3, 2])
    add(list(range(1, 100_001)), [1] * 100_000)

    # Arrival deadlines 1, ..., q followed by another q cause exactly q kills.
    for kills in range(1, 301):
        n = 301
        deadlines = list(range(1, kills + 1)) + [kills] * (n - kills)
        add(deadlines, [1] * n)

    # Distinct increasing deadlines guarantee every monster can be eliminated.
    for n in range(1, 301):
        add(list(range(1, n + 1)), [1] * n)

    # Randomized arrival deadlines with varied speeds cover exact and fractional
    # minute boundaries while respecting the maximum distance and speed.
    while len(cases) < 600:
        size = rng.randint(1, 100)
        deadlines = sorted(rng.randint(1, size + 1) for _ in range(size))
        speed = [rng.randint(1, 100) for _ in range(size)]
        dist = [
            (deadline - 1) * velocity + 1
            for deadline, velocity in zip(deadlines, speed)
        ]
        if max(dist) > 100_000:
            speed = [1] * size
            dist = deadlines
        add(dist, speed)

    result = list(cases)
    rng.shuffle(result)
    return result
