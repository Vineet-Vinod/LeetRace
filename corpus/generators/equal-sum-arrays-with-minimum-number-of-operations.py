import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        n1 = rng.randint(1, 1000)
        n2 = rng.randint(1, 1000)
        nums1 = [rng.randint(1, 6) for _ in range(n1)]
        nums2 = [rng.randint(1, 6) for _ in range(n2)]
        calls.add(f"candidate(nums1={nums1!r}, nums2={nums2!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(nums1=[1, 1, 1, 1, 1, 1, 1], nums2=[6])",
    "candidate(nums1=[1, 2, 3, 4, 5, 6], nums2=[1, 1, 2, 2, 2, 2])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
