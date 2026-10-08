"""Every grid is rectangular, and dimensions, values, and k stay within their bounds."""


def _generate_base(seed: int = 0) -> list[str]:
    import random

    r = random.Random(seed)
    large = [[(i * 50 + j) % 2001 - 1000 for j in range(50)] for i in range(50)]
    cases = {f"candidate(grid={large!r}, k={k})" for k in (0, 1, 100)}
    while len(cases) < 600:
        m, n = r.randint(1, 20), r.randint(1, 20)
        grid = [[r.randint(-1000, 1000) for _ in range(n)] for _ in range(m)]
        k = r.randint(0, 100)
        cases.add(f"candidate(grid={grid!r}, k={k})")
    return sorted(cases)


def _generate_current(seed: int = 0) -> list[str]:
    """Combine reproducible varied calls with explicit large and edge inputs."""
    cases = set(
        [
            "candidate(grid=[[(i + j) % 2001 - 1000 for j in range(50)] for i in range(50)], k=100)"
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
            "candidate(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=1)",
            "candidate(grid=[[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]], k=4)",
            "candidate(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=9)",
        ]
    )
    for call in _generate_current(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)
