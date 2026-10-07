import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        m = rng.randint(1, 50)
        n = rng.randint(1, 50)
        indices = [
            [rng.randrange(m), rng.randrange(n)] for _ in range(rng.randint(1, 100))
        ]
        assert 1 <= m <= 50 and 1 <= n <= 50 and 1 <= len(indices) <= 100
        calls.add(f"candidate(m={m}, n={n}, indices={indices!r})")
    return sorted(calls)
