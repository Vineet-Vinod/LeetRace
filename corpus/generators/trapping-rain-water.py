import random


def sample(r, turn):
    n = r.randint(1, 65)
    a = [r.randint(0, 100000) for _ in range(n)]
    if turn % 4 == 0:
        a.sort()
    if turn % 4 == 1:
        a.sort(reverse=True)
    return dict(height=a)


def validate(height):
    assert 1 <= len(height) <= 20000 and all(0 <= v <= 100000 for v in height)


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

    add(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    add(height=[4, 2, 0, 3, 2, 5])
    add(height=[100000] + [0] * 19998 + [100000])
    turn = 0
    while len(calls) < 600:
        kwargs = sample(r, turn)
        turn += 1
        add(**kwargs)
    assert len(calls) == len(set(calls)) == 600
    return calls
