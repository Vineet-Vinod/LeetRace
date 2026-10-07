import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        a = kwargs["nums"]
        assert 1 <= len(a) <= 1000 and all(0 <= x < 2**16 for x in a)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(nums=[2, 1, 3])
    add(nums=[0, 0, 0])
    add(nums=[65535] * 1000)
    add(nums=[0] * 1000)
    add(nums=[i % 64 for i in range(1000)])
    add(nums=[65535, 0])
    add(nums=rng.sample(range(65536), 1000))
    while len(calls) < 600:
        n = rng.randint(1, 35)
        if len(calls) % 3 == 0:
            a = [rng.randint(1, 32767) | 32768 for _ in range(n)]
        elif len(calls) % 3 == 1:
            a = [rng.randint(0, 63) for _ in range(n)]
        else:
            a = [rng.randint(0, 65535) for _ in range(n)]
        add(nums=a)
    return calls
