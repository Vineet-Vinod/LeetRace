import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[tuple[int, int], ...], int]] = {
        (((1, 0),), 0),
        (((3, 50), (7, 10), (12, 25)), 10),
    }
    if "calculate-amount-paid-in-taxes" == "determine-color-of-a-chessboard-square":
        return [
            f"candidate(coordinates={chr(97 + col) + str(row)!r})"
            for col in range(8)
            for row in range(1, 9)
        ]
    if "calculate-amount-paid-in-taxes" == "smallest-even-multiple":
        return [f"candidate(n={value})" for value in range(1, 151)]
    cases.add((((1000, 100),), 1000))
    cases.add((tuple((bound, 100) for bound in range(10, 1001, 10)), 1000))
    while len(cases) < 600:
        count = rng.randint(1, 100)
        bounds: list[int] = []
        upper = 0
        for _ in range(count):
            upper += rng.randint(1, max(1, 1000 // count))
            bounds.append(min(upper, 1000))
        bounds = sorted(set(bounds))
        brackets = tuple((bound, rng.randint(0, 100)) for bound in bounds)
        income = rng.randint(0, bounds[-1])
        cases.add((brackets, income))
    calls = [
        f"candidate(brackets={[[u, p] for u, p in brackets]!r}, income={income})"
        for brackets, income in cases
    ]
    calls.extend(
        [
            "candidate(brackets=[[1, 0], [4, 25], [5, 50]], income=2)",
            "candidate(brackets=[[2, 50]], income=0)",
        ]
    )
    return list(dict.fromkeys(calls))
