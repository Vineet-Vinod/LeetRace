import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: valid unique-key BST with at most10^4 nodes; values and inserted key -10^8..10^8; inserted value absent."""
    rng = random.Random(seed)
    calls = {
        "candidate(root=tree_node([]), val=5)",
        "candidate(root=tree_node([4, 2, 7, 1, 3]), val=5)",
    }
    while len(calls) < 600:
        values = sorted(rng.sample(range(-(10**8), 10**8 + 1), rng.randint(1, 25)))
        level_order: list[int | None] = [values[0]]
        for value in values[1:]:
            level_order.extend([None, value])
        present = set(values)
        value = rng.randint(-(10**8), 10**8)
        while value in present:
            value = rng.randint(-(10**8), 10**8)
        calls.add(f"candidate(root=tree_node({level_order!r}), val={value})")
    return sorted(calls)
