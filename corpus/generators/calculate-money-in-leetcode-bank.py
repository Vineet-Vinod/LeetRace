"""Seeded unique calls are constructed within the stated input constraints."""


def _generate_current(seed: int = 0) -> list[str]:
    # Include the week boundaries and the maximum n while staying below 999 cases.
    values = set(range(1, 593))
    values.update((6, 7, 8, 13, 14, 15, 999, 1000))
    return [f"candidate(n={n})" for n in sorted(values)]


def generate(seed: int = 0) -> list[str]:
    """Include every legal statement example with seeded and boundary cases."""
    cases = set(["candidate(n=4)", "candidate(n=10)", "candidate(n=20)"])
    for call in _generate_current(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)
