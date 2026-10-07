import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {"12", "226", "06", "0", "10", "11106"}
    while len(cases) < 600:
        cases.add("".join(rng.choice("0123456789") for _ in range(rng.randint(1, 35))))
    return [f"candidate(s={s!r})" for s in cases]
