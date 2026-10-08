def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    possible = {
        "candidate(nums=[1,1],changeIndices=[1,2,1,2])",
        f"candidate(nums={[0] * 2000!r},changeIndices={list(range(1, 2001))!r})",
        f"candidate(nums={[1] * 1000!r},changeIndices={list(range(1, 1001)) + list(range(1, 1001))!r})",
    }
    impossible = {"candidate(nums=[0,0],changeIndices=[1])"}
    while len(possible) < 300:
        n = rng.randint(1, 8)
        nums = [rng.randint(0, 5) for _ in range(n)]
        changes = [
            index for index, amount in enumerate(nums, 1) for _ in range(amount + 1)
        ]
        assert 1 <= n <= 2000 and len(changes) >= n
        assert all(0 <= value <= 10**9 for value in nums)
        possible.add(f"candidate(nums={nums!r},changeIndices={changes!r})")
    while len(impossible) < 300:
        n = rng.randint(2, 8)
        nums = [rng.randint(0, 5) for _ in range(n)]
        nums[-1] = 100
        changes = list(range(1, n + 1)) + [
            rng.randint(1, n) for _ in range(rng.randint(0, 20))
        ]
        assert 1 <= len(changes) <= 2000 and all(1 <= value <= n for value in changes)
        impossible.add(f"candidate(nums={nums!r},changeIndices={changes!r})")
    return sorted(possible | impossible)
