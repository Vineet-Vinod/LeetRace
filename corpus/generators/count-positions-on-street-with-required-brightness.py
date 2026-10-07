def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(n=5, lights=[[0, 1], [2, 1], [3, 2]], requirement=[0, 2, 1, 4, 1])",
        "candidate(n=1, lights=[[0, 1]], requirement=[2])",
        f"candidate(n=100000, lights=[[0, 99999]], requirement={[0] * 50000 + [2] * 50000!r})",
        f"candidate(n=100000, lights={[[i, 0] for i in range(100000)]!r}, requirement={[0] * 100000!r})",
    }
    while len(cases) < 600:
        n = rng.randint(1, 80)
        lights = [[0, n - 1]]
        desired = rng.randint(0, n)
        requirement = [0] * desired + [2] * (n - desired)
        assert 1 <= n <= 100000 and 1 <= len(lights) <= 100000
        assert all(0 <= pos < n and 0 <= radius <= 100000 for pos, radius in lights)
        assert len(requirement) == n and all(
            0 <= value <= 100000 for value in requirement
        )
        cases.add(f"candidate(n={n}, lights={lights!r}, requirement={requirement!r})")
    return sorted(cases)
