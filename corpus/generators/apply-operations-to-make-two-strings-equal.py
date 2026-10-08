import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases, seen = [], set()
    while len(cases) < 600:
        n = rng.randint(1, 80)
        x = rng.randint(1, 500)
        s1 = "".join(rng.choice("01") for _ in range(n))
        s2 = "".join(rng.choice("01") for _ in range(n))
        key = (s1, s2, x)
        if key not in seen:
            seen.add(key)
            assert len(s1) == len(s2) and set(s1 + s2) <= {"0", "1"}
            cases.append(f"candidate(s1={s1!r}, s2={s2!r}, x={x})")
    return cases
