import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        n = rng.randint(1, 80)
        k = rng.randint(1, n)
        x = rng.randint(1, k)
        nums = [rng.randint(-50, 50) for _ in range(n)]
        key = (tuple(nums), k, x)
        if key not in seen:
            seen.add(key)
            assert 1 <= k <= n and 1 <= x <= k and all(-50 <= v <= 50 for v in nums)
            cases.append(f"candidate(nums={nums!r}, k={k}, x={x})")
    return cases
