import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        m = rng.randint(1, 30)
        n = rng.randint(1, 30)
        start = [rng.randrange(m), rng.randrange(n)]
        home = [rng.randrange(m), rng.randrange(n)]
        rows = [rng.randint(0, 10000) for _ in range(m)]
        cols = [rng.randint(0, 10000) for _ in range(n)]
        key = (tuple(start), tuple(home), tuple(rows), tuple(cols))
        if key not in seen:
            seen.add(key)
            assert (
                0 <= start[0] < m
                and 0 <= home[0] < m
                and 0 <= start[1] < n
                and 0 <= home[1] < n
            )
            cases.append(
                f"candidate(startPos={start!r}, homePos={home!r}, rowCosts={rows!r}, colCosts={cols!r})"
            )
    return cases
