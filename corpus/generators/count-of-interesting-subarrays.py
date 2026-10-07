import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    for case in range(300):
        modulo = 1 + rng.randrange(12)
        k = rng.randrange(modulo)
        nums = [rng.randint(1, 10**9) for _ in range(1 + rng.randrange(80))]
        if case % 4:
            residue_value = k if k else modulo
            for index in range(case % 3, len(nums), 4):
                nums[index] = residue_value + modulo * rng.randrange(
                    max(1, (10**9 - residue_value) // modulo + 1)
                )
        calls.add(f"candidate(nums={nums!r}, modulo={modulo}, k={k})")
    for case in range(300):
        modulo = 1 + rng.randrange(12)
        k = rng.randrange(modulo)
        nums = [rng.randint(1, 10**9) for _ in range(1 + rng.randrange(80))]
        residue_value = k if k else modulo
        nums = [
            value
            if value % modulo != k
            else (value + 1 if value < 10**9 else value - 1)
            for value in nums
        ]
        if all(value % modulo == k for value in nums):
            nums[0] = 10**9 - ((10**9 - (k if k else modulo)) % modulo) - modulo
        calls.add(f"candidate(nums={nums!r}, modulo={modulo}, k={k})")
    calls.add(f"candidate(nums={[1] * 100_000!r}, modulo=2, k=1)")
    calls.add(f"candidate(nums={[1] * 100_000!r}, modulo=10**9, k=999_999_999)")
    assert len(calls) == 602
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(nums=[3, 1, 9, 6], modulo=3, k=0)",
    "candidate(nums=[3, 2, 4], modulo=2, k=1)",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))


_AUDIT_BASE_GENERATE = generate
_AUDIT_BOUNDARY_CALLS = ("candidate(nums=[1, 1000000000], modulo=1000000000, k=0)",)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_AUDIT_BASE_GENERATE(seed)) | set(_AUDIT_BOUNDARY_CALLS))
