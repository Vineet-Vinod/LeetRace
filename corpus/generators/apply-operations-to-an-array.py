import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {(0, 0), (0, 1), (1, 1), (1, 1, 1), (1000, 1000)}
    if "apply-operations-to-an-array" == "determine-color-of-a-chessboard-square":
        return [
            f"candidate(coordinates={chr(97 + col) + str(row)!r})"
            for col in range(8)
            for row in range(1, 9)
        ]
    if "apply-operations-to-an-array" == "smallest-even-multiple":
        return [f"candidate(n={value})" for value in range(1, 151)]
    cases.add((0,) * 2000)
    cases.add((1000,) * 2000)
    while len(cases) < 600:
        size = rng.randint(2, 100)
        values = tuple(rng.randint(0, 1000) for _ in range(size))
        cases.add(values)
    calls = [f"candidate(nums={list(values)!r})" for values in cases]
    calls.extend(["candidate(nums=[1, 2, 2, 1, 1, 0])"])
    return list(dict.fromkeys(calls))
