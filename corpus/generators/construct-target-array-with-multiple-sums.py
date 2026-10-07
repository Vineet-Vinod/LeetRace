import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def valid(d):
        a = d["target"]
        assert 1 <= len(a) <= 50000 and all(1 <= v <= 10**9 for v in a)

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

    add(target=[9, 3, 5])
    add(target=[1, 1, 1, 2])
    add(target=[8, 5])
    add(target=[1] * 50000)
    add(target=[1] * 49999 + [10**9])
    add(target=[1, 10**9])
    add(target=[10**9])
    t = 0
    while len(calls) < 600:
        n = rng.randint(1, 15)
        if t % 2:
            target = [1] * n
            for _ in range(rng.randint(0, 12)):
                index = rng.randrange(n)
                total = sum(target)
                if total <= 10**9:
                    target[index] = total
        else:
            target = [rng.randint(1, 1000) for _ in range(n)]
        add(target=target)
        t += 1
    return calls
