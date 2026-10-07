"""The generator enumerates every legal n from 0 through 100."""

DOMAIN_SIZE = 101


def _generate_current(seed: int = 0) -> list[str]:
    return [f"candidate(n={n})" for n in range(101)]


def generate(seed: int = 0) -> list[str]:
    """Include every legal statement example with seeded and boundary cases."""
    cases = set(["candidate(n=7)", "candidate(n=2)", "candidate(n=3)"])
    for call in _generate_current(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)
