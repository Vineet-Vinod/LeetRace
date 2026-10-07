import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: list[str] = []
    seen: set[tuple[int, ...]] = set()

    def add(nums: list[int]) -> None:
        key = tuple(nums)
        if key not in seen:
            assert 1 <= len(nums) <= 100_000
            assert all(1 <= value <= 10**9 for value in nums)
            seen.add(key)
            cases.append(f"candidate(nums={nums!r})")

    add(list(range(1, 100_001)))
    add([1 + (index % 100) for index in range(100_000)])
    add([9] * 100_000)
    add([1])
    for length in range(2, 25):
        add(list(range(1, length + 1)))
        add([7] * length)
        for period in range(1, min(length, 6) + 1):
            add([1 + (index % period) for index in range(length)])
        for gap in range(1, length + 1):
            add([1 if index % gap == 0 else 2 for index in range(length)])
    while len(cases) < 600:
        length = rng.randint(1, 100)
        add([rng.randint(1, 20) for _ in range(length)])
    return cases
