def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(
        ["candidate(piles=[2, 4, 1, 2, 7, 8])", f"candidate(piles={[10000] * 99999!r})"]
    )
    for index in range(600):
        groups = 1 + index % 1000
        piles = [rng.randint(1, 10000) for _ in range(3 * groups)]
        cases.add(f"candidate(piles={piles!r})")
    return sorted(cases)
