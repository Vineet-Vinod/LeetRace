def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(
        [
            'candidate(n=7, edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], labels="abaedcd")'
        ]
    )
    for index in range(600):
        n = 100000 if index == 0 else 1 + index % 300
        edges = [[node, rng.randrange(node)] for node in range(1, n)]
        labels = "".join(rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(n))
        cases.add(f"candidate(n={n}, edges={edges!r}, labels={labels!r})")
    return sorted(cases)
