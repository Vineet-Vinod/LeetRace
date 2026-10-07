import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {"a", "leet", "code", "z", "az", "za", "abcdefghijklmnopqrstuvwxyz"}
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    while len(cases) < 600:
        cases.add("".join(rng.choice(alphabet) for _ in range(rng.randint(1, 100))))
    return [f"candidate(target={target!r})" for target in cases]
