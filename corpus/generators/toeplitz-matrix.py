"""Seeded unique calls are constructed within the stated input constraints."""


def _generate_base(seed: int = 0) -> list[str]:
    import random

    r = random.Random(seed)
    cases = set()
    for _ in range(1000):
        m, n = r.randint(1, 20), r.randint(1, 20)
        matrix = [[r.randint(0, 99) for _ in range(n)] for _ in range(m)]
        if r.random() < 0.5:
            for i in range(1, m):
                for j in range(1, n):
                    matrix[i][j] = matrix[i - 1][j - 1]
        cases.add(f"candidate(matrix={matrix!r})")
        if len(cases) >= 600:
            break
    return sorted(cases)


def _generate_current(seed: int = 0) -> list[str]:
    """Combine reproducible varied calls with explicit large and edge inputs."""
    cases = set(
        ["candidate(matrix=[[j - i + 19 for j in range(20)] for i in range(20)])"]
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
            "candidate(matrix=[[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]])",
            "candidate(matrix=[[1, 2], [2, 2]])",
        ]
    )
    for call in _generate_current(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)
