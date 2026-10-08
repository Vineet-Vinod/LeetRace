import random
import string


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: lowercase string length 1..100000; includes a 100000-character boundary case."""
    rng = random.Random(seed)
    calls = {
        "candidate(s='abcd')",
        "candidate(s='ooo')",
        "candidate(s='abab')",
        f"candidate(s={'a' * 100000!r})",
    }
    while len(calls) < 600:
        size = rng.randint(1, 500)
        s = "".join(rng.choice(string.ascii_lowercase) for _ in range(size))
        calls.add(f"candidate(s={s!r})")
    return sorted(calls)
