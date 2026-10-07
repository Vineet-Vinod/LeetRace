import random


def generate(seed: int = 0) -> list[str]:
    """Heroes, monsters, and coins have positive values; monsters and coins lengths match."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        heroes = [rng.randrange(1, 1001) for _ in range(1 + i % 15)]
        n = 1 + (i * 7) % 20
        monsters = [rng.randrange(1, 1001) for _ in range(n)]
        coins = [rng.randrange(1, 1001) for _ in range(n)]
        call = f"candidate(heroes={heroes!r}, monsters={monsters!r}, coins={coins!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
