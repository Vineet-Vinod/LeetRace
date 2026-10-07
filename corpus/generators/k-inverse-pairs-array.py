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

    def case(n, k):
        assert 1 <= n <= 1000 and 0 <= k <= 1000
        add(n=n, k=k)

    case(1000, 1000)
    case(1000, 0)
    case(1, 1000)
    for n in range(1, 20):
        for k in [0, 1, min(1000, n * (n - 1) // 2), min(1000, n * (n - 1) // 2 + 1)]:
            case(n, k)
    while len(calls) < 600:
        case(rng.randint(1, 70), rng.randint(0, 120))
    assert len(calls) == 600
    return calls
