import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {"x+5-3+x=6+x-2", "x=x", "2x=x"}

    def term(coefficient: int, constant: int) -> str:
        pieces = []
        if coefficient:
            magnitude = abs(coefficient)
            pieces.append(
                ("-" if coefficient < 0 else "")
                + ("" if magnitude == 1 else str(magnitude))
                + "x"
            )
        if constant or not pieces:
            value = abs(constant)
            pieces.append(
                ("+" if constant >= 0 and pieces else "-" if constant < 0 else "")
                + str(value)
            )
        result = "".join(pieces)
        if result and result[0] == "+":
            result = result[1:]
        return result

    while len(cases) < 600:
        a, b = rng.randint(-20, 20), rng.randint(-20, 20)
        x = rng.randint(-20, 20)
        left_constant = rng.randint(-20, 20)
        right_constant = left_constant + (a - b) * x
        if not -100 <= right_constant <= 100:
            continue
        equation = f"{term(a, left_constant)}={term(b, right_constant)}"
        if len(equation) >= 3:
            cases.add(equation)
    return [f"candidate(equation={equation!r})" for equation in cases]
