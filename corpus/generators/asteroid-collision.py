import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    calls.add("candidate(asteroids=[5, 10, -5])")
    calls.add("candidate(asteroids=[8, -8])")
    while len(calls) < 600:
        size = rng.randint(2, 50)
        asteroids = [rng.choice((-1, 1)) * rng.randint(1, 1000) for _ in range(size)]
        calls.add(f"candidate(asteroids={asteroids!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = ("candidate(asteroids=[10, 2, -5])",)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
