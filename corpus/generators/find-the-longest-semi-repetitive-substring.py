import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        s = "".join(rng.choice("0123456789") for _ in range(rng.randint(1, 50)))
        if s not in seen:
            seen.add(s)
            assert 1 <= len(s) <= 50 and all(c in "0123456789" for c in s)
            cases.append(f"candidate(s={s!r})")
    return cases
