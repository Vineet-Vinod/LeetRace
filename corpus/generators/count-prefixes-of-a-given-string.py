"""Seeded unique calls are constructed within the stated input constraints."""


def _generate_base(seed: int = 0) -> list[str]:
    import random

    r = random.Random(seed)
    cases = set()
    for _ in range(1000):
        s = "".join(r.choice("abcd") for _ in range(r.randint(1, 10)))
        words = [
            "".join(r.choice("abcd") for _ in range(r.randint(1, 10)))
            for _ in range(r.randint(1, 30))
        ]
        cases.add(f"candidate(words={words!r}, s={s!r})")
        if len(cases) >= 600:
            break
    return sorted(cases)


def _generate_current(seed: int = 0) -> list[str]:
    """Combine reproducible varied calls with explicit large and edge inputs."""
    cases = set(["candidate(words=['a'] * 1000, s='a' * 10)"])
    for call in _generate_base(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)


def generate(seed: int = 0) -> list[str]:
    """Include every legal statement example with seeded and boundary cases."""
    cases = set(
        [
            "candidate(words=['a', 'b', 'c', 'ab', 'bc', 'abc'], s='abc')",
            "candidate(words=['a', 'a'], s='aa')",
        ]
    )
    for call in _generate_current(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)
