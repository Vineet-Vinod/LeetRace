import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    for case in range(300):
        k = 1 + rng.randrange(1000)
        divisors = [value for value in range(1, k + 1) if k % value == 0]
        nums = [rng.choice(divisors) for _ in range(1 + rng.randrange(80))]
        nums[0] = k
        calls.add(f"candidate(nums={nums!r}, k={k})")
    for case in range(300):
        k = 2 + rng.randrange(998)
        nums = [k + 1 + rng.randrange(1000 - k) for _ in range(1 + rng.randrange(80))]
        calls.add(f"candidate(nums={nums!r}, k={k})")
    calls.add(f"candidate(nums={[1] * 1000!r}, k=1)")
    calls.add(f"candidate(nums={[1] * 1000!r}, k=1000)")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(nums=[3, 6, 2, 7, 1], k=6)",
    "candidate(nums=[3], k=2)",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))


_AUDIT_BASE_GENERATE = generate
_AUDIT_BOUNDARY_CALLS = (
    "candidate(nums=[1000] * 1000, k=1000)",
    "candidate(nums=[999] * 1000, k=1000)",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_AUDIT_BASE_GENERATE(seed)) | set(_AUDIT_BOUNDARY_CALLS))
