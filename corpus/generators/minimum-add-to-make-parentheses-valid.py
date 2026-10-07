import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: s length1..1000, chars only parentheses."""
    rng = random.Random(seed)
    calls = {"candidate(s='())')", "candidate(s='(((')"}
    while len(calls) < 600:
        s = "".join(rng.choice("()") for _ in range(rng.randint(1, 1000)))
        calls.add(f"candidate(s={s!r})")
    return sorted(calls)
