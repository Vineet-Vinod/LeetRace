import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        a = kwargs["arr"]
        assert 1 <= len(a) <= 50000 and all(-(10**8) <= x <= 10**8 for x in a)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(arr=[100, -23, -23, 404, 100, 23, 23, 23, 3, 404])
    add(arr=[7])
    add(arr=[7, 6, 9, 6, 9, 6, 9, 7])
    add(arr=list(range(50000)))
    add(arr=[10**8] * 50000)
    add(arr=[-(10**8), 10**8])
    while len(calls) < 600:
        n = rng.randint(1, 100)
        a = [rng.randint(-12, 12) for _ in range(n)]
        if len(calls) % 4 == 0:
            a = [rng.randint(-(10**8), 10**8)] * n
        add(arr=a)
    return calls
