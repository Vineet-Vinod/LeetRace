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

    def case(n):
        assert 1 <= n <= 1000000000
        add(n=n)

    for n in [1, 2, 5, 1000000000] + [
        x for b in range(1, 30) for x in [(1 << b) - 1, 1 << b, (1 << b) + 1]
    ]:
        case(n)
    while len(calls) < 600:
        case(rng.randint(1, 1000000000))
    assert len(calls) == 600
    return calls
