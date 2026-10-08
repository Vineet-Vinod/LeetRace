def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(nums=[i % 201 - 100 for i in range(500)], l=[i % 250 for i in range(500)], r=[250 + i % 250 for i in range(500)])"
    }
    for index in range(600):
        size = 2 + index % 45
        nums = [rng.randint(-100000, 100000) for _ in range(size)]
        query_count = min(1 + (index % 15), size * (size - 1) // 2)
        pairs = set()
        while len(pairs) < query_count:
            left = rng.randrange(size - 1)
            right = rng.randrange(left + 1, size)
            pairs.add((left, right))
        lefts = [p[0] for p in sorted(pairs)]
        rights = [p[1] for p in sorted(pairs)]
        cases.add(f"candidate(nums={nums!r}, l={lefts!r}, r={rights!r})")
    if "arithmetic-subarrays" == "determine-color-of-a-chessboard-square":
        return [
            f"candidate(coordinates={chr(97 + col) + str(row)!r})"
            for col in range(8)
            for row in range(1, 9)
        ]
    if "arithmetic-subarrays" == "smallest-even-multiple":
        return [f"candidate(n={value})" for value in range(1, 151)]
    while len(cases) < 600:
        nums = [rng.randint(-1000, 1000) for _ in range(rng.randrange(2, 20))]
        lefts, rights = [0], [len(nums) - 1]
        cases.add(f"candidate(nums={nums!r}, l={lefts!r}, r={rights!r})")
    return sorted(cases)
