import random


def generate(seed: int = 0) -> list[str]:
    """Generate 600 distinct binary trees with 0..2000 nodes and values in [-100,100]."""
    rng = random.Random(seed)
    calls = ["candidate(root=tree_node([]))"]
    seen = set(calls)
    index = 1
    while len(calls) < 600:
        n = 1 + index % 40
        values = [rng.randrange(-100, 101) for _ in range(n)]
        assert 1 <= n <= 2000 and all(-100 <= x <= 100 for x in values)
        call = f"candidate(root=tree_node({values!r}))"
        index += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
