def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(head=list_node([0, 3, 1, 0, 4, 5, 2, 0]))",
        "candidate(head=list_node([0, 1, 0]))",
        "candidate(head=list_node([0, 1000, 0]))",
        f"candidate(head=list_node({[0, 1] * 50 + [0]!r}))",
    }
    maximum_nodes = [0] + [1] * 99998 + [0] + [1000] * 99999 + [0]
    assert len(maximum_nodes) == 200000
    assert maximum_nodes[0] == maximum_nodes[-1] == 0
    assert all(left or right for left, right in zip(maximum_nodes, maximum_nodes[1:]))
    cases.add(f"candidate(head=list_node({maximum_nodes!r}))")

    while len(cases) < 600:
        segment_count = rng.randint(1, 30)
        values = [0]
        for _ in range(segment_count):
            values.extend(rng.randint(1, 1000) for _ in range(rng.randint(1, 10)))
            values.append(0)
        assert 3 <= len(values) <= 200000
        assert values[0] == values[-1] == 0
        assert all(left or right for left, right in zip(values, values[1:]))
        assert all(0 <= value <= 1000 for value in values)
        cases.add(f"candidate(head=list_node({values!r}))")
    assert len(cases) == 600
    return sorted(cases)
