def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(3, 100)
        a = rng.randint(1, n - 2)
        b = rng.randint(a, n - 2)
        m = rng.randint(1, 100)
        one = list(range(n))
        two = [rng.randint(0, 100000) for _ in range(m)]
        cases.add(
            f"candidate(list1=list_node({one!r}), a={a}, b={b}, list2=list_node({two!r}))"
        )
    return sorted(cases)
