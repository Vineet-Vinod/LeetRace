import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], int, int]] = {
        ((1,), 1, 1),
        (tuple(range(1, 14)), 2, 3),
    }
    cases.add((tuple(range(1, 10_000)) + (1_000_000,), 1000, 1000))
    while len(cases) < 600:
        size = rng.randint(1, 1000)
        values = tuple(rng.randint(1, 1_000_000) for _ in range(size))
        cases.add((values, rng.randint(1, 1000), rng.randint(1, 1000)))
    calls = [
        f"candidate(head=list_node({list(values)!r}), m={m}, n={n})"
        for values, m, n in cases
    ]
    calls.extend(
        [
            "candidate(head=list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), m=2, n=3)",
            "candidate(head=list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), m=1, n=3)",
        ]
    )
    return list(dict.fromkeys(calls))
