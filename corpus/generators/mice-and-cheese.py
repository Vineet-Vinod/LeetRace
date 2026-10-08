import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        n = rng.randint(1, 1000)
        reward1 = [rng.randint(1, 1000) for _ in range(n)]
        reward2 = [rng.randint(1, 1000) for _ in range(n)]
        k = rng.randint(0, n)
        calls.add(f"candidate(reward1={reward1!r}, reward2={reward2!r}, k={k})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(reward1=[1, 1, 3, 4], reward2=[4, 4, 1, 1], k=2)",
    "candidate(reward1=[1, 1], reward2=[1, 1], k=2)",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
