import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = {f"candidate(nums={[1000] * 10000!r})"}
    while len(calls) < 600:
        nums = [rng.randint(-1000, 1000) for _ in range(rng.randint(3, 1000))]
        calls.add(f"candidate(nums={nums!r})")
    return sorted(calls)
