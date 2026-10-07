import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {(), (40, 10, 20, 30), (100, 100, 100)}
    cases.add(tuple(rng.randint(-1_000_000_000, 1_000_000_000) for _ in range(100_000)))
    cases.add((-1_000_000_000,) * 50_000 + (1_000_000_000,) * 50_000)
    while len(cases) < 600:
        cases.add(
            tuple(
                rng.randint(-1_000_000_000, 1_000_000_000)
                for _ in range(rng.randint(1, 300))
            )
        )
    calls = [f"candidate(arr={list(values)!r})" for values in cases]
    calls.extend(["candidate(arr=[37, 12, 28, 9, 100, 56, 80, 5, 12])"])
    return list(dict.fromkeys(calls))
