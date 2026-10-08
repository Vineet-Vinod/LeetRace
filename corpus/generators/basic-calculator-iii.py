import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def valid(s):
        if not (1 <= len(s) <= 10000 and all(c in "0123456789+-*/()" for c in s)):
            return False
        # Independently evaluate a parsed expression to enforce division and
        # signed-32-bit intermediate promises, including the maximum-length sum.
        if len(s) > 2000:
            return s == "10" + "+1" * 4999

        def visit(node):
            if isinstance(node, ast.Constant):
                value = node.value
            elif isinstance(node, ast.UnaryOp):
                value = visit(node.operand)
                if isinstance(node.op, ast.USub):
                    value = -value
            else:
                a, b = visit(node.left), visit(node.right)
                if isinstance(node.op, ast.Add):
                    value = a + b
                elif isinstance(node.op, ast.Sub):
                    value = a - b
                elif isinstance(node.op, ast.Mult):
                    value = a * b
                else:
                    assert b != 0
                    value = (abs(a) // abs(b)) * (-1 if (a < 0) != (b < 0) else 1)
            assert -(2**31) <= value <= 2**31 - 1
            return value

        visit(ast.parse(s, mode="eval").body)
        return True

    def emit(**args):
        assert valid(**args), args
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in args.items()) + ")"
        calls[call] = None

    for s in [
        "1+1",
        "6-4/2",
        "2*(5+5*2)/3+(6/2+8)",
        "0",
        "2147483647",
        "(0-2147483647)-1",
        "(0-7)/2",
        "7/(0-2)",
        "-1+2",
        "2*-3",
        "-(-3)+4",
        "-(2+3)*4",
        "1-(-(-2))",
        "10" + "+1" * 4999,
    ]:
        emit(s=s)
    while len(calls) < 600:
        a, b, c, d = [rng.randrange(1000) for _ in range(4)]
        d = max(d, 1)
        s = rng.choice(
            [
                f"{a}+{b}*{c}",
                f"({a}-{b})/{d}",
                f"{a}*({b}-{c})/{d}",
                f"(({a}+{b})*{c}-{d})",
                f"{a}-({b}-{c})",
                f"{a}/{d}*{b}",
            ]
        )
        emit(s=s)
    assert len(calls) == 600
    return list(calls)
