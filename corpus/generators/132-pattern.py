import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = set()
    true_cases = {(-(10**9), 10**9, 0)}
    false_cases = {tuple(range(200000)), (0, 10**9)}
    while len(true_cases) < 300:
        n = rng.randint(3, 80)
        vals = [rng.randint(-1000, 1000) for _ in range(n)]
        base = rng.randint(-100000, 100000)
        vals[0], vals[1], vals[2] = base, base + 2, base + 1
        true_cases.add(tuple(vals))
    while len(false_cases) < 300:
        n = rng.randint(1, 100)
        start = rng.randint(-100000, 100000)
        vals = tuple(start + i for i in range(n))
        false_cases.add(vals)
    cases = true_cases | false_cases
    assert len(cases) == 600 and all(
        1 <= len(a) <= 200000 and all(-(10**9) <= v <= 10**9 for v in a) for a in cases
    )
    return [f"candidate(nums={list(a)!r})" for a in sorted(cases)]
