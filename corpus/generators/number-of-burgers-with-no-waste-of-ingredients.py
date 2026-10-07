import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    pairs = {(16, 7), (17, 4), (4, 17), (0, 0)}
    # Construct feasible ingredient totals from nonnegative burger counts.
    for _ in range(200):
        jumbo = rng.randint(0, 5000)
        small = rng.randint(0, 5000)
        pairs.add((4 * jumbo + 2 * small, jumbo + small))
    while len(pairs) < 600:
        pairs.add((rng.randint(0, 10**7), rng.randint(0, 10**7)))
    calls = [
        f"candidate(tomatoSlices={tomatoes}, cheeseSlices={cheese})"
        for tomatoes, cheese in pairs
    ]
    calls.append("candidate(tomatoSlices=10000000, cheeseSlices=5000000)")
    assert 500 <= len(calls) <= 999
    assert len(calls) == len(set(calls))
    return calls
