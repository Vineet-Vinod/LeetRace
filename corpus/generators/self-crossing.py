import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        a = kwargs["distance"]
        assert 1 <= len(a) <= 100000 and all(1 <= x <= 100000 for x in a)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(distance=[2, 1, 1, 2])
    add(distance=[1, 2, 3, 4])
    add(distance=[1, 1, 1, 2, 1])
    add(distance=list(range(1, 100001)))
    add(distance=[100000] * 100000)
    add(distance=[100000])
    while len(calls) < 600:
        n = rng.randint(1, 50)
        if len(calls) % 3 == 0:
            a = sorted(rng.sample(range(1, 100001), n))
        else:
            a = [rng.randint(1, 30) for _ in range(n)]
        add(distance=a)
    return calls
