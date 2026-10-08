def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):

        def digits() -> list[int]:
            size = rng.randint(1, 100)
            if size == 1 and rng.randrange(5) == 0:
                return [0]
            return [rng.randint(1, 9)] + [rng.randint(0, 9) for _ in range(size - 1)]

        a, b = digits(), digits()
        cases.add(f"candidate(l1=list_node({a!r}), l2=list_node({b!r}))")
    assert len(cases) >= 500
    return sorted(cases)[:600]
