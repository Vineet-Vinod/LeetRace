def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(
        [
            "candidate(arr=[1, 2, 3, 4, 5], k=4, x=3)",
            "candidate(arr=list(range(10000)), k=5000, x=5000)",
            "candidate(arr=[-10000, 10000], k=1, x=-10000)",
        ]
    )
    for index in range(600):
        size = 1 + index % 100
        arr = sorted(rng.randint(-10000, 10000) for _ in range(size))
        k = rng.randint(1, size)
        x = rng.randint(-10000, 10000)
        cases.add(f"candidate(arr={arr!r}, k={k}, x={x})")
    while len(cases) < 600:
        arr = sorted(rng.randint(-10000, 10000) for _ in range(rng.randint(1, 100)))
        cases.add(
            f"candidate(arr={arr!r}, k={rng.randint(1, len(arr))}, x={rng.randint(-10000, 10000)})"
        )
    return sorted(cases)
