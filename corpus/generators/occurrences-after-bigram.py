"""Seeded unique calls are constructed within the stated input constraints."""


def _generate_base(seed: int = 0) -> list[str]:
    import random

    r = random.Random(seed)
    cases = set()
    for _ in range(1000):
        words = [r.choice("abcdefghij") for _ in range(r.randint(3, 100))]
        first = r.choice(words)
        second = r.choice(words)
        cases.add(
            f"candidate(text={' '.join(words)!r}, first={first!r}, second={second!r})"
        )
        if len(cases) >= 600:
            break
    return sorted(cases)


def _generate_current(seed: int = 0) -> list[str]:
    """Combine reproducible varied calls with explicit large and edge inputs."""
    cases = set(["candidate(text=('a ' * 499) + 'a', first='a', second='a')"])
    for call in _generate_base(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)


def generate(seed: int = 0) -> list[str]:
    """Include every legal statement example with seeded and boundary cases."""
    cases = set(
        [
            "candidate(text='alice is a good girl she is a good student', first='a', second='good')",
            "candidate(text='we will we will rock you', first='we', second='will')",
        ]
    )
    for call in _generate_current(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)
