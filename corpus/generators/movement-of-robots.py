import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {((-2, 0, 2), "RLL", 3), ((1, 0), "RL", 2)}
    while len(cases) < 600:
        n = rng.randint(2, 100)
        nums = tuple(rng.sample(range(-(10**9), 10**9 + 1), n))
        direction = "".join(rng.choice("LR") for _ in range(n))
        cases.add((nums, direction, rng.randint(0, 10**9)))
    return [f"candidate(nums={list(nums)!r}, s={s!r}, d={d})" for nums, s, d in cases]
