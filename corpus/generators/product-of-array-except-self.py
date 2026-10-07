import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        nums = [rng.randint(-30, 30) for _ in range(rng.randint(2, 80))]
        key = tuple(nums)
        if key not in seen:
            seen.add(key)
            assert len(nums) >= 2 and all(-30 <= v <= 30 for v in nums)
            cases.append(f"candidate(nums={nums!r})")
    return cases
