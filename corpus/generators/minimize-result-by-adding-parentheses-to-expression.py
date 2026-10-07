import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        "candidate(expression='247+38')",
        "candidate(expression='12+34')",
        "candidate(expression='999+999')",
        "candidate(expression='11111111+1')",
        "candidate(expression='1+11111111')",
    }

    def value_with_any_parentheses_fits(expression: str) -> bool:
        plus = expression.index("+")
        left, right = expression[:plus], expression[plus + 1 :]
        for start in range(len(left)):
            for end in range(1, len(right) + 1):
                prefix = int(left[:start]) if start else 1
                middle = int(left[start:]) + int(right[:end])
                suffix = int(right[end:]) if end < len(right) else 1
                if prefix * middle * suffix > 2**31 - 1:
                    return False
        return True

    def add(expression: str) -> None:
        assert 3 <= len(expression) <= 10
        assert expression.count("+") == 1
        left, right = expression.split("+")
        assert left and right and all(char in "123456789" for char in left + right)
        assert value_with_any_parentheses_fits(expression)
        cases.add(f"candidate(expression={expression!r})")

    for expression in list(cases):
        add(expression.split("='")[1].split("'")[0])
    while len(cases) < 600:
        digit_count = rng.randint(2, 9)
        left_length = rng.randint(1, digit_count - 1)
        left = "".join(str(rng.randint(1, 9)) for _ in range(left_length))
        right = "".join(
            str(rng.randint(1, 9)) for _ in range(digit_count - left_length)
        )
        expression = left + "+" + right
        if value_with_any_parentheses_fits(expression):
            add(expression)
    return sorted(cases)
