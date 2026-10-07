"""tree_node receives only values, producing valid trees within the node and value limits."""


def _generate_base(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(["candidate(root=tree_node([]))"])
    for n in range(1, 60):
        for _ in range(12):
            vals = [rng.randint(-100, 100) for _ in range(n)]
            cases.add(f"candidate(root=tree_node({vals!r}))")
    return sorted(cases)


def _generate_current(seed: int = 0) -> list[str]:
    """Combine reproducible varied calls with explicit large and edge inputs."""
    cases = set(["candidate(root=tree_node(list(range(100))))"])
    for call in _generate_base(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)


def generate(seed: int = 0) -> list[str]:
    """Include every legal statement example with seeded and boundary cases."""
    cases = set(
        [
            "candidate(root=tree_node([1, None, 2, 3]))",
            "candidate(root=tree_node([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]))",
            "candidate(root=tree_node([]))",
            "candidate(root=tree_node([1]))",
        ]
    )
    for call in _generate_current(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)
