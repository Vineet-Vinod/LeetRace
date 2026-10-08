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

    def case(n, a):
        assert 1 <= n <= 10000 and len(a) == n + 1 and all(0 <= x <= 100 for x in a)
        add(n=n, ranges=a)

    case(5, [3, 4, 1, 1, 0, 0])
    case(3, [0, 0, 0, 0])
    case(10000, [0] * 10001)
    case(10000, [100] * 10001)
    while len(calls) < 600:
        n = rng.randint(1, 90)
        a = [rng.randint(0, 12) for _ in range(n + 1)]
        mode = len(calls) % 4
        if mode == 0:
            n = max(2, n)
            a = [0] * (n + 1)
            # Last tap cannot reach zero; all other taps have zero radius.
            a[n] = rng.randint(0, min(100, n - 1))
        elif mode == 1:
            a = [rng.randint(1, 100) for _ in range(n + 1)]
        case(n, a)
    assert len(calls) == 600
    return calls
