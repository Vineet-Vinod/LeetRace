def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        size = rng.randint(2, 100)
        nums = [rng.randint(1, 10**9) for _ in range(size)]
        pattern = [rng.randint(-1, 1) for _ in range(rng.randint(1, size - 1))]
        assert all(value in (-1, 0, 1) for value in pattern)
        cases.add(f"candidate(nums={nums!r}, pattern={pattern!r})")
    assert len(cases) >= 500
    return sorted(cases)[:600]
