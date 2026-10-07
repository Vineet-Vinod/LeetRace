import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    calls.add("candidate(windows=[1, 2, 3], queries=[3, 3, 2])")
    while len(calls) < 600:
        size = rng.randint(1, 40)
        windows = list(range(1, size + 1))
        rng.shuffle(windows)
        queries = [rng.randint(1, size) for _ in range(rng.randint(1, 40))]
        calls.add(f"candidate(windows={windows!r}, queries={queries!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = ("candidate(windows=[1, 4, 2, 3], queries=[4, 1, 3])",)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
