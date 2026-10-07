import random


def generate(seed: int = 0) -> list[str]:
    """Generate sorted arrays with exactly one pair summing to a target in [-1000,1000]."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        n = 2 + i % 35
        numbers = sorted(rng.sample(range(-1000, 1001), n))
        pairs = {}
        for a in range(n):
            for b in range(a + 1, n):
                pairs.setdefault(numbers[a] + numbers[b], []).append((a, b))
        targets = [
            target
            for target, indices in pairs.items()
            if len(indices) == 1 and -1000 <= target <= 1000
        ]
        if not targets:
            continue
        target = rng.choice(targets)
        call = f"candidate(numbers={numbers!r}, target={target})"
        if call not in seen:
            seen.add(call)
            calls.append(call)
        i += 1
    return calls
