import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {"0", "(1+(2*3)+((8)/4))+1", "(1)+((2))+(((3)))", "()(())((()()))"}
    operators = "+-*/"
    cases.add("(" * 48 + "1+2" + ")" * 48)
    while len(cases) < 600:
        depth = rng.randint(0, 40)
        term_count = rng.randint(1, 10)
        inside = str(rng.randrange(10))
        for _ in range(term_count - 1):
            inside += rng.choice(operators) + str(rng.randrange(10))
        cases.add("(" * depth + inside + ")" * depth)
    return [f"candidate(s={value!r})" for value in cases]
