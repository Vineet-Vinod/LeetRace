import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        nums = [rng.randint(-(10**9), 10**9) for _ in range(rng.randint(2, 40))]
        target = rng.randint(0, 2 * 10**9)
        key = (tuple(nums), target)
        if key not in seen:
            seen.add(key)
            assert (
                len(nums) >= 2
                and all(-(10**9) <= v <= 10**9 for v in nums)
                and 0 <= target <= 2 * 10**9
            )
            cases.append(f"candidate(nums={nums!r}, target={target})")
    return cases
