import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases, seen = [], set()
    while len(cases) < 600:
        count = rng.randint(1, 50)
        vals = [rng.randint(1, 100) for _ in range(count)]
        key = tuple(vals)
        if key not in seen:
            seen.add(key)
            assert all(1 <= value <= 100 for value in vals)
            cases.append(f"candidate(root=tree_node({vals!r}))")
    return cases
