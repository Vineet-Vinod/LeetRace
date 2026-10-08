import random


def sample(r, turn):
    n = r.randint(1, 55)
    a = [r.randint(0, 100000) for _ in range(n)]
    if turn % 4 == 0:
        a.sort()
    if turn % 4 == 1:
        a.sort(reverse=True)
    return dict(prices=a)


def validate(prices):
    assert 1 <= len(prices) <= 100000 and all(0 <= v <= 100000 for v in prices)


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

    add(prices=[3, 3, 5, 0, 0, 3, 1, 4])
    add(prices=[1, 2, 3, 4, 5])
    add(prices=[7, 6, 4, 3, 1])
    add(prices=[0, 100000] * 50000)
    turn = 0
    while len(calls) < 600:
        kwargs = sample(r, turn)
        turn += 1
        add(**kwargs)
    assert len(calls) == len(set(calls)) == 600
    return calls
