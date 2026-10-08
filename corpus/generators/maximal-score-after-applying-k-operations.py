import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        nums = [rng.randint(1, 10**9) for _ in range(rng.randint(1, 60))]
        k = rng.randint(1, 100000)
        key = (tuple(nums), k)
        if key not in seen:
            seen.add(key)
            assert nums and all(1 <= v <= 10**9 for v in nums) and 1 <= k <= 100000
            cases.append(f"candidate(nums={nums!r}, k={k})")
    return cases
