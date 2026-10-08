import random


def generate(seed: int = 0) -> list[str]:
    """Generate equal counts of nonzero positive and negative integers."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        n = 1 + i % 50
        values = [rng.randrange(1, 100001) for _ in range(n)] + [
            -rng.randrange(1, 100001) for _ in range(n)
        ]
        rng.shuffle(values)
        call = f"candidate(nums={values!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
