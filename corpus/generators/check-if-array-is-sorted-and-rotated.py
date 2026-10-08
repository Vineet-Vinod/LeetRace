import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {
        (1,),
        (1, 2, 3),
        (3, 1, 2),
        (2, 1, 3),
        (1, 1, 1),
        tuple(range(1, 101)),
        (100,) * 100,
    }
    while len(cases) < 600:
        if rng.randrange(2):
            size = rng.randint(1, 100)
            sorted_values = sorted(rng.randint(1, 100) for _ in range(size))
            offset = rng.randrange(size)
            values = tuple(sorted_values[offset:] + sorted_values[:offset])
        else:
            values = tuple(rng.randint(1, 100) for _ in range(rng.randint(1, 100)))
        cases.add(values)
    calls = [f"candidate(nums={list(values)!r})" for values in cases]
    calls.extend(["candidate(nums=[3, 4, 5, 1, 2])", "candidate(nums=[2, 1, 3, 4])"])
    return list(dict.fromkeys(calls))
