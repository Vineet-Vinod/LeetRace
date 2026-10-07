import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**data) -> None:
        a, b = data["target"], data["arr"]
        assert (
            1 <= len(a) <= 100000
            and 1 <= len(b) <= 100000
            and len(set(a)) == len(a)
            and all(1 <= x <= 1000000000 for x in a + b)
        )
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in data.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for example in [
        {"target": [5, 1, 3], "arr": [9, 4, 2, 3, 4]},
        {"target": [6, 4, 8, 1, 3, 2], "arr": [4, 7, 6, 2, 3, 8, 6, 1]},
    ]:
        add(**example)
    add(target=list(range(1, 100001)), arr=list(range(100000, 0, -1)))
    add(target=list(range(1, 100001)), arr=list(range(1, 100001)))
    add(target=[1000000000], arr=[1] * 100000)
    while len(calls) < 600:
        target = rng.sample(range(1, 200), rng.randint(1, 60))
        mode = len(calls) % 4
        arr = [rng.randint(1, 250) for _ in range(rng.randint(1, 80))]
        if mode == 0:
            arr = target.copy()
        if mode == 1:
            arr = target[::-1]
        if mode == 2:
            arr = [rng.choice(target) for _ in range(rng.randint(1, 80))]
        add(target=target, arr=arr)
    assert len(calls) == 600
    return calls
