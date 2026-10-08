"""Seeded unique calls are constructed within the stated input constraints."""


def _generate_base(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)

    def leaf_sums(values: list[int]) -> list[int]:
        pending = [(0, values[0])]
        sums = []
        while pending:
            index, total = pending.pop()
            children = [
                child for child in (2 * index + 1, 2 * index + 2) if child < len(values)
            ]
            if children:
                pending.extend((child, total + values[child]) for child in children)
            else:
                sums.append(total)
        return sums

    true_cases = set()
    false_cases = set()
    while len(true_cases) < 300 or len(false_cases) < 300:
        values = [rng.randint(-30, 30) for _ in range(rng.randint(1, 80))]
        sums = leaf_sums(values)
        if len(true_cases) < 300:
            target = rng.choice(sums)
            assert target in sums and -1000 <= target <= 1000
            true_cases.add(f"candidate(root=tree_node({values!r}), targetSum={target})")
        if len(false_cases) < 300:
            target = rng.choice(
                [value for value in range(-1000, 1001) if value not in sums]
            )
            assert target not in sums and -1000 <= target <= 1000
            false_cases.add(
                f"candidate(root=tree_node({values!r}), targetSum={target})"
            )
    return sorted(true_cases | false_cases)


def _generate_current(seed: int = 0) -> list[str]:
    """Combine reproducible varied calls with explicit large and edge inputs."""
    cases = set(
        [
            "candidate(root=tree_node([1000]), targetSum=1000)",
            "candidate(root=tree_node([-1000]), targetSum=-1000)",
            "candidate(root=tree_node([1] * 5000), targetSum=13)",
            "candidate(root=tree_node([1] * 5000), targetSum=14)",
        ]
    )
    for call in _generate_base(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)


def generate(seed: int = 0) -> list[str]:
    """Include every legal statement example with seeded and boundary cases."""
    cases = set(
        [
            "candidate(root=tree_node([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]), targetSum=22)",
            "candidate(root=tree_node([1, 2, 3]), targetSum=5)",
            "candidate(root=tree_node([]), targetSum=0)",
        ]
    )
    for call in _generate_current(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)
