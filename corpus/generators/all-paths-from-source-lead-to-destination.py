def _generate_base(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        n = rng.randint(1, 20)
        edges = []
        for start in range(n):
            for end in range(n):
                if rng.random() < 0.08:
                    edges.append([start, end])
        source = rng.randrange(n)
        destination = rng.randrange(n)
        cases.add(
            f"candidate(n={n}, edges={edges!r}, source={source}, destination={destination})"
        )
    assert len(cases) >= 500
    return sorted(cases)[:600]


def generate(seed: int = 0) -> list[str]:
    calls = _generate_base(seed)
    nodes = 143
    destination = nodes - 1
    edges = [[node, destination] for node in range(destination)]
    for start in range(destination):
        for end in range(start + 1, destination):
            if len(edges) == 10000:
                break
            edges.append([start, end])
        if len(edges) == 10000:
            break
    assert len(edges) == 10000
    assert all(start < end for start, end in edges)
    boundary = (
        f"candidate(n={nodes}, edges={edges!r}, source=0, destination={destination})"
    )
    if boundary not in calls:
        calls[-1] = boundary
    assert 500 <= len(calls) <= 999
    return calls
