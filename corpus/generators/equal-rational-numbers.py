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

    def valid(s):
        import re

        match = re.fullmatch(
            r"(0|[1-9][0-9]{0,3})(?:\.([0-9]{0,4})(?:\(([0-9]{1,4})\))?)?", s
        )
        assert match is not None

    def case(s, t):
        valid(s)
        valid(t)
        add(s=s, t=t)

    case("0.(52)", "0.5(25)")
    case("0.1666(6)", "0.166(66)")
    case("0.9(9)", "1.")
    case("9999.9999(9999)", "9999.9999")
    while len(calls) < 600:
        integer = str(rng.randint(0, 9999))
        mode = len(calls) % 4
        if mode == 0:
            finite = "".join(rng.choice("0123456789") for _ in range(rng.randint(0, 4)))
            s = integer + "." + finite
            t = s + "(0)"
        elif mode == 1:
            rep = "".join(rng.choice("0123456789") for _ in range(rng.randint(1, 2)))
            s = integer + ".(" + rep + ")"
            t = integer + "." + rep + "(" + rep * 2 + ")"
        elif mode == 2:
            s = (
                integer
                + "."
                + str(rng.randint(0, 9999))
                + "("
                + str(rng.randint(0, 9999))
                + ")"
            )
            t = s
        else:
            s = integer
            t = str((int(integer) + 1) % 10000)
        case(s, t)
    assert len(calls) == 600
    return calls
