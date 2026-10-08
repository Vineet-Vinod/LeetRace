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
        assert 2 <= len(s) <= 30000 and all("a" <= c <= "z" for c in s)
        add(s=s)

    for s in [
        "banana",
        "abcd",
        "aa",
        "ababcdcd",
        "a" * 30000,
        "abcdefghijklmnopqrstuvwxyz" * 1153,
    ]:
        case(s)
    case("abxyabzzxy")
    while len(calls) < 600:
        s = "".join(rng.choice("abcdef") for _ in range(rng.randint(2, 90)))
        if len(calls) % 4 == 0:
            s = "".join(rng.sample("abcdefghijklmnopqrstuvwxyz", rng.randint(2, 26)))
        elif len(calls) % 2:
            s = s + s[: rng.randint(1, len(s))]
        case(s)
    assert len(calls) == 600
    return calls
