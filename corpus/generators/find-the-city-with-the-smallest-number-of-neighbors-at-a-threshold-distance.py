import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: n2..100; distinct bidirectional edges, weights and threshold1..10^4."""
    rng = random.Random(seed)
    calls = {
        "candidate(n=4, edges=[[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], distanceThreshold=4)"
    }
    while len(calls) < 600:
        n = rng.randint(2, 15)
        edges = [
            [a, b, rng.randint(1, 50)]
            for a in range(n)
            for b in range(a + 1, n)
            if rng.random() < 0.3
        ]
        if not edges:
            edges.append([0, 1, rng.randint(1, 50)])
        calls.add(
            f"candidate(n={n}, edges={edges!r}, distanceThreshold={rng.randint(1, 10_000)})"
        )
    return sorted(calls)
