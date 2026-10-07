def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(["candidate(milestones=[1, 2, 3])", "candidate(milestones=[5, 2, 1])"])
    for index in range(600):
        size = 1 + index % 100
        if index == 0:
            size = 100000
        milestones = [rng.randint(1, 10**9) for _ in range(size)]
        cases.add(f"candidate(milestones={milestones!r})")
    return sorted(cases)
