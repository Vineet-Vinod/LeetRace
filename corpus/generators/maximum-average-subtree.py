import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        vals = [rng.randint(0, 100000) for _ in range(rng.randint(1, 45))]
        key = tuple(vals)
        if key not in seen:
            seen.add(key)
            assert vals and all(0 <= v <= 100000 for v in vals)
            cases.append(f"candidate(root=tree_node({vals!r}))")
    return cases
