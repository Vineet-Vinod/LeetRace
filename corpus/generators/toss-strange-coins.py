import random


def generate(seed: int = 0) -> list[str]:
    """Generate probability arrays with values in [0,1] and a legal target count."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        prob = [round(rng.random(), 4) for _ in range(1 + i % 50)]
        target = (i * 7) % (len(prob) + 1)
        call = f"candidate(prob={prob!r}, target={target})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
