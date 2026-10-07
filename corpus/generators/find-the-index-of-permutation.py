def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(["candidate(perm=[1, 2])", "candidate(perm=[3, 1, 2])"])
    for index in range(600):
        size = 1 + index % 100
        perm = list(range(1, size + 1))
        rng.shuffle(perm)
        cases.add(f"candidate(perm={perm!r})")
    while len(cases) < 600:
        perm = list(range(1, rng.randint(1, 100) + 1))
        rng.shuffle(perm)
        cases.add(f"candidate(perm={perm!r})")
    return sorted(cases)
