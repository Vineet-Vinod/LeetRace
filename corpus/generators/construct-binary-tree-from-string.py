import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {"", "4", "4(2(3)(1))(6(5))", "-4(2(3)(1))(6(5)(7))"}

    def build(depth: int) -> str:
        value = rng.randint(-(2**30), 2**30)
        if depth == 0:
            return str(value)
        left = rng.choice((True, False))
        right = rng.choice((True, False))
        if right and not left:
            left = True
        text = str(value)
        if left:
            text += "(" + build(depth - 1) + ")"
        if right:
            text += "(" + build(depth - 1) + ")"
        return text

    while len(cases) < 600:
        cases.add(build(rng.randint(0, 5)))
    return [f"candidate(s={s!r})" for s in cases]
