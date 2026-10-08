import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[tuple[int, int], ...], tuple[tuple[int, int], ...]]] = {
        (((1, 1), (4, 5), (3, 8)), ((3, 1), (1, 5))),
        (((1, 3), (2, 2)), ((7, 1), (2, 2), (1, 4))),
    }
    cases.add(
        (
            tuple((value, 1000) for value in range(1, 1001)),
            tuple((value, 1000) for value in range(1, 1001)),
        )
    )
    while len(cases) < 600:
        first_values = rng.sample(range(1, 1001), rng.randint(1, 80))
        second_values = rng.sample(range(1, 1001), rng.randint(1, 80))
        first = tuple((value, rng.randint(1, 1000)) for value in first_values)
        second = tuple((value, rng.randint(1, 1000)) for value in second_values)
        cases.add((first, second))
    calls = [
        f"candidate(items1={[[v, w] for v, w in first]!r}, items2={[[v, w] for v, w in second]!r})"
        for first, second in cases
    ]
    calls.extend(
        ["candidate(items1=[[1, 1], [3, 2], [2, 3]], items2=[[2, 1], [3, 2], [1, 3]])"]
    )
    return list(dict.fromkeys(calls))
