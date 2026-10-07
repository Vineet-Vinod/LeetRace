import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        n = rng.choice(range(3, 101, 2))
        permutation = list(range(1, n + 1))
        rng.shuffle(permutation)
        encoded = [permutation[i] ^ permutation[i + 1] for i in range(n - 1)]
        calls.add(f"candidate(encoded={encoded!r})")
    return sorted(calls)
