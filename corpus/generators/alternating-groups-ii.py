import random


def generate(seed: int = 0) -> list[str]:
    """Generate 600 distinct circles, with 3 <= k <= len(colors) and binary colors."""
    rng = random.Random(seed)
    cases: list[str] = []
    seen: set[str] = set()
    i = 0
    while len(cases) < 600:
        n = 3 + i % 38
        colors = [rng.randrange(2) for _ in range(n)]
        k = 3 + (i * 7) % (n - 2)
        assert 3 <= k <= n and all(c in (0, 1) for c in colors)
        call = f"candidate(colors={colors!r}, k={k})"
        i += 1
        if call not in seen:
            seen.add(call)
            cases.append(call)
    return cases
