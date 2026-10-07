import random


def generate(seed: int = 0) -> list[str]:
    """Mix arbitrary arrays with arrays constructively produced by legal operations."""
    rng = random.Random(seed)
    cases: list[str] = []
    seen: set[str] = set()
    index = 0
    while len(cases) < 600:
        if index == 0:
            n = 100_000
            k = n
            nums = [1_000_000] * n
        elif index % 3 == 0:
            n = 1 + index % 50
            k = 1 + (index * 11) % n
            operations = [rng.randint(0, 5) for _ in range(n - k + 1)]
            nums = [
                sum(
                    operations[start]
                    for start in range(
                        max(0, position - k + 1), min(position, n - k) + 1
                    )
                )
                for position in range(n)
            ]
        else:
            n = 1 + index % 45
            k = 1 + (index * 11) % n
            nums = [rng.randint(0, 1_000_000) for _ in range(n)]
        assert 1 <= k <= n <= 100_000
        assert all(0 <= value <= 1_000_000 for value in nums)
        call = f"candidate(nums={nums!r}, k={k})"
        index += 1
        if call not in seen:
            seen.add(call)
            cases.append(call)
    return cases
