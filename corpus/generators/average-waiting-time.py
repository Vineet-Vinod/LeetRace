def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(customers=[[1,1]])"}
    while len(cases) < 600:
        n = rng.randint(1, 30)
        t = rng.randint(1, 20)
        rows = []
        for _ in range(n):
            t += rng.randint(0, 12)
            rows.append([t, rng.randint(1, 20)])
        cases.add(f"candidate(customers={rows!r})")
    return sorted(cases)
