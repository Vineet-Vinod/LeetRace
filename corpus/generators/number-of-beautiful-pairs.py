"""Values stay in 1..9999 and have nonzero last digits as required."""


def _generate_base(seed: int = 0) -> list[str]:
    import random

    r = random.Random(seed)
    cases = set()
    for _ in range(1000):
        nums = []
        for _ in range(r.randint(2, 100)):
            value = r.randint(1, 9999)
            while value % 10 == 0:
                value = r.randint(1, 9999)
            nums.append(value)
        cases.add(f"candidate(nums={nums!r})")
        if len(cases) >= 600:
            break
    return sorted(cases)


def _generate_current(seed: int = 0) -> list[str]:
    """Combine reproducible varied calls with explicit large and edge inputs."""
    cases = set(["candidate(nums=[9999] * 100)"])
    for call in _generate_base(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)


def generate(seed: int = 0) -> list[str]:
    """Include every legal statement example with seeded and boundary cases."""
    cases = set(["candidate(nums=[2, 5, 1, 4])", "candidate(nums=[11, 21, 12])"])
    for call in _generate_current(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)
