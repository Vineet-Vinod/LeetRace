"""Seeded unique calls are constructed within the stated input constraints."""


def _generate_base(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    alphabet = "abcxyz"
    for _ in range(1000):
        words = [
            "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 10)))
            for _ in range(rng.randint(1, 8))
        ]
        search = "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 8)))
        cases.add(f"candidate(sentence={' '.join(words)!r}, searchWord={search!r})")
        if len(cases) >= 600:
            break
    return sorted(cases)


def _generate_current(seed: int = 0) -> list[str]:
    """Combine reproducible varied calls with explicit large and edge inputs."""
    cases = set(
        ["candidate(sentence=('a' * 89) + ' ' + ('b' * 10), searchWord='b' * 10)"]
    )
    for call in _generate_base(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)


def generate(seed: int = 0) -> list[str]:
    """Include every legal statement example with seeded and boundary cases."""
    cases = set(
        [
            "candidate(sentence='i love eating burger', searchWord='burg')",
            "candidate(sentence='this problem is an easy problem', searchWord='pro')",
            "candidate(sentence='i am tired', searchWord='you')",
        ]
    )
    for call in _generate_current(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)
