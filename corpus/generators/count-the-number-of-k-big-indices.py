import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def emit(**values):
        nums, k = values["nums"], values["k"]
        assert (
            1 <= len(nums) <= 100000
            and 1 <= k <= len(nums)
            and all(1 <= x <= len(nums) for x in nums)
        )
        call = (
            "candidate("
            + ", ".join(name + "=" + repr(value) for name, value in values.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    emit(nums=[1], k=1)
    emit(nums=[2, 3, 6, 5, 2, 3], k=2)
    emit(nums=[1] * 100000, k=100000)
    emit(nums=list(range(1, 50001)) + list(range(50000, 0, -1)), k=100)
    emit(nums=[1] * 49999 + [100000] + [1] * 50000, k=49999)
    while len(calls) < 600:
        n = rng.randint(2, 100)
        nums = [rng.randint(1, n) for _ in range(n)]
        k = rng.randint(1, max(1, n // 4)) if len(calls) % 3 else rng.randint(1, n)
        emit(nums=nums, k=k)
    return calls
