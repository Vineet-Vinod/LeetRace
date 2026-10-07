import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        questions = [
            [rng.randint(1, 100000), rng.randint(1, 100000)]
            for _ in range(rng.randint(1, 1000))
        ]
        calls.add(f"candidate(questions={questions!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(questions=[[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]])",
    "candidate(questions=[[3, 2], [4, 3], [4, 4], [2, 5]])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
