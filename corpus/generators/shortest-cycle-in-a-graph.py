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

    def case(n, e):
        assert 2 <= n <= 1000 and 1 <= len(e) <= 1000
        assert all(0 <= a < n and 0 <= b < n and a != b for a, b in e)
        assert len({tuple(sorted(edge)) for edge in e}) == len(e)
        add(n=n, edges=e)

    case(7, [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 6], [6, 3]])
    case(1000, [[i, i + 1] for i in range(999)] + [[999, 0]])
    case(1000, [[i, i + 1] for i in range(999)])
    case(4, [[0, 1], [0, 2]])
    while len(calls) < 600:
        n = rng.randint(2, 40)
        mode = len(calls) % 3
        if mode == 0:
            e = [[i, rng.randrange(i)] for i in range(1, n)]
        elif mode == 1:
            length = rng.randint(3, max(3, n))
            n = max(n, length)
            e = [[i, (i + 1) % length] for i in range(length)]
        else:
            e = [
                list(edge)
                for edge in rng.sample(
                    [(a, b) for a in range(n) for b in range(a + 1, n)],
                    rng.randint(1, min(80, n * (n - 1) // 2)),
                )
            ]
        case(n, e)
    assert len(calls) == 600
    return calls
