import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = {f"candidate(nums={list(range(-5000, 5000))!r}, target=9999)"}
    while len(calls) < 600:
        size = rng.randint(1, 1000)
        nums = sorted(rng.sample(range(-9999, 10000), size))
        target = rng.choice(nums) if rng.randrange(2) else rng.randint(-9999, 9999)
        calls.add(f"candidate(nums={nums!r}, target={target})")
    return sorted(calls)
