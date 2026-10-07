"""The endpoints are distinct valid stop indices and every edge distance is nonnegative."""


def _generate_base(seed: int = 0) -> list[str]:
    import random

    r = random.Random(seed)
    cases = set()
    for n in range(2, 80):
        for _ in range(10):
            d = [r.randint(1, 1000) for _ in range(n)]
            a = r.randrange(n)
            b = r.randrange(n - 1)
            b += b >= a
            cases.add(f"candidate(distance={d!r}, start={a}, destination={b})")
    return sorted(cases)


def _generate_current(seed: int = 0) -> list[str]:
    """Combine reproducible varied calls with explicit large and edge inputs."""
    cases = set(["candidate(distance=[1] * 10000, start=0, destination=9999)"])
    for call in _generate_base(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)


def generate(seed: int = 0) -> list[str]:
    """Include every legal statement example with seeded and boundary cases."""
    cases = set(
        [
            "candidate(distance=[1, 2, 3, 4], start=0, destination=1)",
            "candidate(distance=[1, 2, 3, 4], start=0, destination=2)",
            "candidate(distance=[1, 2, 3, 4], start=0, destination=3)",
        ]
    )
    for call in _generate_current(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)
