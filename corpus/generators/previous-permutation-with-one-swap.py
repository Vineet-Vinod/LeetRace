def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(arr=[3, 2, 1])",
        "candidate(arr=[1, 1, 5])",
        f"candidate(arr={list(range(1, 10001))!r})",
        f"candidate(arr={list(range(10000, 0, -1))!r})",
    }
    while len(cases) < 600:
        n = rng.randint(1, 500)
        arr = [rng.randint(1, 10_000) for _ in range(n)]
        if rng.random() < 0.5 and n > 1:
            arr.sort()
            arr[-1], arr[-2] = arr[-2], arr[-1]
        assert 1 <= len(arr) <= 10_000 and all(1 <= x <= 10_000 for x in arr)
        cases.add(f"candidate(arr={arr!r})")
    return sorted(cases)
