import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    calls.add("candidate(nums1=[2, 7, 11, 15], nums2=[1, 10, 4, 11])")
    while len(calls) < 600:
        size = rng.randint(1, 30)
        nums1 = [rng.randint(0, 100) for _ in range(size)]
        nums2 = [rng.randint(0, 100) for _ in range(size)]
        calls.add(f"candidate(nums1={nums1!r}, nums2={nums2!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = ("candidate(nums1=[12, 24, 8, 32], nums2=[13, 25, 32, 11])",)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
