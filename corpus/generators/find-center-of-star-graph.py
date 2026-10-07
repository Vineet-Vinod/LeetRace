"""Each generated edge joins the chosen center to one distinct other label, forming a connected star."""


def _generate_base(seed: int = 0) -> list[str]:
    import random

    r = random.Random(seed)
    cases = set()
    for n in range(3, 80):
        for _ in range(10):
            center = r.randint(1, n)
            leaves = [x for x in range(1, n + 1) if x != center]
            r.shuffle(leaves)
            edges = [[center, x] if r.random() < 0.5 else [x, center] for x in leaves]
            r.shuffle(edges)
            cases.add(f"candidate(edges={edges!r})")
    return sorted(cases)


def _generate_current(seed: int = 0) -> list[str]:
    """Combine reproducible varied calls with explicit large and edge inputs."""
    cases = set(["candidate(edges=[[1, i] for i in range(2, 1002)])"])
    for call in _generate_base(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)


def generate(seed: int = 0) -> list[str]:
    """Include every legal statement example with seeded and boundary cases."""
    cases = set(
        [
            "candidate(edges=[[1, 2], [2, 3], [4, 2]])",
            "candidate(edges=[[1, 2], [5, 1], [1, 3], [1, 4]])",
        ]
    )
    for call in _generate_current(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)
