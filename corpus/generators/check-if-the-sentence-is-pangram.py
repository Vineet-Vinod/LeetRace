"""Seeded unique calls are constructed within the stated input constraints."""


def _generate_base(seed: int = 0) -> list[str]:
    import random
    import string

    rng = random.Random(seed)
    cases = set()
    cases.add(f"candidate(sentence={string.ascii_lowercase!r})")
    while len(cases) < 600:
        letters = list(string.ascii_lowercase if rng.random() < 0.5 else "")
        letters += [
            rng.choice(string.ascii_lowercase) for _ in range(rng.randint(1, 60))
        ]
        rng.shuffle(letters)
        cases.add(f"candidate(sentence={''.join(letters)!r})")
    return sorted(cases)


def _generate_current(seed: int = 0) -> list[str]:
    """Combine reproducible varied calls with explicit large and edge inputs."""
    cases = set(["candidate(sentence=('a' * 975) + 'bcdefghijklmnopqrstuvwxyz')"])
    for call in _generate_base(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)


def generate(seed: int = 0) -> list[str]:
    """Include every legal statement example with seeded and boundary cases."""
    cases = set(
        [
            "candidate(sentence='thequickbrownfoxjumpsoverthelazydog')",
            "candidate(sentence='leetcode')",
        ]
    )
    for call in _generate_current(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)
