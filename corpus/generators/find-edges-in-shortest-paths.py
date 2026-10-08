import random


def literal(value):
    if isinstance(value, list):
        if len(value) > 30 and all(x == value[0] for x in value):
            return f"[{literal(value[0])}] * {len(value)}"
        if len(value) > 30 and all(isinstance(x, int) for x in value):
            step = value[1] - value[0]
            if step and all(x == value[0] + i * step for i, x in enumerate(value)):
                return f"list(range({value[0]}, {value[-1] + step}, {step}))"
        return "[" + ", ".join(literal(x) for x in value) + "]"
    return repr(value)


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = []
    seen = set()

    def add(*args):
        validate(*args)
        call = "candidate(" + ", ".join(literal(x) for x in args) + ")"
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(
        6,
        [
            [0, 1, 4],
            [0, 2, 1],
            [1, 3, 2],
            [1, 4, 3],
            [1, 5, 1],
            [2, 3, 1],
            [3, 5, 3],
            [4, 5, 2],
        ],
    )
    add(4, [[2, 0, 1], [0, 1, 1], [0, 3, 4], [3, 2, 2]])

    add(50000, [[i, i + 1, 100000] for i in range(49999)] + [[0, 49999, 100000]])
    add(50000, [[0, 1, 1]])
    add(2, [[1, 0, 1]])

    while len(calls) < 600:
        n = rng.randint(2, 14)
        pairs = [(a, b) for a in range(n) for b in range(a + 1, n)]
        rng.shuffle(pairs)
        mode = len(calls) % 4
        if mode == 0 and n > 2:
            pairs = [(a, b) for a, b in pairs if b != n - 1]
        edges = [
            [a, b, rng.choice([1, 1, 2, 5, 100000])]
            for a, b in pairs[: rng.randint(1, max(1, min(len(pairs), 30)))]
        ]
        add(n, edges)
    return calls


def validate(n, edges):
    assert 2 <= n <= 50000 and 1 <= len(edges) <= min(50000, n * (n - 1) // 2)
    assert all(
        0 <= a < n and 0 <= b < n and a != b and 1 <= w <= 100000 for a, b, w in edges
    )
    assert len({tuple(sorted((a, b))) for a, b, _ in edges}) == len(edges)
