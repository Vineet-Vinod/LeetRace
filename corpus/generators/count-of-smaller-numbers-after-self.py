import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**data) -> None:
        a = data["nums"]
        assert 1 <= len(a) <= 100000 and all(-10000 <= x <= 10000 for x in a)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in data.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for example in [{"nums": [5, 2, 6, 1]}, {"nums": [-1]}, {"nums": [-1, -1]}]:
        add(**example)
    add(nums=[10000] * 100000)
    add(nums=[10000 - i % 20001 for i in range(100000)])
    add(nums=[-10000 + i % 20001 for i in range(100000)])
    while len(calls) < 600:
        a = [rng.randint(-10000, 10000) for _ in range(rng.randint(1, 70))]
        mode = len(calls) % 4
        if mode == 0:
            a.sort()
        if mode == 1:
            a.sort(reverse=True)
        if mode == 2:
            a = [rng.choice([-2, -1, 0, 1, 2]) for _ in a]
        add(nums=a)
    assert len(calls) == 600
    return calls
