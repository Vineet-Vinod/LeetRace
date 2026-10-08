import random


def generate(seed: int = 0) -> list[str]:
    """Generate nonempty trees with unique node values in the stated value range."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    index = 0
    while len(calls) < 600:
        node_count = 1 + index % 40
        values = rng.sample(range(1, 10_001), node_count)
        assert 1 <= node_count <= 100_000
        assert len(set(values)) == node_count
        assert all(1 <= value <= 10_000 for value in values)
        call = f"candidate(root=tree_node({values!r}))"
        index += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
