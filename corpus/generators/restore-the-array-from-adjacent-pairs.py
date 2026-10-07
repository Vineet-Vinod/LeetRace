def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    maximum = list(range(100000))
    maximum_pairs = [[maximum[i], maximum[i + 1]] for i in range(len(maximum) - 1)]
    rng.shuffle(maximum_pairs)
    cases = {f"candidate(adjacentPairs={maximum_pairs!r})"}
    while len(cases) < 600:
        n = rng.randint(2, 100)
        nums = rng.sample(range(-100000, 100001), n)
        pairs = [[nums[i], nums[i + 1]] for i in range(n - 1)]
        rng.shuffle(pairs)
        for pair in pairs:
            if rng.random() < 0.5:
                pair.reverse()
        assert len(nums) == len(pairs) + 1 <= 100000
        assert len(set(nums)) == n
        assert all(-100000 <= value <= 100000 for value in nums)
        cases.add(f"candidate(adjacentPairs={pairs!r})")
    return sorted(cases)
