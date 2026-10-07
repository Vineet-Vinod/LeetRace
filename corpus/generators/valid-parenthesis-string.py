import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = {
        "(",
        ")",
        "*",
        "()",
        "(*)",
        "(*))",
        "(" * 50 + "*" * 50,
        "(" * 100,
        ")" * 100,
        "*" * 100,
    }
    while len(cases) < 600:
        size = rng.randint(1, 100)
        mode = rng.randrange(3)
        if mode == 0:
            depth = rng.randint(0, size // 2)
            value = "(" * depth + "*" * (size - 2 * depth) + ")" * depth
        elif mode == 1:
            value = "".join(rng.choice("(*") for _ in range(size))
        else:
            value = "".join(rng.choice("()*") for _ in range(size))
        cases.add(value)
    assert all(1 <= len(s) <= 100 and set(s) <= set("()*") for s in cases)
    return [f"candidate(s={s!r})" for s in sorted(cases)]
