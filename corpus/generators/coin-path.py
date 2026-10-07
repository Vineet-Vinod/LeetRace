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

    def case(a, jump):
        assert 1 <= len(a) <= 1000 and 1 <= jump <= 100
        assert a[0] != -1 and all(-1 <= x <= 100 for x in a)
        add(coins=a, maxJump=jump)

    case([1, 2, 4, -1, 2], 2)
    case([1, 2, 4, -1, 2], 1)
    case([0] * 1000, 100)
    case([100] * 1000, 1)
    case([0] + [-1] * 999, 100)
    while len(calls) < 600:
        n = rng.randint(1, 50)
        a = [rng.choice([-1, 0, 0, 1, 2, 100, rng.randint(0, 100)]) for _ in range(n)]
        a[0] = rng.randint(0, 100)
        if len(calls) % 2:
            a = [max(0, x) for x in a]
        if len(calls) % 3 == 0:
            if len(a) == 1:
                a.append(-1)
            a[-1] = -1
        case(a, rng.randint(1, 100))
    assert len(calls) == 600
    return calls
