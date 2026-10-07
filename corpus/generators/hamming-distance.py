import random


def generate(seed: int = 0) -> list[str]:
    """Generate distinct valid cases: x,y in [0,2^31-1]."""
    rng = random.Random(seed)
    cases = {(a, b) for a in range(32) for b in range(32)}
    while len(cases) < 600:
        cases.add((rng.randrange(2**31), rng.randrange(2**31)))
    selected = set(sorted(cases)[:300])
    while len(selected) < 700:
        selected.add((rng.randrange(2**31), rng.randrange(2**31)))
    return [f"candidate(x={a}, y={b})" for a, b in sorted(selected)]
