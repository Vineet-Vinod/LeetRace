"""Seeded unique calls are constructed within the stated input constraints."""


def _generate_base(seed: int = 0) -> list[str]:
    import random
    import string

    r = random.Random(seed)
    cases = set()
    alphabet = string.ascii_letters + string.digits + "'!?.,"
    for _ in range(1000):
        words = [
            "".join(r.choice(alphabet) for _ in range(r.randint(1, 40)))
            for _ in range(r.randint(1, 30))
        ]
        cases.add(f"candidate(s={' '.join(words)!r})")
        if len(cases) >= 600:
            break
    return sorted(cases)


def _generate_current(seed: int = 0) -> list[str]:
    """Combine reproducible varied calls with explicit large and edge inputs."""
    cases = set(["candidate(s='a' * 49999 + 'b')"])
    for call in _generate_base(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)


def generate(seed: int = 0) -> list[str]:
    """Include every legal statement example with seeded and boundary cases."""
    cases = set(
        ['candidate(s="Let\'s take LeetCode contest")', "candidate(s='Mr Ding')"]
    )
    for call in _generate_current(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)
