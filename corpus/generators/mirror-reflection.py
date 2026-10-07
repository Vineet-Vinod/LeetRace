def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(["candidate(p=2, q=1)", "candidate(p=3, q=1)"])
    for index in range(600):
        p = 1 + index % 1000
        q = rng.randint(1, p)
        cases.add(f"candidate(p={p}, q={q})")
    return sorted(cases)
