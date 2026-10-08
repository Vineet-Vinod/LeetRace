import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = {
        "candidate(s='abcdefghijklmnop')",
        "candidate(s='aaaaaaaaaaaaaaaa')",
    }
    while len(calls) < 600:
        s = "".join(
            rng.choice(string.ascii_lowercase[:5]) for _ in range(rng.randint(1, 8))
        )
        calls.add(f"candidate(s={s!r})")
    return sorted(calls)
