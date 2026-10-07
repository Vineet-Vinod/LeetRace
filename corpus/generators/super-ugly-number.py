import random


def generate(seed: int = 0) -> list[str]:
    """Prime lists are sorted, unique, and composed of actual primes from the allowed range."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    primes_all = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    while len(calls) < 600:
        primes = sorted(rng.sample(primes_all, 1 + i % 8))
        n = 1 + (i * 7) % 40
        if i % 101 == 0:
            primes = [2, 3, 5]
            n = 100
        call = f"candidate(n={n}, primes={primes!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
