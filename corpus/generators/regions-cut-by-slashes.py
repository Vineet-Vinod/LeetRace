import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    backslash = chr(92)
    cases = {(" /", "/ "), (" /", "  "), ("/" + backslash, backslash + "/")}
    alphabet = "/" + backslash + " "
    while len(cases) < 600:
        n = rng.randint(1, 15)
        cases.add(
            tuple("".join(rng.choice(alphabet) for _ in range(n)) for _ in range(n))
        )
    return [f"candidate(grid={list(grid)!r})" for grid in cases]
