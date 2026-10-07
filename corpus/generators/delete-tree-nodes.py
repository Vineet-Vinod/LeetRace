def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(1, 40)
        parent = [-1] + [rng.randrange(i) for i in range(1, n)]
        vals = [rng.randint(-10, 10) for _ in range(n)]
        cases.add(f"candidate(nodes={n},parent={parent!r},value={vals!r})")
    return sorted(cases)
