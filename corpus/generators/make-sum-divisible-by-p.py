def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(nums=[3, 1, 4, 2], p=6)",
        "candidate(nums=[6, 3, 5, 2], p=9)",
        "candidate(nums=[1, 2, 3], p=3)",
        "candidate(nums=[1], p=2)",
        f"candidate(nums={[1] * 100000!r}, p=99999)",
    }
    while len(cases) < 600:
        mode = rng.randrange(4)
        if mode == 0:
            p = rng.randint(2, 100000)
            remainder = rng.randint(1, p - 1)
            nums = [p, remainder]
        elif mode == 1:
            p = rng.randint(3, 100000)
            pieces_count = rng.randint(2, min(8, p - 1))
            remainder = rng.randint(pieces_count, p - 1)
            cuts = sorted(rng.sample(range(1, remainder), pieces_count - 1))
            edges = [0, *cuts, remainder]
            pieces = [edges[i + 1] - edges[i] for i in range(pieces_count)]
            nums = pieces + [p]
        elif mode == 2:
            p = rng.randint(1, 100000)
            nums = [p * rng.randint(1, 3) for _ in range(rng.randint(1, 40))]
        else:
            p = rng.randint(2, 100)
            nums = [rng.randint(1, 1000) for _ in range(rng.randint(1, 40))]
        assert 1 <= len(nums) <= 100000 and all(1 <= value <= 10**9 for value in nums)
        assert 1 <= p <= 10**9
        cases.add(f"candidate(nums={nums!r}, p={p})")
    return sorted(cases)
