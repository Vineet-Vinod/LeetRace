def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(tokens=['2', '1', '+', '3', '*'])",
        "candidate(tokens=['4', '13', '5', '/', '+'])",
        "candidate(tokens=['200', '200', '200', '200', '*', '*', '*'])",
        f"candidate(tokens={(['200'] * 5000 + ['+'] * 4999)!r})",
    }

    def trunc_div(left: int, right: int) -> int:
        magnitude = abs(left) // abs(right)
        return -magnitude if (left < 0) != (right < 0) else magnitude

    while len(cases) < 600:
        operand_count = rng.randint(1, 30)
        tokens: list[str] = []
        stack: list[int] = []
        for index in range(operand_count):
            value = rng.randint(-200, 200)
            tokens.append(str(value))
            stack.append(value)
            while len(stack) >= 2 and (
                index == operand_count - 1 or rng.random() < 0.55
            ):
                right, left = stack[-1], stack[-2]
                choices = []
                if -(2**31) <= left + right <= 2**31 - 1:
                    choices.append("+")
                if -(2**31) <= left - right <= 2**31 - 1:
                    choices.append("-")
                if abs(left * right) <= 2**31 - 1:
                    choices.append("*")
                if right != 0:
                    quotient = trunc_div(left, right)
                    if -(2**31) <= quotient <= 2**31 - 1:
                        choices.append("/")
                operator = rng.choice(choices)
                stack.pop()
                stack.pop()
                if operator == "+":
                    result = left + right
                elif operator == "-":
                    result = left - right
                elif operator == "*":
                    result = left * right
                else:
                    result = trunc_div(left, right)
                assert -(2**31) <= result <= 2**31 - 1
                stack.append(result)
                tokens.append(operator)
        while len(stack) > 1:
            right, left = stack.pop(), stack.pop()
            choices = []
            if -(2**31) <= left + right <= 2**31 - 1:
                choices.append("+")
            if -(2**31) <= left - right <= 2**31 - 1:
                choices.append("-")
            operator = rng.choice(choices)
            result = left + right if operator == "+" else left - right
            assert -(2**31) <= result <= 2**31 - 1
            stack.append(result)
            tokens.append(operator)
        assert 1 <= len(tokens) <= 10000 and len(stack) == 1
        cases.add(f"candidate(tokens={tokens!r})")
    return sorted(cases)
