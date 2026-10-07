import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {((1, 2, 3), 4), ((9,), 3)}
    while len(cases) < 600:
        nums = tuple(sorted(rng.sample(range(1, 20), rng.randint(1, 8))))
        target = rng.randint(1, 25)
        cases.add((nums, target))
    return [
        f"candidate(nums={list(nums)!r}, target={target})" for nums, target in cases
    ]
