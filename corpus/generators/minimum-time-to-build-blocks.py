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

    def case(a, s):
        assert (
            1 <= len(a) <= 1000 and all(1 <= x <= 100000 for x in a) and 1 <= s <= 100
        )
        add(blocks=a, split=s)

    case([1], 1)
    case([1, 2], 5)
    case([1, 2, 3], 1)
    case([100000] * 1000, 100)
    case(list(range(1, 1001)), 1)
    while len(calls) < 600:
        case(
            [rng.randint(1, 100000) for _ in range(rng.randint(1, 70))],
            rng.randint(1, 100),
        )
    assert len(calls) == 600
    return calls
