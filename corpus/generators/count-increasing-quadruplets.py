import random

EXAMPLES = ["candidate(nums=[1, 3, 2, 4, 5])", "candidate(nums=[1, 2, 3, 4])"]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = list(EXAMPLES)
    seen = set(calls)

    def emit(call: str) -> None:
        if call not in seen:
            calls.append(call)
            seen.add(call)

    def add(nums):
        assert 4 <= len(nums) <= 4000 and sorted(nums) == list(range(1, len(nums) + 1))
        emit(f"candidate(nums={nums!r})")

    add(list(range(1, 4001)))
    add(list(range(4000, 0, -1)))
    add(
        list(range(1, 1001))
        + list(range(2001, 3001))
        + list(range(1001, 2001))
        + list(range(3001, 4001))
    )
    while len(calls) < 600:
        n = rng.randint(4, 35)
        nums = list(range(1, n + 1))
        rng.shuffle(nums)
        if rng.random() < 0.25:
            nums = [1, n - 1] + list(range(2, n - 1)) + [n]
        add(nums)
    return calls
