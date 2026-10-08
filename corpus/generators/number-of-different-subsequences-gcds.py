import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**data) -> None:
        a = data["nums"]
        assert 1 <= len(a) <= 100000 and all(1 <= x <= 200000 for x in a)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in data.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for example in [{"nums": [6, 10, 3]}, {"nums": [5, 15, 40, 5, 6]}]:
        add(**example)
    add(nums=[200000] * 100000)
    add(nums=list(range(1, 100001)))
    add(nums=[199999, 200000])
    while len(calls) < 600:
        mode = len(calls) % 3
        a = [rng.randint(1, 200) for _ in range(rng.randint(1, 50))]
        if mode == 0:
            divisor = rng.randint(1, 100)
            a = [x * divisor for x in a]
        if mode == 1:
            a = [rng.choice([2, 3, 5, 7, 11, 13, 17, 19]) for _ in a]
        add(nums=a)
    assert len(calls) == 600
    return calls
