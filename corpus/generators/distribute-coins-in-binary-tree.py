import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        "candidate(root=tree_node([3, 0, 0]))",
        "candidate(root=tree_node([0, 3, 0]))",
    }
    for size in range(1, 70):
        for _ in range(9):
            values = [0] * size
            for _ in range(size):
                values[rng.randrange(size)] += 1
            cases.add(f"candidate(root=tree_node({values!r}))")
    return sorted(cases)[:600]
