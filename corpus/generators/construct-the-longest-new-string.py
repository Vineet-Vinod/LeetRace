def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(x=1, y=1, z=1)", "candidate(x=1, y=1, z=2)"}
    cases.update(
        f"candidate(x={x}, y={y}, z={z})"
        for x in range(1, 6)
        for y in range(1, 6)
        for z in range(1, 6)
    )
    cases.add("candidate(x=50, y=50, z=50)")
    while len(cases) < 600:
        x, y, z = (rng.randint(1, 50) for _ in range(3))
        assert 1 <= x <= 50 and 1 <= y <= 50 and 1 <= z <= 50
        cases.add(f"candidate(x={x}, y={y}, z={z})")
    return sorted(cases)
