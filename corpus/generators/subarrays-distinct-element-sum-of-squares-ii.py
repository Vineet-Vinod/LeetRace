import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def emit(**values):
        nums = values["nums"]
        assert 1 <= len(nums) <= 100000 and all(1 <= x <= 100000 for x in nums)
        call = (
            "candidate("
            + ", ".join(name + "=" + repr(value) for name, value in values.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for nums in [
        [1],
        [100000],
        [1, 2, 1],
        [2, 2],
        [1] * 100000,
        list(range(1, 100001)),
        [1, 100000] * 50000,
    ]:
        emit(nums=nums)
    while len(calls) < 600:
        n = rng.randint(1, 100)
        mode = len(calls) % 3
        nums = [rng.randint(1, 5 if mode == 0 else 100000) for _ in range(n)]
        if mode == 2:
            nums = list(range(1, n + 1))
            rng.shuffle(nums)
        emit(nums=nums)
    return calls
