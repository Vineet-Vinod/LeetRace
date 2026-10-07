import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = {f"candidate(nums={[1] * 100000!r})"}
    while len(calls) < 600:
        nums = [rng.randrange(2) for _ in range(rng.randint(1, 1000))]
        calls.add(f"candidate(nums={nums!r})")
    return sorted(calls)
