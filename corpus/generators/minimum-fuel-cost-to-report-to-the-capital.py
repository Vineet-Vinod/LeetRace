def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(
        [
            "candidate(roads=[[0, 1], [0, 2], [0, 3]], seats=5)",
            "candidate(roads=[], seats=1)",
        ]
    )
    for index in range(600):
        n = 1 + index % 1000
        if index == 0:
            n = 100000
        roads = [[node, rng.randrange(node)] for node in range(1, n)]
        seats = rng.randint(1, 100000)
        cases.add(f"candidate(roads={roads!r}, seats={seats})")
    return sorted(cases)
