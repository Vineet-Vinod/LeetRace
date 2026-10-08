def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(s='dcab',pairs=[[0,3],[1,2]])"}
    while len(cases) < 600:
        n = rng.randint(1, 100)
        s = "".join(rng.choice("abcdef") for _ in range(n))
        edges = [(a, b) for a in range(n) for b in range(a + 1, n)]
        rng.shuffle(edges)
        pairs = [list(edge) for edge in edges[: rng.randint(0, min(len(edges), 100))]]
        cases.add(f"candidate(s={s!r},pairs={pairs!r})")
    return sorted(cases)
