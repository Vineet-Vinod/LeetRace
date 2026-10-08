def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(heights=[4, 2, 3, 1])",
        "candidate(heights=[4, 3, 2, 1])",
        "candidate(heights=[1, 3, 2, 4])",
        "candidate(heights=[5, 5, 5, 5])",
        f"candidate(heights={[7] * 100000!r})",
        f"candidate(heights={list(range(1, 100001))!r})",
        f"candidate(heights={list(range(100000, 0, -1))!r})",
        f"candidate(heights={[1000000000, 1, 1000000000]!r})",
    }
    while len(cases) < 600:
        heights = [rng.randint(1, 10**9) for _ in range(rng.randint(1, 100))]
        assert 1 <= len(heights) <= 100000
        assert all(1 <= height <= 10**9 for height in heights)
        cases.add(f"candidate(heights={heights!r})")
    assert len(cases) == 600
    return sorted(cases)
