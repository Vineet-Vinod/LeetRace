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

    def tree(n, mode):
        # Every new vertex has exactly one edge to an earlier vertex: connected and acyclic.
        return [
            [i, i - 1 if mode == 0 else 0 if mode == 1 else rng.randrange(i)]
            for i in range(1, n)
        ]

    def case(a, b):
        for edges in (a, b):
            n = len(edges) + 1
            assert 1 <= n <= 100000
            assert all(0 <= parent < child < n for child, parent in edges)
            assert {child for child, parent in edges} == set(range(1, n))
        add(edges1=a, edges2=b)

    case([], [])
    case(tree(100000, 0), tree(100000, 1))
    case([[1, 0], [2, 0], [3, 0]], [[1, 0]])
    case(
        [[1, 0], [2, 0], [3, 0], [4, 2], [5, 2], [6, 3], [7, 2]],
        [[1, 0], [2, 0], [3, 0], [4, 2], [5, 2], [6, 3], [7, 2]],
    )
    while len(calls) < 600:
        case(
            tree(rng.randint(1, 70), rng.randrange(3)),
            tree(rng.randint(1, 70), rng.randrange(3)),
        )
    assert len(calls) == 600
    return calls
