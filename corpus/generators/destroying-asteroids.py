def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases: set[str] = set()

    def add(mass: int, asteroids: list[int]) -> None:
        assert 1 <= mass <= 100_000
        assert 1 <= len(asteroids) <= 100_000
        assert all(1 <= value <= 100_000 for value in asteroids)
        cases.add(f"candidate(mass={mass}, asteroids={asteroids!r})")

    add(10, [3, 9, 19, 5, 21])
    add(5, [4, 9, 23, 4])
    add(1, [1] * 100_000)
    add(1, [100_000] * 100_000)
    add(100_000, [100_000])

    # Small asteroids allow growth; a single larger asteroid can force failure.
    for size in range(1, 301):
        add(1, [1] * size)
        add(1, [100_000] + [1] * (size - 1))

    while len(cases) < 600:
        size = rng.randint(1, 100)
        mass = rng.randint(1, 100_000)
        if rng.random() < 0.5:
            asteroids = [rng.randint(1, max(1, mass // 2)) for _ in range(size)]
        else:
            asteroids = [rng.randint(1, 100_000) for _ in range(size)]
        add(mass, asteroids)

    result = list(cases)
    rng.shuffle(result)
    return result
