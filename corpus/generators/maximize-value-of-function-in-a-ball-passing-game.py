import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def valid(d):
        a = d["receiver"]
        assert (
            1 <= len(a) <= 100000
            and all(0 <= v < len(a) for v in a)
            and 1 <= d["k"] <= 10**10
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

    add(receiver=[2, 0, 1], k=4)
    add(receiver=[1, 1, 1, 2, 3], k=3)
    add(receiver=list(range(1, 100000)) + [0], k=10**10)
    add(receiver=[99999] * 100000, k=1)
    add(receiver=[0], k=10**10)
    t = 0
    while len(calls) < 600:
        n = rng.randint(1, 40)
        receiver = [rng.randrange(n) for _ in range(n)]
        if t % 3 == 0:
            receiver = [(i + 1) % n for i in range(n)]
        k = rng.choice([1, 2, 10**10, rng.randint(1, 1000)])
        add(receiver=receiver, k=k)
        t += 1
    return calls
