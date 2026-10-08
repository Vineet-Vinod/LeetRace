import random


def sample(r, turn):
    n = r.randint(2, 65)
    vals = list(range(1, n + 1))
    r.shuffle(vals)
    # Packed level-order gives a valid connected binary tree with unique 1..n labels.
    if turn % 3 == 0:
        vals = [
            v for i in range(n) for v in ([vals[i], None] if i < n - 1 else [vals[i]])
        ]
    root_value = vals[0]
    q = r.choices(
        [v for v in vals if v is not None and v != root_value],
        k=r.randint(1, min(n, 30)),
    )
    return dict(root=vals, queries=q)


def validate(root, queries):
    values = [v for v in root if v is not None]
    n = len(values)
    assert 2 <= n <= 100000 and sorted(values) == list(range(1, n + 1))
    assert 1 <= len(queries) <= min(n, 10000) and all(
        q in values and q != root[0] for q in queries
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
            if key == "root":
                expression = "tree_node(" + expression + ")"
            parts.append(key + "=" + expression)
        call = "candidate(" + ", ".join(parts) + ")"
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(root=[1, 3, 4, 2, None, 6, 5, None, None, None, None, None, 7], queries=[4])
    add(root=[5, 8, 9, 2, 1, 3, 7, 4, 6], queries=[3, 2, 4, 8])
    add(root=list(range(1, 100001)), queries=list(range(2, 10002)))
    turn = 0
    while len(calls) < 600:
        kwargs = sample(r, turn)
        turn += 1
        add(**kwargs)
    assert len(calls) == len(set(calls)) == 600
    return calls
