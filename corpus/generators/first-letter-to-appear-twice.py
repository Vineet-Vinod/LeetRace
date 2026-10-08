"""Each generated string is built from unique letters plus a guaranteed duplicate."""


def _generate_current(seed: int = 0) -> list[str]:
    import random
    import string

    r = random.Random(seed)
    cases = set()
    for _ in range(1000):
        chars = list(string.ascii_lowercase)
        r.shuffle(chars)
        size = r.randint(1, 26)
        unique = chars[:size]
        repeat = r.choice(unique)
        pos = r.randrange(len(unique) + 1)
        s = unique[:pos] + [repeat] + unique[pos:]
        r.shuffle(s)
        cases.add(f"candidate(s={''.join(s)!r})")
        if len(cases) >= 600:
            break
    return sorted(cases)


def generate(seed: int = 0) -> list[str]:
    """Include every legal statement example with seeded and boundary cases."""
    cases = set(["candidate(s='abccbaacz')", "candidate(s='abcdd')"])
    for call in _generate_current(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)
