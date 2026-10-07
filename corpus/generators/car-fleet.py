import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    calls.add("candidate(target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3])")
    while len(calls) < 600:
        n = rng.randint(1, 35)
        target = rng.randint(n, 1000)
        positions = sorted(rng.sample(range(target), n))
        speeds = [rng.randint(1, 100) for _ in range(n)]
        calls.add(
            f"candidate(target={target}, position={positions!r}, speed={speeds!r})"
        )
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = ("candidate(target=10, position=[3], speed=[3])",)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
