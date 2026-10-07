"""Seeded unique calls are constructed within the stated input constraints."""


def _generate_base(seed: int = 0) -> list[str]:
    import random

    r = random.Random(seed)
    cases = set()
    for _ in range(1000):
        arrays = [
            [r.randrange(0, 101) for _ in range(r.randint(1, 10))] for _ in range(3)
        ]
        cases.add(f"candidate(a={arrays[0]!r}, b={arrays[1]!r}, c={arrays[2]!r})")
        if len(cases) >= 600:
            break
    return sorted(cases)


def _generate_current(seed: int = 0) -> list[str]:
    """Combine reproducible varied calls with explicit large and edge inputs."""
    cases = set(
        ["candidate(a=list(range(100)), b=list(range(100)), c=list(range(100)) )"]
    )
    for call in _generate_base(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)


def generate(seed: int = 0) -> list[str]:
    """Include every legal statement example with seeded and boundary cases."""
    cases = set(
        ["candidate(a=[1], b=[2], c=[3])", "candidate(a=[1, 1], b=[2, 3], c=[1, 5])"]
    )
    for call in _generate_current(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)
