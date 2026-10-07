import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: s length 1..500; 0..50 nonempty lowercase keywords of length <=10."""
    rng = random.Random(seed)
    calls = {
        "candidate(words=['ab', 'bc'], s='aabcd')",
        "candidate(words=['ab', 'cb'], s='aabcd')",
    }
    while len(calls) < 600:
        s = "".join(rng.choice("abc") for _ in range(rng.randint(1, 80)))
        words = [
            "".join(rng.choice("abc") for _ in range(rng.randint(1, 10)))
            for _ in range(rng.randint(0, 12))
        ]
        calls.add(f"candidate(words={words!r}, s={s!r})")
    return sorted(calls)
