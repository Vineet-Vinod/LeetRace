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
        assert 1 <= len(s) <= 100000
        # Validate grammar iteratively, including nonempty groups and operand/operator alternation.
        depth = 0
        operand = True
        for c in s:
            if c == "(":
                assert operand
                depth += 1
            elif c == ")":
                assert not operand and depth > 0
                depth -= 1
            elif c in "01":
                assert operand
                operand = False
            else:
                assert c in "&|" and not operand
                operand = True
        assert depth == 0 and not operand
        add(expression=s)

    def expression(depth):
        if depth == 0 or rng.randrange(4) == 0:
            return rng.choice("01")
        return (
            "(" + expression(depth - 1) + rng.choice("&|") + expression(depth - 1) + ")"
        )

    for s in [
        "1",
        "0",
        "1&(0|1)",
        "(0&0)&(0&0&0)",
        "(0|(1|0&1))",
        "&".join(["0"] * 50000),
        "(" * 49999 + "1" + ")" * 49999,
    ]:
        case(s)
    for depth in range(1, 15):
        s = "0"
        for _ in range(depth):
            s = "(" + s + "&" + s + ")"
        case(s)
    while len(calls) < 600:
        case(expression(rng.randint(2, 5)))
    assert len(calls) == 600
    return calls
