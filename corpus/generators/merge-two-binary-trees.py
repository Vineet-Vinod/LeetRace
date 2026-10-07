"""Seeded unique calls are constructed within the stated input constraints."""


def _generate_base(seed: int = 0) -> list[str]:
    import random

    r = random.Random(seed)
    cases = set()
    for _ in range(1000):
        n = r.randint(0, 30)
        m = r.randint(0, 30)
        a = [r.randint(-100, 100) for _ in range(n)]
        b = [r.randint(-100, 100) for _ in range(m)]
        cases.add(f"candidate(root1=tree_node({a!r}), root2=tree_node({b!r}))")
        if len(cases) >= 600:
            break
    return sorted(cases)


def _generate_current(seed: int = 0) -> list[str]:
    """Combine reproducible varied calls with explicit large and edge inputs."""
    cases = set(
        ["candidate(root1=tree_node([10000] * 1000), root2=tree_node([-10000] * 1000))"]
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
            "candidate(root1=tree_node([1, 3, 2, 5]), root2=tree_node([2, 1, 3, None, 4, None, 7]))",
            "candidate(root1=tree_node([1]), root2=tree_node([1, 2]))",
        ]
    )
    for call in _generate_current(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)
