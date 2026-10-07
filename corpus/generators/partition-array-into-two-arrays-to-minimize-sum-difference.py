import random

EXAMPLES = [
    "candidate(nums=[3, 9, 7, 3])",
    "candidate(nums=[-36, 36])",
    "candidate(nums=[2, -1, 0, 4, -2, -9])",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = list(EXAMPLES)
    seen = set(calls)

    def emit(call: str) -> None:
        if call not in seen:
            calls.append(call)
            seen.add(call)

    def add(nums):
        assert (
            len(nums) % 2 == 0
            and 2 <= len(nums) <= 30
            and all(-(10**7) <= v <= 10**7 for v in nums)
        )
        emit(f"candidate(nums={nums!r})")

    add([-(10**7)] * 15 + [10**7] * 15)
    add([0] * 30)
    add([-(10**7), 10**7])
    while len(calls) < 600:
        n = rng.randint(1, 8)
        nums = [rng.randint(-10000, 10000) for _ in range(2 * n)]
        if rng.random() < 0.3:
            half = [rng.randint(-10000, 10000) for _ in range(n)]
            nums = half + half
            rng.shuffle(nums)
        add(nums)
    return calls
