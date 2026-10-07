import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        size = rng.randint(1, 1000)
        mode = rng.randrange(3)
        start = rng.randint(1, 10**9 - size)
        nums = (
            [start + i for i in range(size)]
            if mode == 0
            else (
                [start] * size
                if mode == 1
                else [rng.randint(1, 10**9) for _ in range(size)]
            )
        )
        calls.add(f"candidate(nums={nums!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(nums=[1, 2, 3, 4, 5])",
    "candidate(nums=[4, 1, 3, 3])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
