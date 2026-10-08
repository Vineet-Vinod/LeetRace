import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        ((3, 2, 2, 4, 3), 3),
        ((7, 3, 4, 7), 7),
        ((4, 3, 2, 6, 2, 3, 4), 6),
        ((1, 1), 1),
    }
    cases.add((tuple([1] * 100000), 2))
    cases.add((tuple([1000] * 100000), 10**8))
    while len(cases) < 600:
        if rng.random() < 0.55:
            left = [rng.randint(1, 30) for _ in range(rng.randint(1, 6))]
            right = [rng.randint(1, 30) for _ in range(rng.randint(1, 6))]
            target = max(sum(left), sum(right))
            # Grow the shorter planted segment to target, retaining positive values.
            if sum(left) < target:
                left[-1] += target - sum(left)
            if sum(right) < target:
                right[-1] += target - sum(right)
            arr = tuple(left + [rng.randint(1, 5)] + right)
        else:
            arr = tuple(rng.randint(1, 1000) for _ in range(rng.randint(1, 100)))
            target = rng.randint(sum(arr) + 1, 10**8)
        cases.add((arr, target))
    assert len(cases) == 600 and all(
        1 <= len(a) <= 100000 and 1 <= t <= 10**8 and all(1 <= v <= 1000 for v in a)
        for a, t in cases
    )
    return [f"candidate(arr={list(a)!r}, target={t})" for a, t in sorted(cases)]
