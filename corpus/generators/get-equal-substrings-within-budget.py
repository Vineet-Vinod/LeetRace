import random
import string


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: equal lowercase strings length1..100000; cost budget0..10^6."""
    rng = random.Random(seed)
    calls = {
        "candidate(s='abcd', t='bcdf', maxCost=3)",
        "candidate(s='abcd', t='acde', maxCost=0)",
    }
    while len(calls) < 600:
        size = rng.randint(1, 300)
        s = "".join(rng.choice(string.ascii_lowercase) for _ in range(size))
        t = "".join(rng.choice(string.ascii_lowercase) for _ in range(size))
        calls.add(f"candidate(s={s!r}, t={t!r}, maxCost={rng.randint(0, 10**6)})")
    return sorted(calls)
