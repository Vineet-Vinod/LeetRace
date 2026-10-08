import random


def generate(seed: int = 0) -> list[str]:
    """Generate legal positive arrays and include the maximum length of 1000."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    index = 0
    while len(calls) < 600:
        size = 1000 if index == 0 else 2 + index % 50
        nums = [rng.randint(1, 100_000) for _ in range(size)]
        assert 2 <= len(nums) <= 1000 and all(1 <= value <= 100_000 for value in nums)
        call = f"candidate(nums={nums!r})"
        index += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
