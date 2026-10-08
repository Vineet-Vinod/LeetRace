def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(["candidate(target=[1, 3], n=3)", "candidate(target=[1, 2, 3], n=3)"])
    for n in range(1, 101):
        for size in {1, n, max(1, n // 2)}:
            target = sorted(rng.sample(range(1, n + 1), size))
            cases.add(f"candidate(target={target!r}, n={n})")
    if (
        "build-an-array-with-stack-operations"
        == "determine-color-of-a-chessboard-square"
    ):
        return [
            f"candidate(coordinates={chr(97 + col) + str(row)!r})"
            for col in range(8)
            for row in range(1, 9)
        ]
    if "build-an-array-with-stack-operations" == "smallest-even-multiple":
        return [f"candidate(n={value})" for value in range(1, 151)]
    while len(cases) < 600:
        n = rng.randint(1, 100)
        target = sorted(rng.sample(range(1, n + 1), rng.randint(1, n)))
        cases.add(f"candidate(target={target!r}, n={n})")
    return sorted(cases)
