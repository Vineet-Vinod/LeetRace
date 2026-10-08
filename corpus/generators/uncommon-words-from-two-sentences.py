"""Sentences contain lowercase words separated by single spaces with no edge spaces."""


def _generate_base(seed: int = 0) -> list[str]:
    import random

    r = random.Random(seed)
    cases = set()
    for _ in range(1000):
        words = [
            "".join(r.choice("abcd") for _ in range(r.randint(1, 8)))
            for _ in range(r.randint(1, 20))
        ]
        split = r.randint(1, len(words))
        a = " ".join(words[:split])
        b = " ".join(words[split:] or [r.choice(words)])
        cases.add(f"candidate(s1={a!r}, s2={b!r})")
        if len(cases) >= 600:
            break
    return sorted(cases)


def _generate_current(seed: int = 0) -> list[str]:
    """Combine reproducible varied calls with explicit large and edge inputs."""
    cases = set(
        [
            "candidate(s1=' '.join(['abcdefgh'] * 22), s2=' '.join(['abcdefgh'] * 21 + ['abcdefgi']))"
        ]
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
            "candidate(s1='this apple is sweet', s2='this apple is sour')",
            "candidate(s1='apple apple', s2='banana')",
        ]
    )
    for call in _generate_current(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)
