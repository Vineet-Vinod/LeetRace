import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set()
    for i in range(600):
        length = 1 + rng.randrange(80)
        nums = [rng.randint(-10000, 10000) for _ in range(length)]
        queries = [
            [rng.randint(-10000, 10000), rng.randrange(length)]
            for _ in range(1 + rng.randrange(80))
        ]
        cases.add(f"candidate(nums={nums!r}, queries={queries!r})")
    return sorted(cases)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(nums=[1, 2, 3, 4], queries=[[1, 0], [-3, 1], [-4, 0], [2, 3]])",
    "candidate(nums=[1], queries=[[4, 0]])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
