def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(flips=[3, 2, 4, 1, 5])",
        "candidate(flips=[4, 1, 2, 3])",
        f"candidate(flips={list(range(1, 50001))!r})",
        f"candidate(flips={list(range(50000, 0, -1))!r})",
    }
    while len(cases) < 600:
        n = rng.randint(1, 1000)
        aligned = rng.randint(1, n)
        if aligned == n:
            flips = list(range(1, n + 1))
        else:
            flips = list(range(1, aligned)) + list(range(n, aligned - 1, -1))
        assert 1 <= len(flips) <= 50000 and sorted(flips) == list(
            range(1, len(flips) + 1)
        )
        cases.add(f"candidate(flips={flips!r})")
    return sorted(cases)
