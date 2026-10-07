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

    def case(a, k):
        m, n = len(a), len(a[0])
        assert (
            1 <= m <= 50000
            and 1 <= n <= 50000
            and m * n <= 50000
            and all(len(row) == n for row in a)
        )
        assert all(0 <= x <= 100 for row in a for x in row) and 1 <= k <= 50
        add(grid=a, k=k)

    case([[5, 2, 4], [3, 0, 5], [0, 7, 2]], 3)
    case([[0, 0]], 5)
    case([[100] * 50000], 50)
    case([[0] for _ in range(50000)], 1)
    case([[0] * 200 for _ in range(250)], 50)
    case([[7, 3, 4, 9], [2, 3, 6, 2], [2, 3, 7, 0]], 1)
    while len(calls) < 600:
        m, n = rng.randint(1, 9), rng.randint(1, 9)
        k = rng.randint(1, 50)
        a = [[rng.randint(0, 100) for _ in range(n)] for _ in range(m)]
        if len(calls) % 3 == 0:
            a = [[0] * n for _ in range(m)]
        case(a, k)
    assert len(calls) == 600
    return calls
