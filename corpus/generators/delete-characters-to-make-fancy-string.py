import random


def generate(seed: int = 0) -> list[str]:
    """Generate distinct valid cases: Nonempty lowercase strings of length at most 100000."""
    rng = random.Random(seed)
    cases = {"leeetcode", "aaabaaaa", "aab"}
    while len(cases) < 600:
        cases.add("".join(rng.choice("abc") for _ in range(rng.randint(1, 100))))
    return [f"candidate(s={s!r})" for s in cases]
