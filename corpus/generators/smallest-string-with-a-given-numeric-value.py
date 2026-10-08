import random


def generate(seed: int = 0) -> list[str]:
    """Generate feasible 1<=n and n<=k<=26n."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        n = 1 + i % 70
        k = rng.randrange(n, 26 * n + 1)
        call = f"candidate(n={n}, k={k})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
