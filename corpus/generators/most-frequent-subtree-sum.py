import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = set()
    for size in range(1, 70):
        for _ in range(9):
            values = [rng.randint(-100_000, 100_000) for _ in range(size)]
            calls.add(f"candidate(root=tree_node({values!r}))")
    calls.add("candidate(root=tree_node([5, 2, -3]))")
    calls.add("candidate(root=tree_node([5, 2, -5]))")
    calls.add("candidate(root=tree_node([1] * 10000))")
    return sorted(calls)[:600]
