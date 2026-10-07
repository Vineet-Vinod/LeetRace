import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        n = rng.randint(1, 10000)
        positions = rng.sample(range(n + 1), rng.randint(1, min(n + 1, 100)))
        rng.shuffle(positions)
        split = rng.randint(0, len(positions))
        left, right = positions[:split], positions[split:]
        calls.add(f"candidate(n={n}, left={left!r}, right={right!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(n=4, left=[4, 3], right=[0, 1])",
    "candidate(n=7, left=[], right=[0, 1, 2, 3, 4, 5, 6, 7])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
