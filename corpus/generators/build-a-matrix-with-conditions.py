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

    def case(k, rows, cols):
        assert 2 <= k <= 400
        for edges in (rows, cols):
            assert 1 <= len(edges) <= 10000
            assert all(1 <= a <= k and 1 <= b <= k and a != b for a, b in edges)
        add(k=k, rowConditions=rows, colConditions=cols)

    case(3, [[1, 2], [3, 2]], [[2, 1], [3, 2]])
    case(2, [[1, 2], [2, 1]], [[1, 2]])
    case(400, [[i, i + 1] for i in range(1, 400)], [[400, 1]] * 10000)
    case(400, [[1, 2]] * 10000, [[1, 2]] * 10000)
    while len(calls) < 600:
        k = rng.randint(2, 20)
        orders = [rng.sample(range(1, k + 1), k) for _ in range(2)]
        edges = []
        for order in orders:
            e = []
            for _ in range(rng.randint(1, 30)):
                i, j = sorted(rng.sample(range(k), 2))
                e.append([order[i], order[j]])
            if len(calls) % 3 == 0:
                e.extend([[order[0], order[-1]], [order[-1], order[0]]])
            edges.append(e)
        case(k, *edges)
    assert len(calls) == 600
    return calls
