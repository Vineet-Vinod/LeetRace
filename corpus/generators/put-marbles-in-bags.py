import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(weights, k):
        assert 1 <= k <= len(weights) <= 100000 and all(
            1 <= v <= 1000000000 for v in weights
        )
        call = (
            "candidate("
            + ", ".join(
                f"{name}={value!r}"
                for name, value in (
                    ("weights", weights),
                    ("k", k),
                )
            )
            + ")"
        )
        calls[call] = None

    add(weights=[1, 3, 5, 1], k=2)
    add(weights=[1, 3], k=2)
    add(weights=[1, 1000000000] * 50000, k=50000)
    add(weights=list(range(1, 100001)), k=50000)
    add(weights=[1000000000], k=1)
    while len(calls) < 600:
        n = rng.randint(1, 70)
        mode = rng.randrange(4)
        weights = [rng.randint(1, 1000000000) for _ in range(n)]
        if mode == 0:
            weights = [rng.randint(1, 1000000000)] * n
        k = rng.choice((1, n)) if mode == 1 else rng.randint(1, n)
        add(weights=weights, k=k)
    return list(calls)
