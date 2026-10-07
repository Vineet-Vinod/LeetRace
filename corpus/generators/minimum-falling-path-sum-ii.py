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
        assert 1 <= len(a) <= 200 and all(len(row) == len(a) for row in a)
        assert all(-99 <= x <= 99 for row in a for x in row)
        add(grid=a)

    case([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    case([[7]])
    case([[-99] * 200 for _ in range(200)])
    case([[99] * 200 for _ in range(200)])
    while len(calls) < 600:
        n = rng.randint(1, 14)
        case([[rng.randint(-99, 99) for _ in range(n)] for _ in range(n)])
    assert len(calls) == 600
    return calls
