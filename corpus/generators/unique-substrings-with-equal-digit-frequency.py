import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {"1212", "12321"}
    while len(cases) < 600:
        cases.add("".join(rng.choice("0123456789") for _ in range(rng.randint(1, 100))))
    cases.update({"0123456789" * 100})
    return [f"candidate(s={s!r})" for s in cases]
