def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(arr=[3, 3, 3, 3, 5, 5, 5, 2, 2, 7])",
        f"candidate(arr={[1] * 50000 + [2] * 50000!r})",
    }
    while len(cases) < 600:
        n = 2 * rng.randint(1, 500)
        mode = rng.randrange(3)
        if mode == 0:
            arr = [rng.randint(1, 20) for _ in range(n)]
        elif mode == 1:
            arr = [i % max(1, n // 10) + 1 for i in range(n)]
        else:
            arr = [rng.randint(1, 100_000) for _ in range(n)]
        assert 2 <= len(arr) <= 100_000 and len(arr) % 2 == 0
        assert all(1 <= value <= 100_000 for value in arr)
        cases.add(f"candidate(arr={arr!r})")
    return sorted(cases)
