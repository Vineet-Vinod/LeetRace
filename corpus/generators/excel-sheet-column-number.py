"""Seeded unique calls are constructed within the stated input constraints."""


def _generate_current(seed: int = 0) -> list[str]:
    import random
    import string

    r = random.Random(seed)
    cases = {
        f"candidate(columnTitle={title!r})" for title in ("A", "Z", "AA", "FXSHRXW")
    }
    while len(cases) < 600:
        length = r.randint(1, 7)
        if length < 7:
            title = "".join(r.choice(string.ascii_uppercase) for _ in range(length))
        else:
            title = r.choice("ABCDE") + "".join(
                r.choice(string.ascii_uppercase) for _ in range(6)
            )
        cases.add(f"candidate(columnTitle={title!r})")
    return sorted(cases)


def generate(seed: int = 0) -> list[str]:
    """Include every legal statement example with seeded and boundary cases."""
    cases = set(
        [
            "candidate(columnTitle='A')",
            "candidate(columnTitle='AB')",
            "candidate(columnTitle='ZY')",
        ]
    )
    for call in _generate_current(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)
