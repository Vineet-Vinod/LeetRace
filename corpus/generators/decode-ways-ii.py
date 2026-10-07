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

    def case(s):
        assert 1 <= len(s) <= 100000 and set(s) <= set("0123456789*")
        add(s=s)

    for s in [
        "*",
        "1*",
        "2*",
        "*0",
        "0",
        "**",
        "10",
        "30",
        "*" * 100000,
        "1" * 100000,
        "0" * 100000,
    ]:
        case(s)
    while len(calls) < 600:
        alphabet = "12*" if len(calls) % 2 else "0123456789*"
        case("".join(rng.choice(alphabet) for _ in range(rng.randint(1, 70))))
    assert len(calls) == 600
    return calls
