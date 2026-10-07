import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        t = kwargs["transactions"]
        assert 1 <= len(t) <= 8 and all(
            len(row) == 3
            and 0 <= row[0] < 12
            and 0 <= row[1] < 12
            and row[0] != row[1]
            and 1 <= row[2] <= 100
            for row in t
        )
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(transactions=[[i, i + 6, 100] for i in range(6)] + [[0, 7, 1], [1, 8, 99]])
    add(transactions=[[0, 1, 10], [2, 0, 5]])
    add(transactions=[[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]])
    while len(calls) < 600:
        mode = rng.randrange(3)
        transactions = []
        for _ in range(rng.randint(1, 8)):
            a, b = rng.sample(range(12), 2)
            amount = rng.randint(1, 100)
            transactions.append([a, b, amount])
        if mode == 0:
            a, b = rng.sample(range(12), 2)
            amount = rng.randint(1, 100)
            transactions = [[a, b, amount], [b, a, amount]]
        if mode == 1:
            a, b, c = rng.sample(range(12), 3)
            amount = rng.randint(1, 100)
            transactions = [[a, b, amount], [b, c, amount]]
        add(transactions=transactions)
    return calls
