def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    fast = {
        "candidate(nums=[2,3,1,1,4])",
        f"candidate(nums={[1000] * 10000!r})",
    }
    slow = {
        "candidate(nums=[0])",
        f"candidate(nums={[1] * 10000!r})",
    }
    while len(fast) < 300:
        n = rng.randint(2, 100)
        nums = [n - 1] + [rng.randint(0, 20) for _ in range(n - 1)]
        fast.add(f"candidate(nums={nums!r})")
    while len(slow) < 300:
        n = rng.randint(3, 100)
        first_jump = rng.randint(1, n - 2)
        nums = [first_jump] + [1] * (n - 1)
        slow.add(f"candidate(nums={nums!r})")
    return sorted(fast | slow)
