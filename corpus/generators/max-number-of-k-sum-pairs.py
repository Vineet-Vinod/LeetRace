import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    for case in range(300):
        target = 2 + rng.randrange(1999)
        pairs = rng.randrange(60)
        nums = []
        for _ in range(pairs):
            first = 1 + rng.randrange(target - 1)
            nums.extend((first, target - first))
        nums.extend(target + 1 + rng.randrange(1000) for _ in range(rng.randrange(40)))
        rng.shuffle(nums)
        calls.add(f"candidate(nums={nums!r}, k={target})")
    for case in range(300):
        target = 1 + rng.randrange(10**9)
        nums = [rng.randint(1, 10**9) for _ in range(1 + rng.randrange(80))]
        calls.add(f"candidate(nums={nums!r}, k={target})")
    calls.add(f"candidate(nums={[1] * 100_000!r}, k=2)")
    calls.add("candidate(nums=[1, 999999999] * 50000, k=1000000000)")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(nums=[1, 2, 3, 4], k=5)",
    "candidate(nums=[3, 1, 3, 4, 3], k=6)",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))


_AUDIT_BASE_GENERATE = generate
_AUDIT_BOUNDARY_CALLS = ("candidate(nums=[1, 1000000000, 999999999], k=1000000000)",)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_AUDIT_BASE_GENERATE(seed)) | set(_AUDIT_BOUNDARY_CALLS))
