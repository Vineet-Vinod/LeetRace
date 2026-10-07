import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        nums = [rng.randint(1, 50000) for _ in range(rng.randint(1, 40))]
        total = len(nums) * (len(nums) + 1) // 2
        k = rng.randint(1, total)
        key = (tuple(nums), k)
        if key not in seen:
            seen.add(key)
            assert nums and all(1 <= v <= 50000 for v in nums) and 1 <= k <= total
            cases.append(f"candidate(nums={nums!r}, k={k})")
    return cases
