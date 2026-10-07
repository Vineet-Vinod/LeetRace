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

    def case(left, right):
        assert 1 <= left <= right <= 10000
        add(left=left, right=right)

    for a, b in [
        (1, 1),
        (1, 4),
        (2, 11),
        (371, 375),
        (1, 10000),
        (9990, 10000),
        (10000, 10000),
        (1, 30),
    ]:
        case(a, b)
    while len(calls) < 600:
        a = rng.randint(1, 10000)
        case(a, min(10000, a + rng.randint(0, 180)))
    assert len(calls) == 600
    return calls
