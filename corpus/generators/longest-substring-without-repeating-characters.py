import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    alphabet = string.ascii_letters + string.digits + " !?@#$%^&*()"
    cases.append("candidate(s='')")
    seen.add("")
    while len(cases) < 600:
        s = "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 100)))
        if s not in seen:
            seen.add(s)
            assert len(s) <= 50000
            cases.append(f"candidate(s={s!r})")
    return cases
