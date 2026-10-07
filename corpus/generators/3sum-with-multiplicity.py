import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: arr length 3..3000; values 0..100; target 0..300."""
    rng = random.Random(seed)
    calls: set[str] = set()
    fixed = [
        ([0, 0, 0], 0),
        ([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8),
        ([2, 1, 3], 6),
        ([100, 100, 100], 300),
        ([0, 100, 100], 200),
    ]
    for arr, target in fixed:
        calls.add(f"candidate(arr={arr!r}, target={target})")
    while len(calls) < 600:
        size = rng.randint(3, 45)
        arr = [rng.randrange(101) for _ in range(size)]
        target = rng.randrange(301)
        calls.add(f"candidate(arr={arr!r}, target={target})")
    return sorted(calls)
