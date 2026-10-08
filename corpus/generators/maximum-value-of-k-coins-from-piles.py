import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**data) -> None:
        a, k = data["piles"], data["k"]
        assert 1 <= len(a) <= 1000 and all(len(p) >= 1 for p in a)
        assert 1 <= k <= sum(map(len, a)) <= 2000 and all(
            1 <= x <= 100000 for p in a for x in p
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
        {"piles": [[1, 100, 3], [7, 8, 9]], "k": 2},
        {
            "piles": [
                [100],
                [100],
                [100],
                [100],
                [100],
                [100],
                [1, 1, 1, 1, 1, 1, 700],
            ],
            "k": 7,
        },
    ]:
        add(**example)
    add(piles=[[100000] * 2000], k=2000)
    add(piles=[[1, 100000] for _ in range(1000)], k=2000)
    add(piles=[[100000] for _ in range(1000)], k=1)
    while len(calls) < 600:
        piles = [
            [
                rng.randint(1, 100000 if len(calls) % 3 == 0 else 30)
                for _ in range(rng.randint(1, 8))
            ]
            for _ in range(rng.randint(1, 8))
        ]
        total = sum(map(len, piles))
        add(piles=piles, k=rng.choice([1, total, rng.randint(1, total)]))
    assert len(calls) == 600
    return calls
