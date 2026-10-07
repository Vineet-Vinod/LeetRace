import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(n: int, cuts: list[int]) -> None:
        assert 2 <= n <= 1000000 and 1 <= len(cuts) <= min(n - 1, 100)
        assert len(set(cuts)) == len(cuts) and all(1 <= c < n for c in cuts)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in [("n", n), ("cuts", cuts)])
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(n=7, cuts=[1, 3, 4, 5])
    add(n=1000000, cuts=list(range(1, 101)))
    add(n=1000000, cuts=[999999])
    add(n=2, cuts=[1])
    add(n=7, cuts=[1, 3, 4, 5])
    add(n=9, cuts=[5, 6, 1, 4, 2])
    while len(calls) < 600:
        n = rng.randint(2, 1000000)
        cuts = rng.sample(range(1, n), rng.randint(1, min(n - 1, 20)))
        add(n=n, cuts=cuts)
    return calls
