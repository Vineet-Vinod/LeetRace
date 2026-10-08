import random


def generate(seed: int = 0) -> list[str]:
    """Generate trees within 1..100000 nodes and node values 0..100000."""
    rng = random.Random(seed)
    calls = {
        "candidate(root=tree_node([10, 3, 4, 2, 1]))",
        "candidate(root=tree_node([0]))",
        "candidate(root=tree_node([0] + [None, 0] * 99999))",
        "candidate(root=tree_node([1] * 100000))",
    }
    while len(calls) < 600:
        target_size = rng.randint(1, 1000)
        vals: list[int | None] = [rng.choice([0, 1, 2, 10, 100_000])]
        parents = [0]
        cursor = 0
        node_count = 1
        while cursor < len(parents) and node_count < target_size:
            cursor += 1
            for _ in range(2):
                if node_count >= target_size:
                    vals.append(None)
                elif rng.random() < 0.75:
                    vals.append(
                        rng.choice([0, 1, 2, 10, 100_000, rng.randint(0, 100_000)])
                    )
                    parents.append(len(vals) - 1)
                    node_count += 1
                else:
                    vals.append(None)
        while vals and vals[-1] is None:
            vals.pop()
        assert 1 <= node_count <= 100_000
        assert all(value is None or 0 <= value <= 100_000 for value in vals)
        calls.add(f"candidate(root=tree_node({vals!r}))")
    return sorted(calls)
