import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    alphabet = string.ascii_uppercase[:8]
    while len(cases) < 600:
        s = "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 80)))
        k = rng.randint(0, len(s))
        key = (s, k)
        if key not in seen:
            seen.add(key)
            assert (
                1 <= len(s) <= 100000
                and 0 <= k <= len(s)
                and s.isupper()
                and s.isalpha()
            )
            cases.append(f"candidate(s={s!r}, k={k})")
    return cases
