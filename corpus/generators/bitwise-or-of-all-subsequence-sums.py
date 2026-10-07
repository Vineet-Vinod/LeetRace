import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases, seen = [], set()
    cases.extend(
        ["candidate(nums=[0])", "candidate(nums=[1])", "candidate(nums=[1, 2, 3])"]
    )
    seen.update({(0,), (1,), (1, 2, 3)})
    while len(cases) < 600:
        nums = [rng.randint(0, 1000) for _ in range(rng.randint(1, 16))]
        key = tuple(nums)
        if key not in seen:
            seen.add(key)
            assert len(nums) >= 1 and all(0 <= x <= 10**9 for x in nums)
            cases.append(f"candidate(nums={nums!r})")
    return cases
