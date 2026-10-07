"""Seeded unique calls are constructed within the stated input constraints."""


def _generate_current(seed: int = 0) -> list[str]:
    import random

    r = random.Random(seed)
    cases = set()
    for _ in range(1000):
        nums = [r.randint(1, 100) for _ in range(r.randint(1, 100))]
        cases.add(f"candidate(nums={nums!r})")
        if len(cases) >= 600:
            break
    return sorted(cases)


def generate(seed: int = 0) -> list[str]:
    """Include every legal statement example with seeded and boundary cases."""
    cases = set(
        [
            "candidate(nums=[34, 23, 1, 24, 75, 33, 54, 8])",
            "candidate(nums=[99, 77, 33, 66, 55])",
        ]
    )
    for call in _generate_current(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)
