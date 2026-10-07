import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    for case in range(300):
        size = 1 + rng.randrange(100)
        nums = list(range(size))
        index = rng.randrange(size - 1) if size > 1 else 0
        if size > 1:
            nums[index], nums[index + 1] = nums[index + 1], nums[index]
        calls.add(f"candidate(nums={nums!r})")
    for case in range(300):
        size = 3 + rng.randrange(100)
        nums = list(range(size))
        index = rng.randrange(size - 2)
        nums[index], nums[index + 2] = nums[index + 2], nums[index]
        calls.add(f"candidate(nums={nums!r})")
    calls.add(f"candidate(nums={list(range(100_000))!r})")
    maximum_false = list(range(100_000))
    maximum_false[0], maximum_false[2] = maximum_false[2], maximum_false[0]
    calls.add(f"candidate(nums={maximum_false!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = ("candidate(nums=[1, 2, 0])",)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
