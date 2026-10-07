import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: valid nonempty tree, at most3000 nodes; node values -100..100."""
    rng = random.Random(seed)
    calls = {
        "candidate(root=tree_node([1, 3, 2, 5, 3, None, 9]))",
        "candidate(root=tree_node([1, 3, 2, 5, None, None, 9, 6, None, 7]))",
    }
    while len(calls) < 600:
        target = rng.randint(1, 100)
        vals: list[int | None] = [rng.randint(-100, 100)]
        parents = [0]
        cursor = 0
        while (
            cursor < len(parents) and sum(value is not None for value in vals) < target
        ):
            cursor += 1
            for _ in range(2):
                if sum(value is not None for value in vals) >= target:
                    vals.append(None)
                elif rng.random() < 0.7:
                    vals.append(rng.randint(-100, 100))
                    parents.append(len(vals) - 1)
                else:
                    vals.append(None)
        while vals and vals[-1] is None:
            vals.pop()
        calls.add(f"candidate(root=tree_node({vals!r}))")
    return sorted(calls)
