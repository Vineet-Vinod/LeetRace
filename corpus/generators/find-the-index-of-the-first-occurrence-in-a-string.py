"""Seeded unique calls are constructed within the stated input constraints."""


def _generate_base(seed: int = 0) -> list[str]:
    import random

    r = random.Random(seed)
    cases = set()
    for _ in range(1000):
        h = "".join(r.choice("abcde") for _ in range(r.randint(1, 100)))
        n = "".join(r.choice("abcde") for _ in range(r.randint(1, 20)))
        cases.add(f"candidate(haystack={h!r}, needle={n!r})")
        if len(cases) >= 600:
            break
    return sorted(cases)


def _generate_current(seed: int = 0) -> list[str]:
    """Combine reproducible varied calls with explicit large and edge inputs."""
    cases = set(["candidate(haystack='a' * 10000, needle='b' * 10000)"])
    for call in _generate_base(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)


def generate(seed: int = 0) -> list[str]:
    """Include every legal statement example with seeded and boundary cases."""
    cases = set(
        [
            "candidate(haystack='sadbutsad', needle='sad')",
            "candidate(haystack='leetcode', needle='leeto')",
        ]
    )
    for call in _generate_current(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)
