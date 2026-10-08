"""The key appears before exactly one target, giving a unique most frequent successor."""


def _generate_base(seed: int = 0) -> list[str]:
    import random

    r = random.Random(seed)
    cases = set()
    for _ in range(1000):
        key = r.randint(1, 1000)
        target = r.randint(1, 1000)
        nums = [key, target] + [
            x for x in (r.randint(1, 1000) for _ in range(r.randint(0, 98))) if x != key
        ]
        cases.add(f"candidate(nums={nums!r}, key={key})")
        if len(cases) >= 600:
            break
    return sorted(cases)


def _generate_current(seed: int = 0) -> list[str]:
    """Combine reproducible varied calls with explicit large and edge inputs."""
    cases = set(["candidate(nums=[1, 2] + [3] * 998, key=1)"])
    for call in _generate_base(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)


def generate(seed: int = 0) -> list[str]:
    """Include every legal statement example with seeded and boundary cases."""
    cases = set(
        [
            "candidate(nums=[1, 100, 200, 1, 100], key=1)",
            "candidate(nums=[2, 2, 2, 2, 3], key=2)",
        ]
    )
    for call in _generate_current(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)
