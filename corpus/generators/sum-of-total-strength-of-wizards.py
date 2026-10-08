import random


def sample(r, turn):
    n = r.randint(1, 55)
    a = [r.choice([1, 10**9, r.randint(1, 100)]) for _ in range(n)]
    if turn % 4 == 0:
        a.sort()
    if turn % 4 == 1:
        a.sort(reverse=True)
    return dict(strength=a)


def validate(strength):
    assert 1 <= len(strength) <= 100000 and all(1 <= v <= 10**9 for v in strength)


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

    add(strength=[1, 3, 1, 2])
    add(strength=[5, 4, 6])
    add(strength=[10**9] * 100000)
    turn = 0
    while len(calls) < 600:
        kwargs = sample(r, turn)
        turn += 1
        add(**kwargs)
    assert len(calls) == len(set(calls)) == 600
    return calls
