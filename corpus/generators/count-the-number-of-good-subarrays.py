import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        ((1, 1, 1, 1, 1), 10),
        ((3, 1, 4, 3, 2, 2, 4), 2),
        ((1,), 1),
        ((1, 2, 3), 1),
    }
    cases.add((tuple([7] * 100000), 1))
    cases.add((tuple([7] * 100000), 10**9))
    while len(cases) < 600:
        length = rng.randint(2, 100)
        if rng.random() < 0.55:
            nums = tuple(rng.randint(1, 8) for _ in range(length))
            max_pairs = sum(
                v * (v - 1) // 2
                for v in __import__("collections").Counter(nums).values()
            )
            k = rng.randint(1, max(1, max_pairs))
        else:
            nums = tuple(rng.randint(1, 30) for _ in range(length))
            k = rng.randint(10000, 10**9)
        cases.add((nums, k))
    assert len(cases) == 600 and all(
        1 <= len(a) <= 100000 and 1 <= k <= 10**9 and all(1 <= v <= 10**9 for v in a)
        for a, k in cases
    )
    return [f"candidate(nums={list(a)!r}, k={k})" for a, k in sorted(cases)]
