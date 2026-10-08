import random


def generate(seed: int = 0) -> list[str]:
    """Generate unique binary arrays and goals satisfying 1 <= n <= 30000 and 0 <= goal <= n."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    i = 0
    while len(calls) < 600:
        n = 1 + i % 50
        nums = [rng.randrange(2) for _ in range(n)]
        goal = (i * 3) % (n + 1)
        assert all(bit in (0, 1) for bit in nums) and 0 <= goal <= n
        call = f"candidate(nums={nums!r}, goal={goal})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
