import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        size = rng.randint(1, 100)
        values = sorted(rng.sample(range(1, 100001), size))
        level_values: dict[int, int] = {}

        def add_subtree(left: int, right: int, index: int) -> None:
            if left >= right:
                return
            middle = (left + right) // 2
            level_values[index] = values[middle]
            add_subtree(left, middle, index * 2 + 1)
            add_subtree(middle + 1, right, index * 2 + 2)

        add_subtree(0, size, 0)
        tree = [level_values.get(i) for i in range(max(level_values) + 1)]
        while tree and tree[-1] is None:
            tree.pop()
        low, high = sorted((rng.randint(1, 100000), rng.randint(1, 100000)))
        calls.add(f"candidate(root=tree_node({tree!r}), low={low}, high={high})")
    return sorted(calls)
