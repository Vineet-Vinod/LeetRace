import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = ["candidate(s='1'*100000)"]
    seen = {"1" * 100000}
    while len(cases) < 600:
        s = "".join(rng.choice("01") for _ in range(rng.randint(1, 100)))
        if s not in seen:
            seen.add(s)
            assert s and set(s) <= {"0", "1"}
            cases.append(f"candidate(s={s!r})")
    return cases
