import random


def generate(seed: int = 0) -> list[str]:
    """Generate binary trees of 0..10000 nodes, depth at most 1000, values -1000..1000."""
    rng = random.Random(seed)
    calls = {
        "candidate(root=tree_node([]))",
        "candidate(root=tree_node([5, 4, 5, 1, 1, None, 5]))",
        "candidate(root=tree_node([4] * 1023))",
        "candidate(root=tree_node([4] * 10000))",
        "candidate(root=tree_node([7] + [None, 7] * 999))",
    }
    maximum_nodes = 10_000
    maximum_depth = maximum_nodes.bit_length() - 1
    assert maximum_nodes <= 10_000 and maximum_depth <= 1000
    while len(calls) < 600:
        target = rng.randint(1, 300)
        vals: list[int | None] = [rng.choice([-2, -1, 0, 1, 2])]
        parents = [0]
        cursor = 0
        node_count = 1
        while cursor < len(parents) and node_count < target:
            cursor += 1
            for _ in range(2):
                if node_count >= target:
                    vals.append(None)
                elif rng.random() < 0.82:
                    vals.append(rng.choice([-2, -1, 0, 1, 2]))
                    parents.append(len(vals) - 1)
                    node_count += 1
                else:
                    vals.append(None)
        while vals and vals[-1] is None:
            vals.pop()
        assert node_count <= 10_000 and all(
            value is None or -1000 <= value <= 1000 for value in vals
        )
        calls.add(f"candidate(root=tree_node({vals!r}))")
    return sorted(calls)
