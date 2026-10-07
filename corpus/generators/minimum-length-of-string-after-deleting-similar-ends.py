import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: s length1..10^5, alphabet a,b,c."""
    rng = random.Random(seed)
    calls = {"candidate(s='ca')", "candidate(s='cabaabac')", "candidate(s='aabccabba')"}
    while len(calls) < 600:
        s = "".join(rng.choice("abc") for _ in range(rng.randint(1, 500)))
        calls.add(f"candidate(s={s!r})")
    return sorted(calls)
