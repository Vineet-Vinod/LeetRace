import random


def sample(r, turn):
    n = r.randint(1, 30)
    a = [r.randint(1, 100) for _ in range(n)]
    s = r.randint(1, 100)
    h = r.choice(
        [
            max(1, (sum(a) + s - 1) // s),
            r.randint(1, 100),
            max(1, (sum(a) + s - 1) // s + n),
        ]
    )
    if turn % 4 == 0:
        s = 1
        h = max(1, sum(a) - 1)
    return dict(dist=a, speed=s, hoursBefore=h)


def validate(dist, speed, hoursBefore):
    assert 1 <= len(dist) <= 1000 and all(1 <= v <= 100000 for v in dist)
    assert 1 <= speed <= 10**6 and 1 <= hoursBefore <= 10**7


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

    add(dist=[1, 3, 2], speed=4, hoursBefore=2)
    add(dist=[7, 3, 5, 5], speed=2, hoursBefore=10)
    add(dist=[7, 3, 5, 5], speed=1, hoursBefore=10)
    add(dist=[100000] * 1000, speed=10**6, hoursBefore=10**7)
    add(dist=[1] * 1000, speed=10**6, hoursBefore=1)
    turn = 0
    while len(calls) < 600:
        kwargs = sample(r, turn)
        turn += 1
        add(**kwargs)
    assert len(calls) == len(set(calls)) == 600
    return calls
