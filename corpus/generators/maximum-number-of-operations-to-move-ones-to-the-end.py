import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: binary string length1..10^5."""
    rng = random.Random(seed)
    calls = {"candidate(s='1001101')", "candidate(s='00111')"}
    while len(calls) < 600:
        s = "".join(rng.choice("01") for _ in range(rng.randint(1, 1000)))
        calls.add(f"candidate(s={s!r})")
    return sorted(calls)
