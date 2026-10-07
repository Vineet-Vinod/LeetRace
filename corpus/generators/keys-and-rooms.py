def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(2, 100)
        rooms = []
        for _ in range(n):
            rooms.append(rng.sample(range(n), rng.randint(0, min(n, 20))))
        if not any(rooms):
            rooms[0] = [1]
        cases.add(f"candidate(rooms={rooms!r})")
    return sorted(cases)
