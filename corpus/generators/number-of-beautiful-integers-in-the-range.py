import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(low: int, high: int, k: int) -> None:
        assert 1 <= low <= high <= 10**9 and 1 <= k <= 20
        call = (
            "candidate("
            + ", ".join(
                f"{key}={value!r}"
                for key, value in [("low", low), ("high", high), ("k", k)]
            )
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(low=10, high=20, k=3)
    add(low=1, high=10**9, k=20)
    add(low=1, high=10**9, k=1)
    add(low=10**9, high=10**9, k=1)
    add(low=10, high=20, k=3)
    add(low=1, high=10, k=1)
    add(low=5, high=5, k=2)
    while len(calls) < 600:
        low = rng.randint(1, 50000)
        high = low + rng.randint(0, 10000)
        if len(calls) % 4 == 0:
            low = rng.randint(1, 10**8)
            high = rng.randint(low, 10**9)
        add(low=low, high=high, k=rng.randint(1, 20))
    return calls
