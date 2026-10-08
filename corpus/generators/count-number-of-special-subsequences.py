import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def emit(**values):
        nums = values["nums"]
        assert 1 <= len(nums) <= 100000 and all(0 <= x <= 2 for x in nums)
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
        [1],
        [2],
        [0, 1, 2, 2],
        [0, 1, 2, 0, 1, 2],
        [0] * 33333 + [1] * 33333 + [2] * 33334,
        [2] * 100000,
    ):
        emit(nums=nums)
    while len(calls) < 600:
        n = rng.randint(1, 100)
        mode = len(calls) % 4
        if mode == 0:
            nums = (
                [0] * rng.randint(1, 30)
                + [1] * rng.randint(1, 30)
                + [2] * rng.randint(1, 30)
            )
        elif mode == 1:
            nums = (
                [2] * rng.randint(1, 30)
                + [1] * rng.randint(1, 30)
                + [0] * rng.randint(1, 30)
            )
        else:
            nums = [rng.randrange(3) for _ in range(n)]
        emit(nums=nums)
    return calls
