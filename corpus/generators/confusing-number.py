"""Uses valid n values across the full range, with confusing rotations and bounds."""


def _generate_base(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    values = {
        0,
        1,
        6,
        8,
        9,
        10,
        11,
        16,
        68,
        69,
        86,
        89,
        96,
        98,
        8000,
        100000000,
        100000001,
        999999998,
        999999999,
        1000000000,
    }
    while len(values) < 600:
        if rng.random() < 0.4:
            digits = "".join(rng.choice("01689") for _ in range(rng.randint(1, 9)))
            digits = str(rng.randint(1, 9)) + digits[1:]
            values.add(int(digits))
        else:
            values.add(rng.randint(0, 1000000000))
    return [f"candidate(n={value})" for value in sorted(values)]


def _generate_current(seed: int = 0) -> list[str]:
    """Combine reproducible varied calls with explicit large and edge inputs."""
    cases = set(
        [
            "candidate(n=1000000000)",
            "candidate(n=9861)",
            "candidate(n=8000000)",
            "candidate(n=100000001)",
            "candidate(n=999999999)",
        ]
    )
    for call in _generate_base(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)


def generate(seed: int = 0) -> list[str]:
    """Include every legal statement example with seeded and boundary cases."""
    cases = set(["candidate(n=6)", "candidate(n=89)", "candidate(n=11)"])
    for call in _generate_current(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)
