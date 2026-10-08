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

    def case(a, q):
        assert 1 <= len(a) <= 50000 and all(-100000 <= x <= 100000 for x in a)
        assert 1 <= len(q) <= 50000 and all(
            0 <= i < len(a) and -100000 <= x <= 100000 for i, x in q
        )
        add(nums=a, queries=q)

    case([3, 5, 9], [[1, -2], [0, -3]])
    case([0, -1], [[0, -5]])
    case([100000] * 50000, [[0, -100000], [49999, -100000]])
    case([0, 0], [[i % 2, 100000 if i % 3 else -100000] for i in range(50000)])
    while len(calls) < 600:
        n = rng.randint(1, 35)
        mode = len(calls) % 3
        bounds = (-100, 0) if mode == 0 else (0, 100) if mode == 1 else (-100, 100)
        a = [rng.randint(*bounds) for _ in range(n)]
        q = [
            [rng.randrange(n), rng.randint(*bounds)] for _ in range(rng.randint(1, 25))
        ]
        case(a, q)
    assert len(calls) == 600
    return calls
