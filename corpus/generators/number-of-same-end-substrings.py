def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(
        [
            'candidate(s="abcaab", queries=[[0, 0], [1, 4], [2, 5], [0, 5]])',
            'candidate(s="a" * 30000, queries=[[i % 30000, 29999] for i in range(30000)])',
        ]
    )
    for index in range(600):
        size = 2 + index % 200
        s = "".join(rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(size))
        queries = []
        for _ in range(1 + index % 20):
            left = rng.randrange(size)
            queries.append([left, rng.randrange(left, size)])
        cases.add(f"candidate(s={s!r}, queries={queries!r})")
    return sorted(cases)
