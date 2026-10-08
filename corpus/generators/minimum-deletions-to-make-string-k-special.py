import random


def generate(seed: int = 0) -> list[str]:
    """Generate lowercase words of length 1..100000 with k in 0..100000."""
    rng = random.Random(seed)
    calls = {
        "candidate(word='aabcaba', k=0)",
        "candidate(word='dabdcbdcdcd', k=2)",
        "candidate(word='aaabaaa', k=2)",
        "candidate(word='a' * 100000, k=0)",
        "candidate(word='a' * 50000 + 'b' * 30000 + 'c' * 19999 + 'd', k=0)",
        "candidate(word='a' * 50000 + 'b' * 30000 + 'c' * 19999 + 'd', k=100000)",
    }
    while len(calls) < 600:
        letters = rng.randint(1, 8)
        counts = [rng.randint(1, 500) for _ in range(letters)]
        word = "".join(chr(ord("a") + i) * count for i, count in enumerate(counts))
        k = rng.choice([0, 1, 2, 5, 20, 100_000, rng.randint(0, 100_000)])
        assert 1 <= len(word) <= 100_000 and word.islower() and 0 <= k <= 100_000
        calls.add(f"candidate(word={word!r}, k={k})")
    return sorted(calls)
