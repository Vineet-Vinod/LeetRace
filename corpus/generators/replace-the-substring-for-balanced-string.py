import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {"QWER", "QQWE", "QQQW"}
    while len(cases) < 600:
        n = 4 * rng.randint(1, 25)
        cases.add("".join(rng.choice("QWER") for _ in range(n)))
    return [f"candidate(s={s!r})" for s in cases]
