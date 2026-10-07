import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    fixed = [
        ([1, 0, -1, 0, -2, 2], 0),
        ([2, 2, 2, 2, 2], 8),
        ([0, 0, 0, 0], 0),
        ([-(10**9), 10**9, 0, 1], 1),
    ]
    for nums, target in fixed:
        calls.add(f"candidate(nums={nums!r}, target={target})")
    while len(calls) < 600:
        size = rng.randint(1, 12)
        nums = [rng.randint(-30, 30) for _ in range(size)]
        if rng.random() < 0.35:
            target = sum(rng.sample(nums, 4)) if size >= 4 else rng.randint(-80, 80)
        else:
            target = rng.randint(-80, 80)
        calls.add(f"candidate(nums={nums!r}, target={target})")
    return sorted(calls)
