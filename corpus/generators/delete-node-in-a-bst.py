import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: valid unique-key BST; 0..10000 nodes, values and key -100000..100000; generated valid right-chain trees and example."""
    rng = random.Random(seed)
    calls = {
        "candidate(root=tree_node([5, 3, 6, 2, 4, None, 7]), key=3)",
        "candidate(root=tree_node([]), key=0)",
    }
    while len(calls) < 600:
        values = sorted(rng.sample(range(-1000, 1001), rng.randint(1, 30)))
        level_order: list[int | None] = [values[0]]
        for value in values[1:]:
            level_order.extend([None, value])
        key = rng.randint(-105, 105)
        calls.add(f"candidate(root=tree_node({level_order!r}), key={key})")
    return sorted(calls)
