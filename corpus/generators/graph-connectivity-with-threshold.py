import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        validate(kwargs)
        call = (
            "candidate(" + ", ".join(k + "=" + repr(v) for k, v in kwargs.items()) + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    def letters(text):
        return all("a" <= ch <= "z" for ch in text)

    def array(values, minimum, maximum, length):
        assert 1 <= len(values) <= length
        assert all(minimum <= v <= maximum for v in values)

    def validate(d):
        assert 2 <= d["n"] <= 10000 and 0 <= d["threshold"] <= d["n"]
        assert 1 <= len(d["queries"]) <= 100000
        assert all(
            len(q) == 2 and 1 <= q[0] <= d["n"] and 1 <= q[1] <= d["n"] and q[0] != q[1]
            for q in d["queries"]
        )

    add(n=10000, threshold=0, queries=[[1, 10000]] * 100000)
    add(n=10000, threshold=10000, queries=[[1, 10000]])
    add(n=6, threshold=2, queries=[[1, 4], [2, 5], [3, 6]])
    while len(calls) < 600:
        n = rng.randint(2, 120)
        t = rng.choice([0, n, rng.randint(0, n)])
        queries = [rng.sample(range(1, n + 1), 2) for _ in range(rng.randint(1, 60))]
        add(n=n, threshold=t, queries=queries)
    assert len(calls) == 600
    return calls
