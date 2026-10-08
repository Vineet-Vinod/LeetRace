"""Seeded unique calls are constructed within the stated input constraints."""


def _generate_current(seed: int = 0) -> list[str]:
    import random

    r = random.Random(seed)
    cases = set()
    for _ in range(1000):
        s = "".join(r.choice("ABCDXYZ") for _ in range(r.randint(1, 100)))
        cases.add(f"candidate(s={s!r})")
        if len(cases) >= 600:
            break
    return sorted(cases)


def generate(seed: int = 0) -> list[str]:
    """Include every legal statement example with seeded and boundary cases."""
    cases = set(["candidate(s='ABFCACDB')", "candidate(s='ACBBD')"])
    for call in _generate_current(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)
