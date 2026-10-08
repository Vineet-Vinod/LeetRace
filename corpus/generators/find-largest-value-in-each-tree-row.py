import random


def generate(seed: int = 0) -> list[str]:
    """Generate arbitrary valid binary trees, including the empty tree, with signed 32-bit values."""
    rng = random.Random(seed)
    calls = ["candidate(root=tree_node([]))"]
    seen = set(calls)
    i = 0
    while len(calls) < 600:
        vals = [rng.randrange(-10000, 10001) for _ in range(1 + i % 45)]
        call = f"candidate(root=tree_node({vals!r}))"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
