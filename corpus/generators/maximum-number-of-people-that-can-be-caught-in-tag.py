import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        team = [rng.randint(0, 1) for _ in range(rng.randint(1, 1000))]
        dist = rng.randint(1, len(team))
        calls.add(f"candidate(team={team!r}, dist={dist})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(team=[0, 1, 0, 1, 0], dist=3)",
    "candidate(team=[1], dist=1)",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
