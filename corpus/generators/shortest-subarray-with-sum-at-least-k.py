import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def valid(d):
        a = d["nums"]
        assert (
            1 <= len(a) <= 100000
            and all(-100000 <= v <= 100000 for v in a)
            and 1 <= d["k"] <= 10**9
        )

    def add(**kwargs):
        valid(kwargs)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(nums=[1], k=1)
    add(nums=[1, 2], k=4)
    add(nums=[2, -1, 2], k=3)
    add(nums=[100000] * 100000, k=10**9)
    add(nums=[-100000, 100000] * 50000, k=100001)
    add(nums=[-100000] * 99999 + [100000], k=100000)
    t = 0
    while len(calls) < 600:
        n = rng.randint(1, 70)
        a = [rng.randint(-100, 100) for _ in range(n)]
        k = rng.randint(1, 500) if t % 3 else rng.randint(1, 10**9)
        if t % 4 == 0:
            a = [rng.randint(1, 100) for _ in range(n)]
            k = rng.randint(1, sum(a))
        add(nums=a, k=k)
        t += 1
    return calls
