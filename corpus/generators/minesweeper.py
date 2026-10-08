def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        r, c = rng.randint(1, 15), rng.randint(1, 15)
        board = [[rng.choice(["E", "E", "E", "M"]) for _ in range(c)] for _ in range(r)]
        click = [rng.randrange(r), rng.randrange(c)]
        cases.add(f"candidate(board={board!r},click={click!r})")
    return sorted(cases)
