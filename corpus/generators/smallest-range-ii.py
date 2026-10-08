import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {((1,), 0), ((0, 10), 2), ((1, 3, 6), 3)}
    while len(cases) < 600:
        cases.add(
            (
                tuple(rng.randint(0, 10000) for _ in range(rng.randint(1, 100))),
                rng.randint(0, 10000),
            )
        )
    return [f"candidate(nums={list(nums)!r}, k={k})" for nums, k in cases]
