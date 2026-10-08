import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {(3, (0, 1), "RRDDLU"), (2, (1, 1), "LURD"), (1, (0, 0), "LRUD")}
    while len(cases) < 600:
        n = rng.randint(1, 30)
        start = (rng.randrange(n), rng.randrange(n))
        s = "".join(rng.choice("LRUD") for _ in range(rng.randint(1, 80)))
        cases.add((n, start, s))
    return [f"candidate(n={n}, startPos={list(pos)!r}, s={s!r})" for n, pos, s in cases]
