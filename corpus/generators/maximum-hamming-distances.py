import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def emit(**values):
        nums, m = values["nums"], values["m"]
        assert (
            1 <= m <= 17 and 2 <= len(nums) <= 2**m and all(0 <= x < 2**m for x in nums)
        )
        call = (
            "candidate("
            + ", ".join(name + "=" + repr(value) for name, value in values.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    emit(nums=[0, 0], m=1)
    emit(nums=[0, 1], m=1)
    emit(nums=list(range(2**17)), m=17)
    emit(nums=[0] * (2**17), m=17)
    emit(nums=[0, 2**17 - 1], m=17)
    while len(calls) < 600:
        m = rng.randint(1, 17)
        n = rng.randint(2, min(40, 2**m))
        nums = [rng.randrange(2**m) for _ in range(n)]
        if len(calls) % 4 == 0:
            nums[-1] = nums[0] ^ (2**m - 1)
        emit(nums=nums, m=m)
    return calls
