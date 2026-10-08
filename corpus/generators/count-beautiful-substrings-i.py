import random


def generate(seed: int = 0) -> list[str]:
    """Generate lowercase strings of length 1..1000 and k in 1..1000."""
    rng = random.Random(seed)
    calls = {
        "candidate(s='baeyh', k=2)",
        "candidate(s='abba', k=1)",
        "candidate(s='bcdf', k=1)",
        "candidate(s='ab' * 500, k=1)",
        "candidate(s='aeiou' * 200, k=25)",
    }
    for pairs in range(1, 101):
        for k in (1, 2, 4, 9, 25, 1000):
            s = "ab" * pairs
            calls.add(f"candidate(s={s!r}, k={k})")
    alphabet = "aeioubcdfg"
    while len(calls) < 600:
        length = rng.randint(1, 120)
        s = "".join(rng.choice(alphabet) for _ in range(length))
        k = rng.choice([1, 2, 4, 9, 25, 1000, rng.randint(1, 1000)])
        assert 1 <= len(s) <= 1000 and s.islower() and 1 <= k <= 1000
        calls.add(f"candidate(s={s!r}, k={k})")
    return sorted(calls)
