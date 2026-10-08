import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(n: int) -> None:
        assert 0 <= n <= 10**9
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in [("n", n)])
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for n in (
        [0, 1, 2, 3, 6, 10**9]
        + [1 << i for i in range(30)]
        + [(1 << i) - 1 for i in range(1, 30)]
    ):
        add(n=n)
    add(n=3)
    add(n=6)
    while len(calls) < 600:
        add(n=rng.randint(0, 10**9))
    return calls
