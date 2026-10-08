def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(root=tree_node(None), targetSum=0)",
        "candidate(root=tree_node([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]), targetSum=8)",
        "candidate(root=tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]), targetSum=22)",
        "candidate(root=tree_node([0, 0, 0]), targetSum=0)",
        f"candidate(root=tree_node({[0] * 1000!r}), targetSum=0)",
        f"candidate(root=tree_node({[1000000000] * 1000!r}), targetSum=1000)",
    }
    while len(cases) < 300:
        values = [rng.randint(-5, 5) for _ in range(rng.randint(1, 31))]
        target = rng.randint(-1000, 1000)
        node_index = rng.randrange(len(values))
        ancestor_indices = []
        index = node_index
        while True:
            ancestor_indices.append(index)
            if index == 0:
                break
            index = (index - 1) // 2
        target = sum(values[index] for index in ancestor_indices)
        assert -1000 <= target <= 1000
        cases.add(f"candidate(root=tree_node({values!r}), targetSum={target})")

    while len(cases) < 600:
        values = [rng.randint(-1000, 1000) for _ in range(rng.randint(1, 60))]
        target = rng.randint(-1000, 1000)
        assert len(values) <= 1000 and all(
            -(10**9) <= value <= 10**9 for value in values
        )
        cases.add(f"candidate(root=tree_node({values!r}), targetSum={target})")
    assert len(cases) == 600
    return sorted(cases)
