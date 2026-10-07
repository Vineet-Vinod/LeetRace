import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        size = rng.randint(1, 1000)
        mode = rng.randrange(3)
        nums = [rng.randint(0, 10**6) for _ in range(size)]
        if mode == 1:
            nums = [rng.randrange(1024) for _ in range(size)]
        elif mode == 2:
            nums = [value ^ value for value in nums]
        calls.add(f"candidate(nums={nums!r})")
    calls.add(f"candidate(nums={([1] * 100_000)!r})")
    calls.add(f"candidate(nums={([0] * 100_000)!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(nums=[1, 10, 4])",
    "candidate(nums=[4, 3, 1, 2, 4])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))


_AUDIT_BASE_GENERATE = generate
_AUDIT_BOUNDARY_CALLS = ("candidate(nums=[1000000])",)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_AUDIT_BASE_GENERATE(seed)) | set(_AUDIT_BOUNDARY_CALLS))
