import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {
        (5, 4, 1, 2, 2),
        (1, 3, 2, 4),
        (2, 2, 4),
        (2, 4, 2),
        (2, 4, 16, 4, 2),
        (2, 2),
        (1,) * 99_999,
        (10**9, 1),
    }
    cases.add(tuple(value for value in (2, 4, 16, 256) for _ in range(2)) + (65_536,))
    while len(cases) < 600:
        size = rng.randint(2, 100)
        if rng.random() < 0.6:
            value = rng.randint(1, 1000)
            if value == 1:
                count = rng.choice((1, 3, 5, 7, 9, size))
                nums = (1,) * min(size, count)
            else:
                chain = [value]
                while chain[-1] * chain[-1] <= 10**9 and rng.random() < 0.7:
                    chain.append(chain[-1] * chain[-1])
                nums = tuple(element for element in chain[:-1] for _ in range(2)) + (
                    chain[-1],
                )
            if len(nums) > size:
                nums = nums[:size]
            if len(nums) < 2:
                nums += (rng.randint(1, 10**9),)
        else:
            nums = tuple(rng.randint(1, 10**9) for _ in range(size))
        cases.add(nums)
    assert all(
        2 <= len(nums) <= 100_000 and all(1 <= value <= 10**9 for value in nums)
        for nums in cases
    )
    return [f"candidate(nums={list(nums)!r})" for nums in sorted(cases)]
