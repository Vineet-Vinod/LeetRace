import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = {"candidate(root=tree_node([]))"}
    for size in range(1, 70):
        for _ in range(9):
            values = [rng.randint(-1000, 1000) for _ in range(size)]
            calls.add(f"candidate(root=tree_node({values!r}))")
    calls.add("candidate(root=tree_node([5] * 1000))")
    return sorted(calls)[:600]
