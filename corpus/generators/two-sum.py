import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    boundary_nums = list(range(9998)) + [10000, 10001]
    calls: set[str] = {f"candidate(nums={boundary_nums!r}, target=20001)"}
    while len(calls) < 600:
        first = rng.randint(-500000000, 500000000)
        second = rng.randint(-500000000, 500000000)
        if first == second:
            continue
        nums = [first, second] + [
            rng.randint(-500000000, 500000000) for _ in range(rng.randint(0, 98))
        ]
        target = first + second
        solutions = [
            (i, j)
            for i in range(len(nums))
            for j in range(i + 1, len(nums))
            if nums[i] + nums[j] == target
        ]
        if len(solutions) != 1:
            continue
        calls.add(f"candidate(nums={nums!r}, target={target})")
    return sorted(calls)
