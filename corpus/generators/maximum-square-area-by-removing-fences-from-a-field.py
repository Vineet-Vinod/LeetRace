import random


def generate(seed: int = 0) -> list[str]:
    """Fence coordinates are unique interior integers in the corresponding dimensions."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        m = 3 + rng.randrange(1000)
        n = 3 + rng.randrange(1000)
        hs = sorted(rng.sample(range(2, m), 1 + i % min(12, m - 2)))
        vs = sorted(rng.sample(range(2, n), 1 + (i * 7) % min(12, n - 2)))
        call = f"candidate(m={m}, n={n}, hFences={hs!r}, vFences={vs!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
