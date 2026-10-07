"""Values are generated as 2*n integers, so the pair-count constraint always holds."""


def _generate_base(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    for n in range(1, 41):
        for _ in range(15):
            nums = [rng.randint(-10000, 10000) for _ in range(2 * n)]
            cases.add(f"candidate(nums={nums!r})")
    return sorted(cases)


def _generate_current(seed: int = 0) -> list[str]:
    """Combine reproducible varied calls with explicit large and edge inputs."""
    cases = set(["candidate(nums=list(range(-10000, 10000)))"])
    for call in _generate_base(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)


def generate(seed: int = 0) -> list[str]:
    """Include every legal statement example with seeded and boundary cases."""
    cases = set(["candidate(nums=[1, 4, 3, 2])", "candidate(nums=[6, 2, 6, 5, 1, 2])"])
    for call in _generate_current(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)
