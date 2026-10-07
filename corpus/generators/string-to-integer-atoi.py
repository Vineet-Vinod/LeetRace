import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        "42",
        " -042",
        "1337c0d3",
        "0-1",
        "words and 987",
        "",
        "2147483648",
        "-2147483649",
    }
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 +-."
    while len(cases) < 600:
        cases.add("".join(rng.choice(alphabet) for _ in range(rng.randint(0, 200))))
    return [f"candidate(s={s!r})" for s in cases]
