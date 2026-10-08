import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    for case in range(300):
        size = 2 + rng.randrange(100)
        nums = [rng.randint(-10_000, 10_000) for _ in range(size)]
        left = rng.randrange(size)
        right = rng.randrange(left, size)
        k = sum(nums[left : right + 1])
        assert -(10**9) <= k <= 10**9
        calls.add(f"candidate(nums={nums!r}, k={k})")
    for case in range(300):
        nums = [rng.randint(-10_000, 10_000) for _ in range(1 + rng.randrange(100))]
        calls.add(f"candidate(nums={nums!r}, k=1000000000)")
    calls.add(f"candidate(nums={[0] * 200_000!r}, k=0)")
    calls.add(f"candidate(nums={[1] * 200_000!r}, k=200000)")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(nums=[-2, -1, 2, 1], k=1)",
    "candidate(nums=[1, -1, 5, -2, 3], k=3)",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))


_AUDIT_BASE_GENERATE = generate
_AUDIT_BOUNDARY_CALLS = ("candidate(nums=[10000, -10000], k=0)",)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_AUDIT_BASE_GENERATE(seed)) | set(_AUDIT_BOUNDARY_CALLS))
