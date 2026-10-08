"""Inputs are sets of distinct two-letter lowercase words."""


def _generate_base(seed: int = 0) -> list[str]:
    import random

    r = random.Random(seed)
    cases = set()
    for _ in range(1200):
        words = set()
        while len(words) < r.randint(1, 20):
            w = "".join(r.choice("abcdefghij") for _ in range(2))
            words.add(w)
        cases.add(f"candidate(words={sorted(words)!r})")
        if len(cases) >= 600:
            break
    return sorted(cases)


def _generate_current(seed: int = 0) -> list[str]:
    """Combine reproducible varied calls with explicit large and edge inputs."""
    cases = set(
        [
            "candidate(words=['aa','ab','ac','ad','ae','af','ag','ah','ai','aj','ba','bb','bc','bd','be','bf','bg','bh','bi','bj','ca','cb','cc','cd','ce','cf','cg','ch','ci','cj','da','db','dc','dd','de','df','dg','dh','di','dj','ea','eb','ec','ed','ee','ef','eg','eh','ei','ej'])"
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
            "candidate(words=['cd', 'ac', 'dc', 'ca', 'zz'])",
            "candidate(words=['ab', 'ba', 'cc'])",
            "candidate(words=['aa', 'ab'])",
        ]
    )
    for call in _generate_current(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)
