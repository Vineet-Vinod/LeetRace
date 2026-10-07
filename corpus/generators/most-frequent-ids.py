import random


def generate(seed: int = 0) -> list[str]:
    """Frequency updates are nonzero and never cause any identifier count to become negative."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        nums = []
        freq = []
        counts = {}
        for _ in range(1 + i % 50):
            available = [key for key, value in counts.items() if value > 0]
            if available and rng.random() < 0.35:
                identifier = rng.choice(available)
                change = -rng.randint(1, counts[identifier])
            else:
                identifier = rng.randrange(1, 20)
                change = rng.randint(1, 20)
            counts[identifier] = counts.get(identifier, 0) + change
            nums.append(identifier)
            freq.append(change)
        call = f"candidate(nums={nums!r}, freq={freq!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
