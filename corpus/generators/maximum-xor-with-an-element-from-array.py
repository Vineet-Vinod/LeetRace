import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def valid(d):
        a = d["nums"]
        q = d["queries"]
        assert (
            1 <= len(a) <= 100000
            and 1 <= len(q) <= 100000
            and all(0 <= v <= 10**9 for v in a)
        )
        assert all(len(p) == 2 and all(0 <= v <= 10**9 for v in p) for p in q)

    def add(**kwargs):
        valid(kwargs)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(nums=[0, 1, 2, 3, 4], queries=[[3, 1], [1, 3], [5, 6]])
    add(nums=[5, 2, 4, 6, 6, 3], queries=[[12, 4], [8, 1], [6, 3]])
    add(nums=list(range(100000)), queries=[[10**9, 10**9], [0, 0], [10**9, 0]])
    add(nums=[10**9], queries=[[i, i] for i in range(100000)])
    t = 0
    while len(calls) < 600:
        nums = [rng.randint(0, 1000) for _ in range(rng.randint(1, 40))]
        queries = [
            [rng.randint(0, 10**9), rng.choice([0, 10**9, rng.randint(0, 1000)])]
            for _ in range(rng.randint(1, 25))
        ]
        add(nums=nums, queries=queries)
        t += 1
    return calls
