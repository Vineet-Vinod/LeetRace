import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    boundary_nums = list(range(0, 1000, 2)) * 20 + list(range(1, 1000, 2)) * 20
    calls: set[str] = {f"candidate(nums={boundary_nums!r})"}
    while len(calls) < 600:
        size = 2 * rng.randint(1, 1000)
        evens = [2 * rng.randint(0, 500) for _ in range(size // 2)]
        odds = [2 * rng.randint(0, 499) + 1 for _ in range(size // 2)]
        nums = evens + odds
        rng.shuffle(nums)
        assert len(nums) % 2 == 0 and sum(value % 2 == 0 for value in nums) == size // 2
        calls.add(f"candidate(nums={nums!r})")
    return sorted(calls)
