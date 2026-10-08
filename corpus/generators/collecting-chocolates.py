import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases, seen = [], set()
    while len(cases) < 600:
        nums = [rng.randint(1, 1000) for _ in range(rng.randint(1, 25))]
        x = rng.randint(1, 1000)
        key = (tuple(nums), x)
        if key not in seen:
            seen.add(key)
            assert nums and all(v > 0 for v in nums)
            cases.append(f"candidate(nums={nums!r}, x={x})")
    return cases
