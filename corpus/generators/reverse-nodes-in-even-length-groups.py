def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(head=list_node([5, 2, 6, 3, 9, 1, 7, 3, 8, 4]))",
        "candidate(head=list_node([1, 1, 0, 6]))",
        "candidate(head=list_node([1, 1, 0, 6, 5]))",
        f"candidate(head=list_node({[i % 100001 for i in range(100000)]!r}))",
    }
    while len(cases) < 600:
        values = [rng.randint(0, 100_000) for _ in range(rng.randint(1, 1000))]
        assert 1 <= len(values) <= 100_000
        assert all(0 <= value <= 100_000 for value in values)
        cases.add(f"candidate(head=list_node({values!r}))")
    return sorted(cases)
