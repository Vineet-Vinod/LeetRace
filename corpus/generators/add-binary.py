"""Seeded unique calls are constructed within the stated input constraints."""


def _generate_base(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        f"candidate(a={a!r}, b={b!r})"
        for a, b in [("0", "0"), ("1", "1"), ("1", "0"), ("11", "1"), ("1010", "1011")]
    }
    while len(cases) < 600:
        la, lb = rng.randint(1, 80), rng.randint(1, 80)
        a = (
            ("1" + "".join(rng.choice("01") for _ in range(la - 1)))
            if la > 1
            else rng.choice("01")
        )
        b = (
            ("1" + "".join(rng.choice("01") for _ in range(lb - 1)))
            if lb > 1
            else rng.choice("01")
        )
        cases.add(f"candidate(a={a!r}, b={b!r})")
    return sorted(cases)


def _generate_current(seed: int = 0) -> list[str]:
    """Combine reproducible varied calls with explicit large and edge inputs."""
    cases = set(["candidate(a='1' + '0' * 9999, b='1' + '0' * 9999)"])
    for call in _generate_base(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)


def generate(seed: int = 0) -> list[str]:
    """Include every legal statement example with seeded and boundary cases."""
    cases = set(["candidate(a='11', b='1')", "candidate(a='1010', b='1011')"])
    for call in _generate_current(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)
