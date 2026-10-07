import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        nums, q = kwargs["nums"], kwargs["queries"]
        n = len(nums)
        assert (
            3 <= n <= 100000
            and all(1 <= v <= 100000 for v in nums)
            and 1 <= len(q) <= 100000
        )
        assert all(
            len(row) == 3
            and (
                row[0] == 1
                and 0 <= row[1] <= row[2] < n
                or row[0] == 2
                and 0 <= row[1] < n
                and 1 <= row[2] <= 100000
            )
            for row in q
        )
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(nums=[1, 100000] * 50000, queries=[[1, 0, 99999], [2, 1, 1]] * 50000)
    add(nums=[3, 1, 4, 2, 5], queries=[[2, 3, 4], [1, 0, 4]])
    add(nums=[4, 1, 4, 2, 1, 5], queries=[[2, 2, 4], [1, 0, 2], [1, 0, 4]])
    while len(calls) < 600:
        n = rng.randint(3, 45)
        nums = [rng.randint(1, 100000) for _ in range(n)]
        if len(calls) % 3 == 0:
            nums = [1 if i % 2 == 0 else 100000 for i in range(n)]
        queries = []
        for _ in range(rng.randint(1, 35)):
            if rng.randrange(2):
                a = rng.randrange(n)
                queries.append([1, a, rng.randint(a, n - 1)])
            else:
                queries.append([2, rng.randrange(n), rng.randint(1, 100000)])
        add(nums=nums, queries=queries)
    return calls
