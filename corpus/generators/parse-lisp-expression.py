import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = dict.fromkeys(
        ast.unparse(ast.parse(call, mode="eval"))
        for call in [
            'candidate(expression = "(let x 2 (mult x (let x 3 y 4 (add x y))))")',
            'candidate(expression = "(let x 3 x 2 x)")',
            'candidate(expression = "(let x 1 y 2 x (add x y) (add x y))")',
        ]
    )

    def add(**kwargs):
        validate(kwargs)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        calls[ast.unparse(ast.parse(call, mode="eval"))] = None

    def evaluate(expression):
        tokens = expression.replace("(", "( ").replace(")", " )").split()

        def parse(i, env):
            token = tokens[i]
            if token != "(":
                value = int(token) if token.lstrip("-").isdigit() else env[token]
                assert -(2**31) <= value < 2**31
                return value, i + 1
            op = tokens[i + 1]
            i += 2
            if op in ("add", "mult"):
                a, i = parse(i, env)
                b, i = parse(i, env)
                value = a + b if op == "add" else a * b
                assert tokens[i] == ")" and -(2**31) <= value < 2**31
                return value, i + 1
            local = env.copy()
            while True:
                if (
                    tokens[i] == "("
                    or tokens[i].lstrip("-").isdigit()
                    or tokens[i + 1] == ")"
                ):
                    value, i = parse(i, local)
                    assert tokens[i] == ")"
                    return value, i + 1
                name = tokens[i]
                value, i = parse(i + 1, local)
                local[name] = value

        result, end = parse(0, {})
        assert end == len(tokens)
        return result

    def validate(p):
        evaluate(p["expression"])
        assert 1 <= len(p["expression"]) <= 2000
        assert (
            p["expression"] == p["expression"].strip() and "  " not in p["expression"]
        )

    add(expression="2147483647")
    add(expression="-2147483648")
    add(expression="(let " + "x" * 1990 + " 0 0)")
    attempts = 0
    while len(calls) < 600:
        attempts % 8
        attempts += 1

        def expr(depth, env):
            if depth == 0 or rng.random() < 0.3:
                if env and rng.random() < 0.5:
                    return rng.choice(env)
                return str(rng.randint(-9, 9))
            op = rng.choice(["add", "mult", "let"])
            if op == "let":
                name = rng.choice(["x", "y", "z1", "var2"])
                return (
                    "(let "
                    + name
                    + " "
                    + expr(depth - 1, env)
                    + " "
                    + expr(depth - 1, env + [name])
                    + ")"
                )
            return (
                "(" + op + " " + expr(depth - 1, env) + " " + expr(depth - 1, env) + ")"
            )

        candidate_expression = expr(rng.randint(1, 4), [])
        try:
            evaluate(candidate_expression)
        except AssertionError:
            continue
        add(expression=candidate_expression)
    return list(calls)
