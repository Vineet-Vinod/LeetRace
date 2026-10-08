import random


def sample(r, turn):
    n = r.randint(2, 10)
    labels = r.sample(range(1, 501), n)
    if turn % 3 == 0:
        pairs = [[min(labels[0], v), max(labels[0], v)] for v in labels[1:]]
    elif turn % 3 == 1:
        parent = [-1] + [r.randrange(i) for i in range(1, n)]
        pairs = []
        for i in range(1, n):
            j = parent[i]
            while j != -1:
                pairs.append(sorted([labels[i], labels[j]]))
                j = parent[j]
    else:
        pairs = [
            sorted([labels[i], labels[j]])
            for i in range(n)
            for j in range(i + 1, n)
            if r.random() < 0.4
        ]
        if not pairs:
            pairs = [sorted(labels[:2])]
    r.shuffle(pairs)
    return dict(pairs=pairs)


def validate(pairs):
    assert 1 <= len(pairs) <= 100000 and all(
        len(p) == 2 and 1 <= p[0] < p[1] <= 500 for p in pairs
    )
    assert len({tuple(p) for p in pairs}) == len(pairs)


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

    add(pairs=[[1, 2], [2, 3]])
    add(pairs=[[1, 2], [2, 3], [1, 3]])
    add(pairs=[[1, 2], [2, 3], [2, 4], [1, 5]])
    add(pairs=[[1, i] for i in range(2, 501)])
    add(pairs=[[a, b] for a in range(1, 501) for b in range(a + 1, 501)][:100000])
    turn = 0
    while len(calls) < 600:
        kwargs = sample(r, turn)
        turn += 1
        add(**kwargs)
    assert len(calls) == len(set(calls)) == 600
    return calls
