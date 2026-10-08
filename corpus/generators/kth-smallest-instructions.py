import random
from math import comb


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(destination: list[int], k: int) -> None:
        assert len(destination) == 2 and all(1 <= x <= 15 for x in destination)
        assert 1 <= k <= comb(sum(destination), destination[0])
        call = (
            "candidate("
            + ", ".join(
                f"{key}={value!r}"
                for key, value in [("destination", destination), ("k", k)]
            )
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(destination=[2, 3], k=1)
    add(destination=[15, 15], k=1)
    add(destination=[15, 15], k=comb(30, 15))
    add(destination=[2, 3], k=1)
    add(destination=[2, 3], k=2)
    add(destination=[2, 3], k=3)
    while len(calls) < 600:
        a, b = rng.randint(1, 15), rng.randint(1, 15)
        n = comb(a + b, a)
        add(destination=[a, b], k=rng.choice([1, n, rng.randint(1, n)]))
    return calls
