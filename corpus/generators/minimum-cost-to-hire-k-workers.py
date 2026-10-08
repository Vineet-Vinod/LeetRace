import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**data) -> None:
        a, b, k = data["quality"], data["wage"], data["k"]
        assert (
            1 <= k <= len(a) <= 10000
            and len(a) == len(b)
            and all(1 <= x <= 10000 for x in a + b)
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
        {"quality": [10, 20, 5], "wage": [70, 50, 30], "k": 2},
        {"quality": [3, 1, 10, 10, 1], "wage": [4, 8, 2, 2, 7], "k": 3},
    ]:
        add(**example)
    add(quality=[10000] * 10000, wage=[10000] * 10000, k=10000)
    add(quality=[1] * 10000, wage=[10000] * 10000, k=1)
    add(quality=[10000, 1], wage=[1, 10000], k=2)
    while len(calls) < 600:
        n = rng.randint(1, 60)
        quality = [rng.randint(1, 10000) for _ in range(n)]
        wage = [rng.randint(1, 10000) for _ in range(n)]
        if len(calls) % 3 == 0:
            quality = [rng.randint(1, 100) for _ in range(n)]
            ratio = rng.randint(1, 100)
            wage = [q * ratio for q in quality]
        add(quality=quality, wage=wage, k=rng.choice([1, n, rng.randint(1, n)]))
    assert len(calls) == 600
    return calls
