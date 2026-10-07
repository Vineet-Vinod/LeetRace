def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(
        [
            "candidate(candidates=[2, 3, 6, 7], target=7)",
            "candidate(candidates=[2], target=1)",
            "candidate(candidates=[7, 3, 2, 6], target=7)",
            "candidate(candidates=list(range(2, 32)), target=1)",
        ]
    )
    for index in range(600):
        candidates = sorted(rng.sample(range(2, 41), rng.randint(1, 7)))
        target = rng.randint(1, 40)
        cases.add(f"candidate(candidates={candidates!r}, target={target})")
    while len(cases) < 600:
        candidates = sorted(rng.sample(range(2, 41), rng.randint(1, 6)))
        cases.add(f"candidate(candidates={candidates!r}, target={rng.randint(1, 40)})")
    return sorted(cases)
