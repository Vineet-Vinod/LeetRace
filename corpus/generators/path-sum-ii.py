def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(root=tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]), targetSum=22)",
        f"candidate(root=tree_node({[0] + [None, 0] * 4999!r}), targetSum=0)",
        f"candidate(root=tree_node({[0] + [None, 0] * 4999!r}), targetSum=1)",
    }
    while len(cases) < 600:
        size = rng.randint(1, 80)
        if rng.random() < 0.5:
            values = [rng.randint(-10, 10) for _ in range(size)]
            leaf = rng.randrange(size // 2, size)
            path = []
            index = leaf
            while index >= 0:
                path.append(values[index])
                if index == 0:
                    break
                index = (index - 1) // 2
            target = sum(path)
        else:
            values = [rng.randint(1, 1000) for _ in range(size)]
            target = -1000
        assert 1 <= len(values) <= 5000
        assert all(-1000 <= value <= 1000 for value in values)
        assert -1000 <= target <= 1000
        cases.add(f"candidate(root=tree_node({values!r}), targetSum={target})")
    return sorted(cases)
