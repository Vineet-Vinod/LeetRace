import random


def generate(seed: int = 0) -> list[str]:
    """Mix constructively reachable arrays with arrays trapped behind zero jumps."""
    rng = random.Random(seed)
    calls: list[str] = [
        f"candidate(nums={[0] * 10_000!r})",
        f"candidate(nums={[100_000] * 10_000!r})",
        f"candidate(nums={[1] + [0] * 9_999!r})",
    ]
    seen: set[str] = set(calls)
    index = 0
    while len(calls) < 300:
        length = 2 + index % 100
        nums = [rng.randint(1, 100_000) for _ in range(length)]
        call = f"candidate(nums={nums!r})"
        index += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    while len(calls) < 600:
        length = 5 + index % 100
        nums = [0] * length
        nums[0] = rng.randint(1, min(3, length - 2))
        assert 1 <= len(nums) <= 10_000 and all(0 <= jump <= 100_000 for jump in nums)
        call = f"candidate(nums={nums!r})"
        index += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
