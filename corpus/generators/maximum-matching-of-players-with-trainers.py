import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        players = [rng.randint(1, 10**9) for _ in range(rng.randint(1, 500))]
        trainers = [rng.randint(1, 10**9) for _ in range(rng.randint(1, 500))]
        calls.add(f"candidate(players={players!r}, trainers={trainers!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(players=[1, 1, 1], trainers=[10])",
    "candidate(players=[4, 7, 9], trainers=[8, 2, 5, 8])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
