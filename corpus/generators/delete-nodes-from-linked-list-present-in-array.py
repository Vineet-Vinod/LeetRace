import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        ((1, 2, 3), (1, 2, 3, 4, 5)),
        ((1,), (1, 2, 1, 2, 1, 2)),
        ((5,), (1, 2, 3, 4)),
    }
    while len(cases) < 600:
        n = rng.randint(1, 80)
        values = tuple(rng.randint(1, 100) for _ in range(n))
        removed = tuple(rng.sample(range(1, 101), rng.randint(1, 20)))
        if any(value not in removed for value in values):
            cases.add((removed, values))
    return [
        f"candidate(nums={list(nums)!r}, head=list_node({list(values)!r}) )"
        for nums, values in cases
    ]
