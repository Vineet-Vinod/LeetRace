import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    alphabet = string.ascii_lowercase
    while len(cases) < 600:
        s = "".join(rng.choice(alphabet[:5]) for _ in range(rng.randint(3, 50)))
        if s not in seen:
            seen.add(s)
            assert 3 <= len(s) <= 50 and s.islower() and s.isalpha()
            cases.append(f"candidate(s={s!r})")
    return cases
