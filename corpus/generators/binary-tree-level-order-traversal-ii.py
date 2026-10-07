import random


def generate(seed: int = 0) -> list[str]:

    rng = random.Random(seed)
    cases, seen = [], set()
    cases.append("candidate(root=None)")
    seen.add(())
    while len(cases) < 600:
        n = rng.randint(1, 40)
        vals = [rng.randint(-1000, 1000) for _ in range(n)]
        level = vals[:]
        key = tuple(level)
        if key not in seen:
            seen.add(key)
            assert -1000 <= min(vals) <= max(vals) <= 1000
            cases.append(f"candidate(root=tree_node({level!r}))")
    return cases
