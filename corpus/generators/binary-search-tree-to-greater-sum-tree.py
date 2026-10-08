import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: valid BST, 1..100 nodes, unique keys 0..100; generated trees are sorted right chains plus stated example."""
    rng = random.Random(seed)
    calls = {
        "candidate(root=tree_node([4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]))"
    }
    while len(calls) < 600:
        values = sorted(rng.sample(range(101), rng.randint(1, 20)))
        # Alternating null markers encode a valid right-only BST chain for tree_node.
        level_order: list[int | None] = [values[0]]
        for value in values[1:]:
            level_order.extend([None, value])
        calls.add(f"candidate(root=tree_node({level_order!r}))")
    return sorted(calls)
