def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(
        [
            'candidate(s="abcda", queries=[[3, 3, 0], [1, 2, 0], [0, 3, 1]])',
            'candidate(s="a" * 100000, queries=[[i, 99999, 0] for i in range(100000)])',
        ]
    )
    for index in range(600):
        size = 1 + index % 80
        s = "".join(rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(size))
        count = min(size, 1 + index % 20)
        queries = []
        for _ in range(count):
            left = rng.randrange(size)
            right = rng.randrange(left, size)
            queries.append([left, right, rng.randrange(size + 1)])
        cases.add(f"candidate(s={s!r}, queries={queries!r})")
    while len(cases) < 600:
        s = "".join(
            rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(rng.randint(1, 50))
        )
        left = rng.randrange(len(s))
        right = rng.randrange(left, len(s))
        cases.add(
            f"candidate(s={s!r}, queries=[[{left}, {right}, {rng.randrange(len(s) + 1)}]])"
        )
    return sorted(cases)
