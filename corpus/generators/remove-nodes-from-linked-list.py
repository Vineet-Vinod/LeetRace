import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = [
        "candidate(head=list_node([5, 2, 13, 3, 8]))",
        "candidate(head=list_node([1, 1, 1, 1]))",
        "candidate(head=list_node(list(range(1, 100001))))",
    ]
    seen = {tuple([5, 2, 13, 3, 8]), (1, 1, 1, 1), tuple(range(1, 100001))}
    while len(cases) < 600:
        values = [rng.randint(1, 100000) for _ in range(rng.randint(1, 100))]
        key = tuple(values)
        if key not in seen:
            seen.add(key)
            assert 1 <= len(values) <= 100000
            assert all(1 <= value <= 100000 for value in values)
            cases.append(f"candidate(head=list_node({values!r}))")
    return cases
