def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], tuple[tuple[int, int], ...]]] = set()
    while len(cases) < 600:
        size = rng.randint(1, 50)
        original = rng.sample(range(1, 1_000_001), size)
        current = original[:]
        operations = []
        for _ in range(rng.randint(1, 60)):
            old = rng.choice(current)
            new = rng.randint(1, 1_000_000)
            while new in current:
                new = rng.randint(1, 1_000_000)
            operations.append((old, new))
            current[current.index(old)] = new
        cases.add((tuple(original), tuple(operations)))

    cases.add(((1, 2), ((1, 3), (2, 1), (3, 2))))
    cases.add(((1, 2, 4, 6), ((1, 3), (4, 7), (6, 1))))
    large_nums = tuple(range(1, 100_001))
    large_operations = tuple((value, value + 100_000) for value in range(1, 100_001))
    cases.add((large_nums, large_operations))

    calls = []
    for nums, operations in sorted(cases):
        current_values = set(nums)
        assert 1 <= len(nums) <= 100_000 and len(set(nums)) == len(nums)
        assert all(1 <= value <= 1_000_000 for value in nums)
        assert 1 <= len(operations) <= 100_000
        for old, new in operations:
            assert 1 <= old <= 1_000_000 and 1 <= new <= 1_000_000
            assert old in current_values and new not in current_values
            current_values.remove(old)
            current_values.add(new)
        calls.append(
            f"candidate(nums={list(nums)!r}, operations={[list(op) for op in operations]!r})"
        )
    assert 500 <= len(calls) <= 999 and len(calls) == len(set(calls))
    return calls
