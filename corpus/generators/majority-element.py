import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {(3, 2, 3), (2, 2, 1, 1, 1, 2, 2)}
    cases.add((1_000_000_000,) * 25_001 + (-1_000_000_000,) * 24_999)
    while len(cases) < 600:
        size = rng.randint(1, 500)
        majority = rng.randint(-1_000_000_000, 1_000_000_000)
        count = rng.randint(size // 2 + 1, size)
        values = [majority] * count
        while len(values) < size:
            value = rng.randint(-1_000_000_000, 1_000_000_000)
            if value != majority:
                values.append(value)
        rng.shuffle(values)
        cases.add(tuple(values))
    return [f"candidate(nums={list(nums)!r})" for nums in cases]
