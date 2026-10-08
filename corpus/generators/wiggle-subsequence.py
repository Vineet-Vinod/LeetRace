import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set()
    for i in range(600):
        length = 1 + rng.randrange(200)
        if i % 3 == 0:
            nums = [rng.randrange(1001) for _ in range(length)]
        elif i % 3 == 1:
            nums = sorted(rng.randrange(1001) for _ in range(length))
        else:
            nums = [rng.randrange(5) for _ in range(length)]
        cases.add(f"candidate(nums={nums!r})")
    return sorted(cases)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(nums=[1, 2, 3, 4, 5, 6, 7, 8, 9])",
    "candidate(nums=[1, 7, 4, 9, 2, 5])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
