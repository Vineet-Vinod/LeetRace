def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    for _ in range(599):
        size = rng.randint(1, 60)
        nums = [rng.randint(1, 100) for _ in range(size)]
        total = size * (size + 1) // 2
        left = rng.randint(1, total)
        right = rng.randint(left, total)
        cases.add(f"candidate(nums={nums!r}, n={size}, left={left}, right={right})")
    nums = [rng.randint(1, 100) for _ in range(1000)]
    total = len(nums) * (len(nums) + 1) // 2
    cases.add(f"candidate(nums={nums!r}, n=1000, left=1, right={total})")
    assert len(cases) >= 500
    return sorted(cases)[:600]
