import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases, seen = [], set()
    alphabet = string.ascii_lowercase
    while len(cases) < 600:
        a = "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 80)))
        b = "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 80)))
        key = (a, b)
        if key not in seen:
            seen.add(key)
            assert a.islower() and b.islower() and a.isalpha() and b.isalpha()
            cases.append(f"candidate(a={a!r}, b={b!r})")
    return cases
