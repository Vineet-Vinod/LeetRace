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

    def case(a):
        assert 1 <= len(a) <= 20000 and all(0 <= x < 100000 for x in a)
        add(arr=a)

    for a in (
        [10, 13, 12, 14, 15],
        [2, 3, 1, 1, 4],
        [5, 1, 3, 4, 2],
        [0] * 20000,
        list(range(20000)),
        list(range(99999, 79999, -1)),
    ):
        case(a)
    while len(calls) < 600:
        case([rng.randint(0, 20) for _ in range(rng.randint(1, 70))])
    assert len(calls) == 600
    return calls
