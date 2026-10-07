import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: 0..100 nodes, values -100..100; generator builds connected level-order trees."""
    rng = random.Random(seed)
    calls = {
        "candidate(root=tree_node([]))",
        "candidate(root=tree_node([1, 2, 3, None, 5, None, 4]))",
    }
    while len(calls) < 600:
        target_size = rng.randint(1, 50)
        vals: list[int | None] = [rng.randint(-100, 100)]
        parents = [0]
        cursor = 0
        while (
            cursor < len(parents)
            and sum(value is not None for value in vals) < target_size
        ):
            parents[cursor]
            cursor += 1
            for _ in range(2):
                if sum(value is not None for value in vals) >= target_size:
                    vals.append(None)
                    continue
                if rng.random() < 0.7:
                    vals.append(rng.randint(-100, 100))
                    parents.append(len(vals) - 1)
                else:
                    vals.append(None)
        while vals and vals[-1] is None:
            vals.pop()
        calls.add(f"candidate(root=tree_node({vals!r}))")
    return sorted(calls)
