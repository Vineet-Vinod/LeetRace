import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        a = kwargs["nums"]
        assert 1 <= len(a) <= 100000 and all(0 <= x < len(a) for x in a)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(nums=[2, 3, 1, 4, 0])
    add(nums=[1, 3, 0, 2, 4])
    add(nums=list(range(100000)))
    add(nums=[99999] * 100000)
    add(nums=[0])
    while len(calls) < 600:
        n = rng.randint(1, 100)
        a = [rng.randrange(n) for _ in range(n)]
        if len(calls) % 4 == 0:
            a = [rng.randrange(n)] * n
        add(nums=a)
    return calls
