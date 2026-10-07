"""Seeded unique calls are constructed within the stated input constraints."""


def _generate_current(seed: int = 0) -> list[str]:
    import random

    r = random.Random(seed)
    cases = set()
    for _ in range(1000):
        arr = [r.randint(1, 8) for _ in range(r.randint(2, 100))]
        m = r.randint(1, 10)
        k = r.randint(2, 8)
        if m * k > len(arr):
            k = max(2, len(arr) // m)
        if m * k > len(arr):
            m = 1
            k = 2
        cases.add(f"candidate(arr={arr!r}, m={m}, k={k})")
        if len(cases) >= 600:
            break
    return sorted(cases)


def generate(seed: int = 0) -> list[str]:
    """Include every legal statement example with seeded and boundary cases."""
    cases = set(
        [
            "candidate(arr=[1, 2, 4, 4, 4, 4], m=1, k=3)",
            "candidate(arr=[1, 2, 1, 2, 1, 1, 1, 3], m=2, k=2)",
            "candidate(arr=[1, 2, 1, 2, 1, 3], m=2, k=3)",
        ]
    )
    for call in _generate_current(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)
