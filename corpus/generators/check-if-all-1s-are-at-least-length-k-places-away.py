from __future__ import annotations
import random

EXAMPLE_CALLS = [
    "candidate(nums=[1, 0, 0, 0, 1, 0, 0, 1], k=2)",
    "candidate(nums=[1, 0, 0, 1, 0, 1], k=2)",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    valid = {
        EXAMPLE_CALLS[0],
        "candidate(nums=[1], k=0)",
        f"candidate(nums={[1] + [0] * 99999!r}, k=99999)",
        f"candidate(nums={[1, 0] + [0] * 99998!r}, k=0)",
    }
    invalid = {
        EXAMPLE_CALLS[1],
        "candidate(nums=[1, 1], k=1)",
        f"candidate(nums={[1, 1] + [0] * 99998!r}, k=1)",
    }
    while len(valid) < 300:
        length = rng.randint(1, 1000)
        k = rng.randint(0, length)
        nums = [0] * length
        position = rng.randint(0, length - 1)
        while position < length:
            nums[position] = 1
            position += k + 1 + rng.randint(0, 3)
        valid.add(f"candidate(nums={nums!r}, k={k})")
    while len(invalid) < 300:
        length = rng.randint(2, 1000)
        k = rng.randint(1, length)
        first = rng.randint(0, length - 2)
        second = rng.randint(first + 1, min(length - 1, first + k))
        nums = [0] * length
        nums[first] = nums[second] = 1
        invalid.add(f"candidate(nums={nums!r}, k={k})")
    assert len(valid) == 300 and len(invalid) == 300
    return sorted(valid | invalid)
