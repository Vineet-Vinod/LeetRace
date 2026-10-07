import random


def generate(seed: int = 0) -> list[str]:
    """Each node array is level-order for a complete binary tree and uses values in the stated range."""
    rng = random.Random(seed)
    cases = [[], [1], [1, 2], [1, 2, 3], [1, 2, 3, 4, 5, 6]]
    seen = {tuple(x) for x in cases}
    while len(cases) < 600:
        n = rng.randint(0, 100)
        vals = [rng.randint(0, 50000) for _ in range(n)]
        key = tuple(vals)
        if key not in seen:
            seen.add(key)
            cases.append(vals)
    cases.extend([list(range(50000)), [50000] * 50000])
    return [f"candidate(root=tree_node({v!r}))" for v in cases]
