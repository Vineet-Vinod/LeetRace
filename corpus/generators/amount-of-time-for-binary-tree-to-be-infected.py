import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = {
        "candidate(root=tree_node([1]), start=1)",
        "candidate(root=tree_node(list(range(1, 1001))), start=1)",
    }
    for size in range(1, 70):
        for _ in range(9):
            values = rng.sample(range(1, 100_001), size)
            start = rng.choice(values)
            calls.add(f"candidate(root=tree_node({values!r}), start={start})")
    assert all(1 <= len(call) for call in calls)
    return sorted(calls)[:600]
