import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {(("3", "6", "7", "10"), 4), (("2", "21", "12", "1"), 3), (("0", "0"), 2)}
    while len(cases) < 600:
        n = rng.randint(1, 100)
        nums = tuple(
            str(rng.randint(0, 10**30))
            if rng.random() < 0.6
            else str(rng.randint(0, 10**90))
            for _ in range(n)
        )
        cases.add((nums, rng.randint(1, n)))
    return [f"candidate(nums={list(nums)!r}, k={k})" for nums, k in cases]
