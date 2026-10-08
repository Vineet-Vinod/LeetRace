import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def emit(**values):
        nums = values["nums"]
        assert 1 <= len(nums) <= 300 and all(0 <= x <= 100 for x in nums)
        call = (
            "candidate("
            + ", ".join(name + "=" + repr(value) for name, value in values.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for nums in (
        [0],
        [100],
        [3, 1, 5, 8],
        [1, 5],
        [100] * 300,
        [0] * 300,
        [0, 100] * 150,
    ):
        emit(nums=nums)
    while len(calls) < 600:
        n = rng.randint(1, 14)
        mode = len(calls) % 4
        nums = [
            rng.randint(0, 100) if mode == 0 else rng.randint(0, 5) for _ in range(n)
        ]
        emit(nums=nums)
    return calls
