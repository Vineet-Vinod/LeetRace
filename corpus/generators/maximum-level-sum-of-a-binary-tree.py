import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: valid tree with1..10^4 nodes and values -10^5..10^5."""
    rng = random.Random(seed)
    calls = {
        "candidate(root=tree_node([1, 7, 0, 7, -8]))",
        "candidate(root=tree_node([989, None, 10250, 98693, -89388, None, None, None, -32127]))",
    }
    while len(calls) < 600:
        target = rng.randint(1, 100)
        vals: list[int | None] = [rng.randint(-100_000, 100_000)]
        parents = [0]
        cursor = 0
        while (
            cursor < len(parents) and sum(value is not None for value in vals) < target
        ):
            cursor += 1
            for _ in range(2):
                if sum(value is not None for value in vals) >= target:
                    vals.append(None)
                elif rng.random() < 0.75:
                    vals.append(rng.randint(-100_000, 100_000))
                    parents.append(len(vals) - 1)
                else:
                    vals.append(None)
        while vals and vals[-1] is None:
            vals.pop()
        calls.add(f"candidate(root=tree_node({vals!r}))")
    return sorted(calls)
