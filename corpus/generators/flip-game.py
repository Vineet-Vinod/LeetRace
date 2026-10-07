import random


def generate(seed: int = 0) -> list[str]:
    """Generate distinct valid cases: Strings over + and - with length at most 100."""
    rng = random.Random(seed)
    cases = {"+", "++", "+++", "++++", "----"}
    while len(cases) < 600:
        cases.add("".join(rng.choice("+-") for _ in range(rng.randint(1, 100))))
    return [f"candidate(currentState={s!r})" for s in cases]
