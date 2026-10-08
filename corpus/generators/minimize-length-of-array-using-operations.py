import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    arrays = {
        (1,),
        (1, 4, 3, 1),
        (5, 5, 5, 10, 5),
        (2, 3, 4),
        (1,) * 100000,
        (2,) * 50000 + (4,) * 50000,
        (2,) * 50000 + (3,) * 50000,
    }
    while len(arrays) < 300:
        base = rng.randint(1, 1000)
        minimum_count = rng.randint(1, 80)
        other_count = rng.randint(0, 80)
        values = [base] * minimum_count + [
            base * rng.randint(2, 10) for _ in range(other_count)
        ]
        rng.shuffle(values)
        arrays.add(tuple(values))
    while len(arrays) < 600:
        base = rng.randint(1, 1000)
        values = [base] * rng.randint(1, 80)
        values.append(base + rng.randint(1, 20))
        rng.shuffle(values)
        arrays.add(tuple(values))
    calls = [f"candidate(nums={list(nums)!r})" for nums in arrays]
    assert 500 <= len(calls) <= 999 and len(calls) == len(set(calls))
    assert all(
        1 <= len(nums) <= 100000 and all(1 <= value <= 10**9 for value in nums)
        for nums in arrays
    )
    return calls
