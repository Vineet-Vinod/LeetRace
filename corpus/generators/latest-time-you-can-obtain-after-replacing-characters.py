import random


def generate(seed: int = 0) -> list[str]:
    """Generate distinct valid cases: Valid 12-hour times with wildcards only at digit positions."""
    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        hh = f"{rng.randrange(12):02d}"
        mm = f"{rng.randrange(60):02d}"
        valid = hh + ":" + mm
        chars = list(valid)
        for i in range(5):
            if i != 2 and rng.random() < 0.55:
                chars[i] = "?"
        cases.add("".join(chars))
    cases.update({"??:??", "?1:??", "1?:?9"})
    return [f"candidate(s={s!r})" for s in cases]
