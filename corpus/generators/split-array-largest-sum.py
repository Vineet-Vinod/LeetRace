import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def emit(**values):
        nums, k = values["nums"], values["k"]
        assert (
            1 <= len(nums) <= 1000
            and all(0 <= x <= 1000000 for x in nums)
            and 1 <= k <= min(50, len(nums))
        )
        call = (
            "candidate("
            + ", ".join(name + "=" + repr(value) for name, value in values.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for nums, k in [
        ([0], 1),
        ([1000000] * 1000, 50),
        ([0] * 1000, 1),
        ([0, 1000000] * 500, 1),
        ([7, 2, 5, 10, 8], 2),
    ]:
        emit(nums=nums, k=k)
    while len(calls) < 600:
        n = rng.randint(1, 80)
        nums = [rng.randint(0, 1000) for _ in range(n)]
        emit(nums=nums, k=rng.randint(1, min(50, n)))
    return calls
