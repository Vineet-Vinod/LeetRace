def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    possible = {"candidate(nums=[1],m=200)", "candidate(nums=[100]*100,m=200)"}
    impossible = {"candidate(nums=[99]*100,m=199)"}
    while len(possible) < 300:
        n = rng.randint(2, 100)
        nums = [rng.randint(1, 100) for _ in range(n)]
        threshold = rng.randint(
            1, min(200, max(nums[i] + nums[i + 1] for i in range(n - 1)))
        )
        assert 1 <= n <= 100 and all(1 <= value <= 100 for value in nums)
        possible.add(f"candidate(nums={nums!r},m={threshold})")
    while len(impossible) < 300:
        n = rng.randint(3, 100)
        nums = [rng.randint(1, 98) for _ in range(n)]
        threshold = max(nums[i] + nums[i + 1] for i in range(n - 1)) + 1
        assert 3 <= n <= 100 and 1 <= threshold <= 200
        impossible.add(f"candidate(nums={nums!r},m={threshold})")
    return sorted(possible | impossible)
