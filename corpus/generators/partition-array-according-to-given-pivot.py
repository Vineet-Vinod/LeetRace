import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        nums = [rng.randint(-(10**6), 10**6) for _ in range(rng.randint(1, 80))]
        pivot = rng.choice(nums)
        key = (tuple(nums), pivot)
        if key not in seen:
            seen.add(key)
            assert pivot in nums and all(-(10**6) <= v <= 10**6 for v in nums)
            cases.append(f"candidate(nums={nums!r}, pivot={pivot})")
    return cases
