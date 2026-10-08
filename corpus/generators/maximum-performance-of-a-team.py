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

    def case(s, e, k):
        n = len(s)
        assert 1 <= k <= n <= 100000 and len(e) == n
        assert all(1 <= x <= 100000 for x in s) and all(1 <= x <= 100000000 for x in e)
        add(n=n, speed=s, efficiency=e, k=k)

    case([2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 2)
    case([100000] * 100000, [100000000] * 100000, 100000)
    case(list(range(1, 100001)), list(range(100000, 0, -1)), 1)
    case([2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 3)
    case([2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 4)
    while len(calls) < 600:
        n = rng.randint(1, 50)
        case(
            [rng.randint(1, 100000) for _ in range(n)],
            [rng.randint(1, 100000000) for _ in range(n)],
            rng.randint(1, n),
        )
    assert len(calls) == 600
    return calls
