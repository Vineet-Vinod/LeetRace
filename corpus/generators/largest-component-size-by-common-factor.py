import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def valid(d):
        a = d["nums"]
        assert (
            1 <= len(a) <= 20000
            and len(set(a)) == len(a)
            and all(1 <= v <= 100000 for v in a)
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

    add(nums=[4, 6, 15, 35])
    add(nums=[20, 50, 9, 63])
    add(nums=[2, 3, 6, 7, 4, 12, 21, 39])
    add(nums=list(range(80001, 100001)))
    add(nums=[1])
    add(nums=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])
    t = 0
    while len(calls) < 600:
        n = rng.randint(1, 40)
        nums = (
            rng.sample(range(1, 500), n) if t % 3 else rng.sample(range(2, 1000, 2), n)
        )
        add(nums=nums)
        t += 1
    return calls
