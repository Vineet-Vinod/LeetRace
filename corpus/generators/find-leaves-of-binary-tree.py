import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = set()
    for size in range(1, 70):
        for _ in range(9):
            values = [rng.randint(-100, 100) for _ in range(size)]
            calls.add(f"candidate(root=tree_node({values!r}))")
    return sorted(calls)[:600]
