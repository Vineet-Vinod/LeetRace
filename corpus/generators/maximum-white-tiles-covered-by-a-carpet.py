def _generate_base(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        count = rng.randint(1, 30)
        position = rng.randint(1, 1000)
        tiles = []
        for _ in range(count):
            start = position + rng.randint(0, 20)
            end = start + rng.randint(0, 50)
            tiles.append([start, end])
            position = end + 1
        carpet = rng.randint(1, 1000)
        assert all(tiles[i][1] < tiles[i + 1][0] for i in range(len(tiles) - 1))
        cases.add(f"candidate(tiles={tiles!r}, carpetLen={carpet})")
    assert len(cases) >= 500
    return sorted(cases)[:600]


def generate(seed: int = 0) -> list[str]:
    calls = _generate_base(seed)
    boundary = f"candidate(tiles={[[2 * index + 1, 2 * index + 1] for index in range(50000)]!r}, carpetLen=50000)"
    if boundary not in calls:
        calls[-1] = boundary
    assert 500 <= len(calls) <= 999
    return calls
