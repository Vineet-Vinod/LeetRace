import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = set()
    for size in range(1, 70):
        for _ in range(9):
            values = [rng.randint(1, 100) for _ in range(size)]
            calls.add(f"candidate(root=tree_node({values!r}))")
    calls.add(
        "candidate(root=tree_node([1, None, 1, 1, 1, None, None, 1, 1, None, 1]))"
    )
    return sorted(calls)[:600]
