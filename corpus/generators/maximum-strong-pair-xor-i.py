"""Seeded unique calls are constructed within the stated input constraints."""


def _generate_current(seed: int = 0) -> list[str]:
    import random

    r = random.Random(seed)
    cases = set()
    for _ in range(1000):
        nums = [r.randint(1, 100) for _ in range(r.randint(1, 50))]
        cases.add(f"candidate(nums={nums!r})")
        if len(cases) >= 600:
            break
    return sorted(cases)


def generate(seed: int = 0) -> list[str]:
    """Include every legal statement example with seeded and boundary cases."""
    cases = set(
        [
            "candidate(nums=[1, 2, 3, 4, 5])",
            "candidate(nums=[10, 100])",
            "candidate(nums=[5, 6, 25, 30])",
        ]
    )
    for call in _generate_current(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)
