import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {"candidate(root=tree_node([]))"}
    for size in range(1, 70):
        for _ in range(9):
            values = [rng.randint(-1000, 1000) for _ in range(size)]
            cases.add(f"candidate(root=tree_node({values!r}))")
    return sorted(cases)[:600]
