"""Seeded unique calls are constructed within the stated input constraints."""


def _generate_current(seed: int = 0) -> list[str]:
    import random

    r = random.Random(seed)
    values = {0, 1, -1, 2, -2, 2**30, 2**31 - 1, -(2**31)}
    values.update(2**i for i in range(31))
    values.update(r.randint(-(2**31), 2**31 - 1) for _ in range(600))
    return [f"candidate(n={n})" for n in sorted(values)]


def generate(seed: int = 0) -> list[str]:
    """Include every legal statement example with seeded and boundary cases."""
    cases = set(["candidate(n=1)", "candidate(n=16)", "candidate(n=3)"])
    for call in _generate_current(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)
