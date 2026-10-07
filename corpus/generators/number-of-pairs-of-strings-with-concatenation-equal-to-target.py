import random


def generate(seed: int = 0) -> list[str]:
    """Mix random digit strings with cases containing a guaranteed concatenation pair."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    index = 0

    while len(calls) < 300:
        first = str(rng.randint(1, 10**30))
        second = str(rng.randint(1, 10**30))
        target = first + second
        nums = [first, second]
        nums.extend(str(rng.randint(1, 10**30)) for _ in range(index % 18))
        call = f"candidate(nums={nums!r}, target={target!r})"
        index += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)

    nums = ["9" * 50, "8" * 50] + [str(i + 1) for i in range(98)]
    calls.append(f"candidate(nums={nums!r}, target={'9' * 50 + '8' * 50!r})")
    seen.add(calls[-1])

    while len(calls) < 600:
        target = str(rng.randint(10, 10**12))
        nums = [str(rng.randint(1, 10**20)) for _ in range(2 + index % 15)]
        call = f"candidate(nums={nums!r}, target={target!r})"
        index += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
