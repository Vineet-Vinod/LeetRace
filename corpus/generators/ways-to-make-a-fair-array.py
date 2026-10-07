def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(nums=[2, 1, 6, 4])",
        "candidate(nums=[1, 1, 1])",
        "candidate(nums=[1, 2, 3])",
        f"candidate(nums={[1] * 99999!r})",
        f"candidate(nums={[1] * 100000!r})",
    }

    def fair_removals(nums: list[int]) -> int:
        count = 0
        for removed in range(len(nums)):
            even = sum(
                nums[i]
                for i in range(len(nums))
                if i != removed and (i if i < removed else i - 1) % 2 == 0
            )
            odd = sum(
                nums[i]
                for i in range(len(nums))
                if i != removed and (i if i < removed else i - 1) % 2 == 1
            )
            count += even == odd
        return count

    while len(cases) < 600:
        mode = rng.randrange(4)
        if mode == 0:
            n = 2 * rng.randint(1, 50) + 1
            nums = [1] * n
        elif mode == 1:
            n = rng.randint(1, 100)
            value = rng.randint(1, 10000)
            nums = [value] * n
        elif mode == 2:
            n = rng.randint(2, 100)
            nums = [rng.randint(1, 5) for _ in range(n)]
        else:
            n = rng.randint(1, 100)
            nums = [1 + (i % 2) for i in range(n)]
        assert 1 <= len(nums) <= 100000 and all(1 <= value <= 10000 for value in nums)
        assert 0 <= fair_removals(nums) <= len(nums)
        cases.add(f"candidate(nums={nums!r})")
    return sorted(cases)
