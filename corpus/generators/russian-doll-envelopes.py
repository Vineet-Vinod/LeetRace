import random


def sample(r, turn):
    n = r.randint(1, 60)
    a = [[r.randint(1, 30), r.randint(1, 30)] for _ in range(n)]
    if turn % 3 == 0:
        a = [[i + 1, i + 1] for i in range(n)]
    if turn % 3 == 1:
        a = [[1, r.randint(1, 100000)] for _ in range(n)]
    return dict(envelopes=a)


def validate(envelopes):
    assert 1 <= len(envelopes) <= 100000 and all(
        len(a) == 2 and all(1 <= v <= 100000 for v in a) for a in envelopes
    )


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

    add(envelopes=[[5, 4], [6, 4], [6, 7], [2, 3]])
    add(envelopes=[[1, 1], [1, 1], [1, 1]])
    add(envelopes=[[i, i] for i in range(1, 100001)])
    turn = 0
    while len(calls) < 600:
        kwargs = sample(r, turn)
        turn += 1
        add(**kwargs)
    assert len(calls) == len(set(calls)) == 600
    return calls
