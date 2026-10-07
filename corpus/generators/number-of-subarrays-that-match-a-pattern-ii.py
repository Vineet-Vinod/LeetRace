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

    def case(a, p):
        assert 2 <= len(a) <= 1000000 and all(1 <= x <= 1000000000 for x in a)
        assert 1 <= len(p) < len(a) and all(x in (-1, 0, 1) for x in p)
        add(nums=a, pattern=p)

    case([1, 2, 3, 4, 5, 6], [1, 1])
    case([1, 4, 4, 1, 3, 5, 5, 3], [1, 0, -1])
    case([1000000000] * 1000000, [0])
    case([1] * 1000, [1] * 999)
    case([1] * 1000000, [0] * 999999)
    case([1000000000] * 1000000, [1] * 999999)
    while len(calls) < 600:
        n = rng.randint(2, 90)
        a = [rng.randint(1, 12) for _ in range(n)]
        m = rng.randint(1, n - 1)
        if len(calls) % 2:
            start = rng.randint(0, n - m - 1)
            p = [(a[i + 1] > a[i]) - (a[i + 1] < a[i]) for i in range(start, start + m)]
        else:
            p = [rng.choice([-1, 0, 1]) for _ in range(m)]
        case(a, p)
    assert len(calls) == 600
    return calls
