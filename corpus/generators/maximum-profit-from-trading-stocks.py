def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(present=[0]*1000,future=[100]*1000,budget=1000)",
        "candidate(present=[100]*1000,future=[0]*1000,budget=0)",
    }
    while len(cases) < 600:
        n = rng.randint(1, 100)
        present = [rng.randint(0, 100) for _ in range(n)]
        future = [rng.randint(0, 100) for _ in range(n)]
        budget = rng.randint(0, 1000)
        assert 1 <= len(present) == len(future) <= 1000
        assert all(0 <= value <= 100 for value in present + future)
        assert 0 <= budget <= 1000
        cases.add(f"candidate(present={present!r},future={future!r},budget={budget})")
    return sorted(cases)
