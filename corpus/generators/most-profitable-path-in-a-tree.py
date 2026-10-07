def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(
        [
            "candidate(edges=[[0, 1], [1, 2], [1, 3], [3, 4]], bob=3, amount=[-2, 4, 2, -4, 6])"
        ]
    )
    for index in range(600):
        n = 2 + index % 200
        if index == 0:
            n = 100000
        edges = [[node, rng.randrange(node)] for node in range(1, n)]
        bob = rng.randint(1, n - 1)
        amount = [2 * rng.randint(-5000, 5000) for _ in range(n)]
        cases.add(f"candidate(edges={edges!r}, bob={bob}, amount={amount!r})")
    return sorted(cases)
