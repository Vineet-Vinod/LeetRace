def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(nums=[2,2,3,2])"}
    while len(cases) < 600:
        unique = rng.randint(-(2**31), 2**31 - 1)
        others = set()
        while len(others) < rng.randint(0, 15):
            others.add(rng.randint(-(2**31), 2**31 - 1))
        others.discard(unique)
        nums = [unique] + [value for item in others for value in (item, item, item)]
        rng.shuffle(nums)
        cases.add(f"candidate(nums={nums!r})")
    return sorted(cases)
