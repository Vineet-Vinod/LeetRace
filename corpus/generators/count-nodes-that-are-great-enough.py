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

    def case(values, k):
        assert values and values[0] is not None
        count = sum(x is not None for x in values)
        assert 1 <= count <= 10000 and all(x is None or 1 <= x <= 10000 for x in values)
        pending = 1
        for x in values:
            assert pending > 0
            pending -= 1
            if x is not None:
                pending += 2
        assert 1 <= k <= 10
        call = f"candidate(root=tree_node({values!r}), k={k})"
        if call not in seen:
            seen.add(call)
            calls.append(call)

    case([7, 6, 5, 4, 3, 2, 1], 2)
    case([3, 2, 2], 2)
    case(list(range(10000, 0, -1)), 10)
    case([10000] * 10000, 1)
    case([10000] + [v for x in range(9999, 0, -1) for v in (None, x)], 1)
    case([1] + [v for x in range(2, 10001) for v in (x, None)], 10)
    case([5, None, 4, 3, None, None, 2], 1)
    case([1, 2, 3], 1)
    while len(calls) < 600:
        n = rng.randint(1, 80)
        mode = len(calls) % 4
        a = (
            sorted([rng.randint(1, 10000) for _ in range(n)], reverse=mode == 0)
            if mode < 2
            else [rng.randint(1, 8) for _ in range(n)]
        )
        if mode == 3:
            sparse = [a[0]]
            pending = 2
            for value in a[1:]:
                if pending >= 2 and rng.randrange(2):
                    sparse.append(None)
                    pending -= 1
                sparse.append(value)
                pending += 1
            a = sparse
        case(a, rng.randint(1, 10))
    assert len(calls) == 600
    return calls
