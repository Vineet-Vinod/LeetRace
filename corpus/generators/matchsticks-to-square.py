def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(matchsticks=[1,1,2,2,2])",
        "candidate(matchsticks=[1,1,1,1])",
        "candidate(matchsticks=[8,4,4,2,2,2,2,1,1,1,1,1,1,1,1])",
        f"candidate(matchsticks={[10**8] * 4!r})",
        f"candidate(matchsticks={[1] * 14 + [100]!r})",
    }
    while len(cases) < 600:
        if rng.random() < 0.5:
            segment = rng.randint(1, 100000)
            side_parts = rng.randint(1, 3)
            sticks = [segment] * (4 * side_parts)
        else:
            scale = rng.randint(1, 20000000)
            sticks = [scale, scale, scale, 5 * scale]
        assert 1 <= len(sticks) <= 15
        assert all(1 <= stick <= 10**8 for stick in sticks)
        cases.add(f"candidate(matchsticks={sticks!r})")
    return sorted(cases)
