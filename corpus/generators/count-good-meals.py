def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(deliciousness=[0])",
        "candidate(deliciousness=[1,1])",
        "candidate(deliciousness=[1048576,0])",
        f"candidate(deliciousness={[1] * 100000!r})",
        f"candidate(deliciousness={[3] * 100000!r})",
    }
    while len(cases) < 600:
        if rng.random() < 0.5:
            count = rng.randint(2, 100)
            value = 1 << rng.randint(0, 19)
        else:
            count = rng.randint(2, 100)
            value = rng.randint(3, 1000)
            while value & (value - 1) == 0:
                value = rng.randint(3, 1000)
        deliciousness = [value] * count
        assert 1 <= len(deliciousness) <= 100000
        assert all(0 <= item <= 2**20 for item in deliciousness)
        cases.add(f"candidate(deliciousness={deliciousness!r})")
    return sorted(cases)
