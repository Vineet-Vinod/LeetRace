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
        array(d["arr"], 1, len(d["arr"]), 100000)
        assert 1 <= d["k"] <= len(d["arr"])

    add(arr=list(range(100000, 0, -1)), k=1)
    add(arr=[100000] * 100000, k=100000)
    add(arr=[5, 4, 3, 2, 1], k=1)
    add(arr=[4, 1, 5, 2, 6, 2], k=2)
    while len(calls) < 600:
        n = rng.randint(1, 100)
        arr = [rng.randint(1, n) for _ in range(n)]
        if rng.randrange(4) == 0:
            arr.sort()
        add(arr=arr, k=rng.choice([1, n, rng.randint(1, n)]))
    assert len(calls) == 600
    return calls
