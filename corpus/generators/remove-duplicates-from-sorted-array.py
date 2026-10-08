"""Inputs are sorted; the wrapper captures both k and the mutated unique prefix."""


def _generate_base(seed: int = 0) -> list[str]:
    import random

    r = random.Random(seed)
    cases = set()
    for _ in range(1000):
        nums = sorted(r.randint(-100, 100) for _ in range(r.randint(1, 200)))
        # The wrapper returns both the result and the required in-place prefix.
        cases.add(
            f"(lambda nums: (lambda k: (k, nums[:k]))(candidate(nums)))({nums!r})"
        )
        if len(cases) >= 600:
            break
    return sorted(cases)


def _generate_current(seed: int = 0) -> list[str]:
    """Combine reproducible varied calls with explicit large and edge inputs."""
    cases = set(
        [
            "(lambda nums: (lambda k: (k, nums[:k]))(candidate(nums)))(sorted((i % 201) - 100 for i in range(30000)))"
        ]
    )
    for call in _generate_base(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)


def generate(seed: int = 0) -> list[str]:
    """Include every legal statement example with seeded and boundary cases."""
    cases = set(
        ["candidate(nums=[1, 1, 2])", "candidate(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4])"]
    )
    for call in _generate_current(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)
