import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases, seen = [], set()
    while len(cases) < 600:
        nums = [rng.randint(1, 100000) for _ in range(rng.randint(1, 80))]
        k = rng.randint(1, len(nums))
        key = (tuple(nums), k)
        if key not in seen:
            seen.add(key)
            assert 1 <= k <= len(nums) and all(1 <= x <= 10**5 for x in nums)
            cases.append(f"candidate(nums={nums!r}, k={k})")
    return cases
