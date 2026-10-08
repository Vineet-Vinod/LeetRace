def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {'candidate(time="19:34")', 'candidate(time="23:59")'}
    for _ in range(600):
        minutes = rng.randrange(24 * 60)
        time = f"{minutes // 60:02d}:{minutes % 60:02d}"
        cases.add(f"candidate(time={time!r})")
    while len(cases) < 600:
        minutes = rng.randrange(24 * 60)
        time = f"{minutes // 60:02d}:{minutes % 60:02d}"
        cases.add(f"candidate(time={time!r})")
    return sorted(cases)
