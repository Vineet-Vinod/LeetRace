def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(boxGrid=[['#', '.', '#']])",
        "candidate(boxGrid=[['#', '.', '*', '.'], ['#', '#', '*', '.']])",
        "candidate(boxGrid=[['#'] * 500])",
        f"candidate(boxGrid={[[rng.choice('#*.') for _ in range(500)] for _ in range(500)]!r})",
    }
    while len(cases) < 600:
        m, n = rng.randint(1, 12), rng.randint(1, 12)
        grid = [[rng.choice("#*.") for _ in range(n)] for _ in range(m)]
        # Any row is valid: gravity settles stones during the rotation.
        assert (
            1 <= m <= 500
            and 1 <= n <= 500
            and all(c in "#*." for row in grid for c in row)
        )
        cases.add(f"candidate(boxGrid={grid!r})")
    return sorted(cases)
