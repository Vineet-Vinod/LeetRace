"""Seeded unique calls are constructed within the stated input constraints."""


def _generate_base(seed: int = 0) -> list[str]:
    import random
    import string

    r = random.Random(seed)
    cases = set()
    for _ in range(1000):
        n = r.randint(2, 1000)
        durations = []
        current = 0
        for _ in range(n):
            current += r.randint(1, 1000)
            durations.append(current)
        keys = "".join(r.choice(string.ascii_lowercase) for _ in range(n))
        cases.add(f"candidate(releaseTimes={durations!r}, keysPressed={keys!r})")
        if len(cases) >= 600:
            break
    return sorted(cases)


def _generate_current(seed: int = 0) -> list[str]:
    """Combine reproducible varied calls with explicit large and edge inputs."""
    cases = set(
        ["candidate(releaseTimes=list(range(1, 1001)), keysPressed='a' * 1000)"]
    )
    for call in _generate_base(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)


def generate(seed: int = 0) -> list[str]:
    """Include every legal statement example with seeded and boundary cases."""
    cases = set(
        [
            "candidate(releaseTimes=[9, 29, 49, 50], keysPressed='cbcd')",
            "candidate(releaseTimes=[12, 23, 36, 46, 62], keysPressed='spuda')",
        ]
    )
    for call in _generate_current(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)
