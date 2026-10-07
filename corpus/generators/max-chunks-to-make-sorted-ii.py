import random


def sample(r, turn):
    n = r.randint(1, 65)
    a = [r.randint(0, 20) for _ in range(n)]
    if turn % 4 == 0:
        a.sort()
    if turn % 4 == 1:
        a.sort(reverse=True)
    return dict(arr=a)


def validate(arr):
    assert 1 <= len(arr) <= 2000 and all(0 <= v <= 10**8 for v in arr)


def generate(seed: int = 0) -> list[str]:
    r = random.Random(seed)
    calls = []
    seen = set()

    def add(**kwargs):
        validate(**kwargs)
        parts = []
        for key, value in kwargs.items():
            expression = repr(value)
            parts.append(key + "=" + expression)
        call = "candidate(" + ", ".join(parts) + ")"
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(arr=[5, 4, 3, 2, 1])
    add(arr=[2, 1, 3, 4, 4])
    add(arr=[10**8, 0] * 1000)
    add(arr=list(range(2000)))
    turn = 0
    while len(calls) < 600:
        kwargs = sample(r, turn)
        turn += 1
        add(**kwargs)
    assert len(calls) == len(set(calls)) == 600
    return calls
