import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    true_cases = {
        ((4, 2, 3, 0, 3, 1, 2), 5),
        ((4, 2, 3, 0, 3, 1, 2), 0),
        ((3, 0, 2, 1, 2), 2),
        ((0,), 0),
    }
    true_cases.add((tuple([0] * 50_000), 0))
    while len(true_cases) < 300:
        n = rng.randint(2, 80)
        start = rng.randrange(n - 1)
        arr = [rng.randrange(n) for _ in range(n)]
        arr[start] = n - 1 - start
        arr[-1] = 0
        true_cases.add((tuple(arr), start))
    false_cases = set()
    while len(false_cases) < 300:
        n = rng.randint(2, 80)
        arr = [rng.randrange(n) for _ in range(n)]
        arr[-1] = n - 1
        false_cases.add((tuple(arr), n - 1))
    cases = true_cases | false_cases
    assert len(cases) == 600 and all(
        1 <= len(a) <= 50000 and 0 <= s < len(a) and all(0 <= v < len(a) for v in a)
        for a, s in cases
    )
    return [f"candidate(arr={list(a)!r}, start={s})" for a, s in sorted(cases)]
