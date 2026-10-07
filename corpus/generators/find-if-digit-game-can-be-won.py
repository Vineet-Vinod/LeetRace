import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {
        (1,),
        (10,),
        (1, 2, 3, 4, 10),
        (1, 2, 3, 4, 5, 14),
        (5, 5, 10),
    }
    while len(cases) < 600:
        if rng.randrange(2):
            target = rng.randint(1, 9) * 10
            singles: list[int] = []
            remaining = target
            while remaining:
                value = rng.randint(1, min(9, remaining))
                singles.append(value)
                remaining -= value
            values = tuple(singles + [10] * (target // 10))
        else:
            values = tuple(rng.randint(1, 99) for _ in range(rng.randint(1, 100)))
        cases.add(values)
    calls = [f"candidate(nums={list(nums)!r})" for nums in cases]
    calls.extend(["candidate(nums=[5, 5, 5, 25])"])
    return list(dict.fromkeys(calls))
