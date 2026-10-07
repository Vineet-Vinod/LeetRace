import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        a = kwargs["nums"]
        assert 2 <= len(a) <= 100000 and all(1 <= x <= 100000 for x in a)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(nums=[2, 2, 1, 1, 5, 3, 3, 5])
    add(nums=[1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5])
    add(nums=[100000] * 100000)
    add(nums=list(range(1, 100001)))
    add(nums=[1, 2])
    while len(calls) < 600:
        n = rng.randint(2, 120)
        a = [rng.randint(1, rng.randint(1, 15)) for _ in range(n)]
        if len(calls) % 5 == 0:
            a = [rng.randint(1, 100000)] * n
        add(nums=a)
    return calls
