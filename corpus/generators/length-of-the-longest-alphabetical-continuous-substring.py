import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        s = "".join(
            rng.choice(string.ascii_lowercase) for _ in range(rng.randint(1, 80))
        )
        if s not in seen:
            seen.add(s)
            assert s.islower() and s.isalpha() and 1 <= len(s) <= 100000
            cases.append(f"candidate(s={s!r})")
    return cases
