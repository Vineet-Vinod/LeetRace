import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        arrays = [
            [rng.randint(0, 10**9) for _ in range(rng.randint(1, 40))] for _ in range(3)
        ]
        calls.add(f"candidate(a={arrays[0]!r}, b={arrays[1]!r}, c={arrays[2]!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(a=[1, 1], b=[2, 3], c=[1, 5])",
    "candidate(a=[1], b=[2], c=[3])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
