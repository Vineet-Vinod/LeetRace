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

    add(5, [[4, 1, -1], [2, 0, -1], [0, 3, -1], [4, 3, -1]], 0, 1, 5)
    add(3, [[0, 1, -1], [0, 2, 5]], 0, 2, 6)
    add(4, [[1, 0, 4], [1, 2, 3], [2, 3, 5], [0, 3, -1]], 0, 2, 6)

    add(
        100,
        [[a, b, 10**7] for a in range(100) for b in range(a + 1, 100)],
        0,
        99,
        10**7,
    )
    add(100, [[i, i + 1, -1] for i in range(99)], 0, 99, 10**9)
    add(2, [[0, 1, -1]], 0, 1, 1)

    while len(calls) < 600:
        n = rng.randint(2, 10)
        # A spanning tree guarantees connectedness; additional edges are unique.
        pairs = {(i, rng.randrange(i)) for i in range(1, n)}
        pairs = {tuple(sorted(e)) for e in pairs}
        extras = [
            (a, b) for a in range(n) for b in range(a + 1, n) if (a, b) not in pairs
        ]
        rng.shuffle(extras)
        pairs.update(extras[: rng.randint(0, min(len(extras), 8))])
        pairs = sorted(pairs)
        rng.shuffle(pairs)
        edges = [
            [a, b, -1 if rng.random() < 0.55 else rng.randint(1, 20)] for a, b in pairs
        ]
        source, destination = rng.sample(range(n), 2)
        mode = len(calls) % 4
        if mode == 0:
            edges = [[a, b, -1] for a, b, _ in edges]
            target = rng.randint(n, 60)
        elif mode == 1:
            edges = [[a, b, rng.randint(2, 20)] for a, b, _ in edges]
            target = 1
        else:
            target = rng.randint(1, 70)
        add(n, edges, source, destination, target)
    return calls


def validate(n, edges, source, destination, target):
    assert 2 <= n <= 100 and 1 <= len(edges) <= n * (n - 1) // 2
    assert (
        0 <= source < n
        and 0 <= destination < n
        and source != destination
        and 1 <= target <= 10**9
    )
    assert all(
        a != b and 0 <= a < n and 0 <= b < n and (w == -1 or 1 <= w <= 10**7)
        for a, b, w in edges
    )
    assert len({tuple(sorted((a, b))) for a, b, _ in edges}) == len(edges)
    graph = [[] for _ in range(n)]
    for a, b, _ in edges:
        graph[a].append(b)
        graph[b].append(a)
    seen = {0}
    stack = [0]
    while stack:
        for b in graph[stack.pop()]:
            if b not in seen:
                seen.add(b)
                stack.append(b)
    assert len(seen) == n
