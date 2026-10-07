import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    boundary_values = list(range(10000))
    boundary_tree: dict[int, int] = {}

    def add_boundary_subtree(left: int, right: int, index: int) -> None:
        if left >= right:
            return
        middle = (left + right) // 2
        boundary_tree[index] = boundary_values[middle]
        add_boundary_subtree(left, middle, index * 2 + 1)
        add_boundary_subtree(middle + 1, right, index * 2 + 2)

    add_boundary_subtree(0, len(boundary_values), 0)
    boundary_level = [
        boundary_tree.get(index) for index in range(max(boundary_tree) + 1)
    ]
    while boundary_level and boundary_level[-1] is None:
        boundary_level.pop()
    calls.add(f"candidate(root=tree_node({boundary_level!r}))")
    while len(calls) < 600:
        size = rng.randint(2, 100)
        values = sorted(rng.sample(range(0, 100001), size))
        level_values: dict[int, int] = {}

        def add_subtree(left: int, right: int, index: int) -> None:
            if left >= right:
                return
            middle = (left + right) // 2
            level_values[index] = values[middle]
            add_subtree(left, middle, index * 2 + 1)
            add_subtree(middle + 1, right, index * 2 + 2)

        add_subtree(0, len(values), 0)
        vals: list[int | None] = [
            level_values.get(index) for index in range(max(level_values) + 1)
        ]
        while vals and vals[-1] is None:
            vals.pop()
        calls.add(f"candidate(root=tree_node({vals!r}))")
    return sorted(calls)
