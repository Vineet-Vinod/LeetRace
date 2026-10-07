import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        n = rng.randint(1, 80)
        dominant = rng.randint(1, 10)
        count = rng.randint(n // 2 + 1, n)
        nums = [dominant] * count
        nums.extend(
            rng.choices([v for v in range(1, 11) if v != dominant], k=n - count)
        )
        rng.shuffle(nums)
        key = tuple(nums)
        if key not in seen:
            seen.add(key)
            assert nums.count(dominant) > n // 2 and len(nums) == n
            cases.append(f"candidate(nums={nums!r})")
    return cases
