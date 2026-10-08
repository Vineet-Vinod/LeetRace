def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(head=list_node([4, 2, 1, 3]))",
        "candidate(head=list_node([-1, 5, 3, 4, 0]))",
        "candidate(head=list_node([]))",
        f"candidate(head=list_node({list(range(50000, 0, -1))!r}))",
    }
    while len(cases) < 600:
        n = rng.randint(0, 100)
        values = [rng.randint(-100000, 100000) for _ in range(n)]
        assert len(values) <= 50000 and all(-100000 <= x <= 100000 for x in values)
        cases.add(f"candidate(head=list_node({values!r}))")
    return sorted(cases)
