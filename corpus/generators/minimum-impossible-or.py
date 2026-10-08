import random


def generate(seed: int = 0) -> list[str]:
    """Construct prefixes of present powers of two to force diverse missing powers."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    for count in range(30):
        nums = [1 << bit for bit in range(count)] or [2]
        call = f"candidate(nums={nums!r})"
        seen.add(call)
        calls.append(call)
    calls.append(f"candidate(nums={[1 << bit for bit in range(30)]!r})")
    seen.add(calls[-1])
    calls.extend(["candidate(nums=[1000000000])"])
    seen.add(calls[-1])
    boundary = [1] * 100_000
    calls.append(f"candidate(nums={boundary!r})")
    seen.add(calls[-1])

    index = 0
    while len(calls) < 600:
        present_count = rng.randrange(0, 30)
        nums = [1 << bit for bit in range(present_count)]
        nums.extend(rng.randint(1, 10**9) for _ in range(rng.randint(1, 30)))
        rng.shuffle(nums)
        assert 1 <= len(nums) <= 100_000
        assert all(1 <= value <= 10**9 for value in nums)
        call = f"candidate(nums={nums!r})"
        index += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
