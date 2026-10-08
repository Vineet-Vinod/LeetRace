import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        (1, 1, 8, 8, 2, 3),
        (5, 3, 3, 4, 5, 2),
        (1, 1, 1, 2, 8, 8),
        (8, 8, 1, 1, 8, 7),
    }
    while len(cases) < 600:
        squares = rng.sample(range(64), 3)
        pairs = [(s // 8 + 1, s % 8 + 1) for s in squares]
        cases.add(tuple(v for pair in pairs for v in pair))
    assert len(cases) == 600
    assert all(
        all(1 <= v <= 8 for v in case)
        and len({(case[i], case[i + 1]) for i in (0, 2, 4)}) == 3
        for case in cases
    )
    return [
        f"candidate(a={a}, b={b}, c={c}, d={d}, e={e}, f={f})"
        for a, b, c, d, e, f in sorted(cases)
    ]
