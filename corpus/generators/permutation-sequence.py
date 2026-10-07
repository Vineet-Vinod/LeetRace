import random
from math import factorial


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(n: int, k: int) -> None:
        assert 1 <= n <= 9 and 1 <= k <= factorial(n)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in [("n", n), ("k", k)])
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for n in range(1, 10):
        add(n=n, k=1)
        add(n=n, k=factorial(n))
    add(n=3, k=3)
    add(n=4, k=9)
    add(n=3, k=1)
    while len(calls) < 600:
        n = rng.randint(1, 9)
        add(n=n, k=rng.randint(1, factorial(n)))
    return calls
