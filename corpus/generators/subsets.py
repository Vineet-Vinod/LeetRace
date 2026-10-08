# Inputs are unique-element arrays with the full stated value range.
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    values = {
        (1, 2, 3),
        (0,),
        tuple(range(-10, 0)),
        tuple(range(1, 11)),
    }
    while len(values) < 600:
        size = rng.randint(1, 10)
        values.add(tuple(rng.sample(range(-10, 11), size)))
    calls = []
    for nums in sorted(values):
        assert 1 <= len(nums) <= 10
        assert len(nums) == len(set(nums))
        assert all(-10 <= value <= 10 for value in nums)
        calls.append(f"candidate(nums={list(nums)!r})")
    return calls
