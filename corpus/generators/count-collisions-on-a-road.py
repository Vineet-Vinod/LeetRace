import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {"RLRSLL", "LLRR", "S", "R", "L"}
    while len(cases) < 600:
        cases.add("".join(rng.choice("LRS") for _ in range(rng.randint(1, 100))))
    return [f"candidate(directions={directions!r})" for directions in cases]
