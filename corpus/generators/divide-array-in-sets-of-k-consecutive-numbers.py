import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases, seen = [], set()
    while len(cases) < 600:
        k = rng.randint(1, 8)
        groups = rng.randint(2, 10)
        nums = []
        for _ in range(groups):
            start = rng.randint(1, 100)
            nums.extend(range(start, start + k))
        if rng.random() < 0.5 and nums:
            nums.pop(rng.randrange(len(nums)))
        rng.shuffle(nums)
        key = (tuple(nums), k)
        if key not in seen:
            seen.add(key)
            assert 1 <= k <= max(1, len(nums)) and all(1 <= v <= 10**9 for v in nums)
            cases.append(f"candidate(nums={nums!r}, k={k})")
    return cases
