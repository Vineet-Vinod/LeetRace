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

    add(3, [[1, 3], [2, 3]], [3, 2, 5])
    add(5, [[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]], [1, 2, 3, 4, 5])

    add(50000, [[i, i + 1] for i in range(1, 50000)] + [[1, 50000]], [10000] * 50000)
    add(50000, [], [1] * 50000)
    add(1, [], [1])

    while len(calls) < 600:
        n = rng.randint(1, 30)
        order = list(range(1, n + 1))
        rng.shuffle(order)
        edges = [
            [order[a], order[b]]
            for a in range(n)
            for b in range(a + 1, n)
            if rng.random() < rng.choice([0.05, 0.3])
        ]
        t = [rng.randint(1, 10000) for _ in range(n)]
        add(n, edges, t)
    return calls


def validate(n, edges, t):
    assert 1 <= n <= 50000 and 0 <= len(edges) <= min(n * (n - 1) // 2, 50000)
    assert len(t) == n and all(1 <= x <= 10000 for x in t)
    assert all(a != b and 1 <= a <= n and 1 <= b <= n for a, b in edges)
    assert len({tuple(e) for e in edges}) == len(edges)
    graph = [[] for _ in range(n)]
    degrees = [0] * n
    for a, b in edges:
        graph[a - 1].append(b - 1)
        degrees[b - 1] += 1
    queue = [i for i in range(n) if degrees[i] == 0]
    count = 0
    while queue:
        a = queue.pop()
        count += 1
        for b in graph[a]:
            degrees[b] -= 1
            if degrees[b] == 0:
                queue.append(b)
    assert count == n
