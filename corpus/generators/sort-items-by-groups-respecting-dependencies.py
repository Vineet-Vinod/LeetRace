import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        def render(value):
            # Repeat only immutable scalar values; nested input lists retain distinct identities.
            if isinstance(value, list):
                if (
                    len(value) >= 1000
                    and isinstance(value[0], (int, str))
                    and all(x == value[0] for x in value)
                ):
                    return f"[{value[0]!r}] * {len(value)}"
                return "[" + ", ".join(render(x) for x in value) + "]"
            return repr(value)

        call = (
            "candidate("
            + ", ".join(f"{key}={render(value)}" for key, value in kwargs.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    def case(n, m, g, b):
        assert 1 <= m <= n <= 30000 and len(g) == len(b) == n
        assert all(-1 <= x < m for x in g)
        for i, prior in enumerate(b):
            assert len(prior) <= n - 1 and len(prior) == len(set(prior))
            assert all(0 <= j < n and j != i for j in prior)
        add(n=n, m=m, group=g, beforeItems=b)

    case(8, 2, [-1, -1, 1, 0, 0, 1, 0, -1], [[], [6], [5], [6], [3, 6], [], [], []])
    case(8, 2, [-1, -1, 1, 0, 0, 1, 0, -1], [[], [6], [5], [6], [3], [], [4], []])
    case(30000, 30000, [-1] * 30000, [[] for _ in range(30000)])
    case(30000, 1, [0] * 30000, [[]] + [[i - 1] for i in range(1, 30000)])
    case(50, 1, [0] * 50, [[] for _ in range(49)] + [list(range(49))])
    while len(calls) < 600:
        n = rng.randint(2, 25)
        m = rng.randint(1, n)
        g = [rng.randint(-1, m - 1) for _ in range(n)]
        # Order whole groups first, then sample only forward dependencies for positive cases.
        labels = [x if x != -1 else m + i for i, x in enumerate(g)]
        keys = rng.sample(sorted(set(labels)), len(set(labels)))
        order = []
        for key in keys:
            items = [i for i in range(n) if labels[i] == key]
            rng.shuffle(items)
            order.extend(items)
        b = [[] for _ in range(n)]
        for i in range(1, n):
            b[order[i]] = rng.sample(order[:i], rng.randint(0, min(i, 4)))
        if len(calls) % 3 == 0:
            b[order[0]].append(order[-1])
            b[order[-1]] = sorted(set(b[order[-1]] + [order[0]]))
        case(n, m, g, b)
    assert len(calls) == 600
    return calls
