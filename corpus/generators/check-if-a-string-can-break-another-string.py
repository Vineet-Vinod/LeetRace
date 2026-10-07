import random
import string


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: equal length 1..100000; lowercase English letters."""
    rng = random.Random(seed)
    calls = {"candidate(s1='abc', s2='xya')", "candidate(s1='abe', s2='acd')"}
    while len(calls) < 600:
        size = rng.randint(1, 100)
        s1 = "".join(rng.choice(string.ascii_lowercase) for _ in range(size))
        s2 = "".join(rng.choice(string.ascii_lowercase) for _ in range(size))
        calls.add(f"candidate(s1={s1!r}, s2={s2!r})")
    return sorted(calls)
