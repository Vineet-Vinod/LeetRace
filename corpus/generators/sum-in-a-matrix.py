import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        rows = rng.randint(1, 30)
        cols = rng.randint(1, 30)
        nums = [[rng.randint(0, 1000) for _ in range(cols)] for _ in range(rows)]
        key = tuple(map(tuple, nums))
        if key not in seen:
            seen.add(key)
            assert all(
                len(row) == cols and all(0 <= v <= 1000 for v in row) for row in nums
            )
            cases.append(f"candidate(nums={nums!r})")
    return cases
