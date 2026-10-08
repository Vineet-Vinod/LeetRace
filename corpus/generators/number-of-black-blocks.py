def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(
        [
            "candidate(m=3, n=3, coordinates=[[0, 0]])",
            "candidate(m=100000, n=100000, coordinates=[[i // 100, i % 100] for i in range(10000)])",
            "candidate(m=100000, n=100000, coordinates=[[99999, 99999]])",
        ]
    )
    for index in range(600):
        m, n = 2 + index % 50, 2 + (index * 7) % 50
        if index == 0:
            m, n = 100000, 100000
        limit = min(10000, m * n)
        cells = rng.sample(range(m * n), min(limit, index % 100 + 1))
        coordinates = [[cell // n, cell % n] for cell in cells]
        cases.add(f"candidate(m={m}, n={n}, coordinates={coordinates!r})")
    return sorted(cases)
