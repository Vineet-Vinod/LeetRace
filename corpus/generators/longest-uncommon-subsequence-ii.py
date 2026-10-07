def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(
        [
            'candidate(strs=["aba", "cdc", "eae"])',
            'candidate(strs=["aaa", "aaa", "aa"])',
            'candidate(strs=["a" * (1 + i % 10) for i in range(50)])',
        ]
    )
    for index in range(600):
        size = 2 + index % 20
        strs = [
            "".join(rng.choice("abcde") for _ in range(rng.randint(1, 10)))
            for _ in range(size)
        ]
        if index % 5 == 0 and size >= 2:
            strs[1] = strs[0]
        cases.add(f"candidate(strs={strs!r})")
    while len(cases) < 600:
        strs = [
            "".join(rng.choice("abcde") for _ in range(rng.randint(1, 10)))
            for _ in range(rng.randint(2, 20))
        ]
        cases.add(f"candidate(strs={strs!r})")
    return sorted(cases)
