"""Each k is selected from 1..len(nums), and all values stay within the stated range."""


def _generate_base(seed: int = 0) -> list[str]:
    import random

    r = random.Random(seed)
    cases = set()
    for _ in range(1000):
        nums = [r.randint(-100, 100) for _ in range(r.randint(1, 100))]
        k = r.randint(1, len(nums))
        cases.add(f"candidate(nums={nums!r}, k={k})")
        if len(cases) >= 600:
            break
    return sorted(cases)


def _generate_current(seed: int = 0) -> list[str]:
    """Combine reproducible varied calls with explicit large and edge inputs."""
    cases = set(["candidate(nums=list(range(-500, 500)), k=500)"])
    for call in _generate_base(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)


def generate(seed: int = 0) -> list[str]:
    """Include every legal statement example with seeded and boundary cases."""
    cases = set(
        [
            "candidate(nums=[2, 1, 3, 3], k=2)",
            "candidate(nums=[-1, -2, 3, 4], k=3)",
            "candidate(nums=[3, 4, 3, 3], k=2)",
        ]
    )
    for call in _generate_current(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)
