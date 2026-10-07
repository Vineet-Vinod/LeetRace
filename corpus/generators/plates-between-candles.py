import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        ("**|**|***|", ((2, 5), (5, 9))),
        ("***|**|*****|**||**|*", ((1, 17), (4, 5), (14, 17), (5, 11), (15, 16))),
    }
    while len(cases) < 600:
        n = rng.randint(3, 100)
        s = "".join(rng.choice("*|") for _ in range(n))
        queries = tuple(
            (left := rng.randrange(n), rng.randint(left, n - 1))
            for _ in range(rng.randint(1, 30))
        )
        cases.add((s, queries))
    return [
        f"candidate(s={s!r}, queries={[list(q) for q in queries]!r})"
        for s, queries in cases
    ]
