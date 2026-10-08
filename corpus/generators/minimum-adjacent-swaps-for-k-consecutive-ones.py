import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        a, k = kwargs["nums"], kwargs["k"]
        assert 1 <= len(a) <= 100000 and set(a) <= set([0, 1])
        assert 1 <= k <= sum(a)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(nums=[1, 0, 0, 1, 0, 1], k=2)
    add(nums=[1, 0, 0, 0, 0, 0, 1, 1], k=3)
    add(nums=[1, 1, 0, 1], k=2)
    add(nums=[1] * 100000, k=100000)
    add(nums=[1, 0] * 50000, k=50000)
    add(nums=[1], k=1)
    while len(calls) < 600:
        n = rng.randint(1, 150)
        a = rng.choices([0, 1], k=n)
        if not sum(a):
            a[rng.randrange(n)] = 1
        add(nums=a, k=rng.randint(1, sum(a)))
    return calls
