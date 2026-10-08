def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    for _ in range(599):
        arr = [rng.randint(1, 30000) for _ in range(rng.randint(1, 100))]
        cases.add(f"candidate(arr={arr!r})")
    boundary = [rng.randint(1, 30000) for _ in range(30000)]
    cases.add(f"candidate(arr={boundary!r})")
    assert len(cases) >= 500
    return sorted(cases)[:600]
