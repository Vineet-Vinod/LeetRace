"""Every pick uses an in-range player index and a color in 0..10."""


def _generate_current(seed: int = 0) -> list[str]:
    import random

    r = random.Random(seed)
    cases = set()
    for _ in range(1000):
        n = r.randint(2, 10)
        pick = [[r.randrange(n), r.randint(0, 10)] for _ in range(r.randint(1, 100))]
        cases.add(f"candidate(n={n}, pick={pick!r})")
        if len(cases) >= 600:
            break
    return sorted(cases)


def generate(seed: int = 0) -> list[str]:
    """Include every legal statement example with seeded and boundary cases."""
    cases = set(
        [
            "candidate(n=4, pick=[[0, 0], [1, 0], [1, 0], [2, 1], [2, 1], [2, 0]])",
            "candidate(n=5, pick=[[1, 1], [1, 2], [1, 3], [1, 4]])",
            "candidate(n=5, pick=[[1, 1], [2, 4], [2, 4], [2, 4]])",
        ]
    )
    for call in _generate_current(seed):
        if len(cases) >= 999:
            break
        cases.add(call)
    return sorted(cases)
