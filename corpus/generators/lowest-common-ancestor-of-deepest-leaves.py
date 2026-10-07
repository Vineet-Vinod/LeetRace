def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(1, 70)
        vals = rng.sample(range(0, 1001), n)
        level = [vals[0]]
        queue = [0]
        used = 1
        while queue and used < n:
            queue.pop(0)
            for _ in range(2):
                if used < n and rng.random() < 0.75:
                    level.append(vals[used])
                    queue.append(used)
                    used += 1
                else:
                    level.append(None)
        while used < n:
            level.append(vals[used])
            used += 1
        cases.add(f"candidate(root=tree_node({level!r}))")
    return sorted(cases)
