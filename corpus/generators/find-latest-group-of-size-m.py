def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    maximum = list(range(1, 100001))
    cases = {
        "candidate(arr=[1],m=1)",
        f"candidate(arr={maximum!r},m=100000)",
    }
    while len(cases) < 600:
        n = rng.randint(1, 100)
        arr = list(range(1, n + 1))
        rng.shuffle(arr)
        m = rng.choice([1, n, rng.randint(1, n)])
        assert 1 <= m <= len(arr) <= 100000
        assert sorted(arr) == list(range(1, n + 1))
        cases.add(f"candidate(arr={arr!r},m={m})")
    return sorted(cases)
