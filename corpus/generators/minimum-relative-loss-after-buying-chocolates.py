import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(prices, queries):
        assert 1 <= len(prices) <= 100000 and all(1 <= p <= 1000000000 for p in prices)
        assert 1 <= len(queries) <= 100000
        assert all(
            len(q) == 2 and 1 <= q[0] <= 1000000000 and 1 <= q[1] <= len(prices)
            for q in queries
        )
        call = (
            "candidate("
            + ", ".join(
                f"{name}={value!r}"
                for name, value in (
                    ("prices", prices),
                    ("queries", queries),
                )
            )
            + ")"
        )
        calls[call] = None

    add(prices=[1, 9, 22, 10, 19], queries=[[18, 4], [5, 2]])
    add(prices=[1, 5, 4, 3, 7, 11, 9], queries=[[5, 4], [5, 7], [7, 3], [4, 5]])
    add(prices=[5, 6, 7], queries=[[10, 1], [5, 3], [3, 3]])
    add(prices=list(range(1, 100001)), queries=[[1, i] for i in range(1, 100001)])
    add(prices=[1, 1000000000], queries=[[1000000000, 1], [1, 2], [500000000, 2]])
    while len(calls) < 600:
        n = rng.randint(1, 35)
        prices = [rng.randint(1, 100) for _ in range(n)]
        mode = rng.randrange(4)
        if mode == 0:
            queries = [
                [rng.randint(1, 10), rng.randint(1, n)]
                for _ in range(rng.randint(1, 15))
            ]
        elif mode == 1:
            queries = [
                [rng.randint(100, 1000), rng.randint(1, n)]
                for _ in range(rng.randint(1, 15))
            ]
        elif mode == 2:
            prices = [rng.randint(1, 100)] * n
            queries = [
                [rng.randint(1, 100), rng.randint(1, n)]
                for _ in range(rng.randint(1, 15))
            ]
        else:
            queries = [
                [rng.randint(1, 100), rng.randint(1, n)]
                for _ in range(rng.randint(1, 15))
            ]
        add(prices=prices, queries=queries)
    return list(calls)
