import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        s = kwargs["expression"]
        assert 1 <= len(s) <= 20000 and set(s) <= set("()&|!tf,")
        # Inputs are built from the grammar. Check it again with an iterative arity parser.
        stack = []
        pending = None
        for c in s:
            if c in "!&|":
                assert pending is None
                pending = c
            elif c == "(":
                assert pending is not None
                stack.append([pending, 0])
                pending = None
            elif c in "tf":
                assert pending is None
                if stack:
                    stack[-1][1] += 1
            elif c == ")":
                assert stack and pending is None
                op, count = stack.pop()
                assert count == 1 if op == "!" else count >= 1
                if stack:
                    stack[-1][1] += 1
        assert not stack and pending is None
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(expression="&(|(f))")
    add(expression="|(f,f,f,t)")
    add(expression="!(&(f,t))")
    add(expression="!(" * 6666 + "t" + ")" * 6666)
    add(expression="&(" + ",".join(["t"] * 9999) + ")")
    add(expression="|(" + ",".join(["f"] * 9999) + ")")
    while len(calls) < 600:

        def expr(depth):
            if depth == 0 or rng.random() < 0.3:
                return rng.choice("tf")
            op = rng.choice("!&|")
            count = 1 if op == "!" else rng.randint(1, 5)
            return op + "(" + ",".join(expr(depth - 1) for _ in range(count)) + ")"

        add(expression=expr(rng.randint(1, 5)))
    return calls
