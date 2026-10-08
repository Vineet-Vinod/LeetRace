import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {"()", "(())", "()()"}
    while len(cases) < 600:
        pairs = rng.randint(1, 12)
        depth = 0
        chars = []
        for _ in range(2 * pairs):
            if depth == 0 or (depth < pairs and rng.random() < 0.5):
                chars.append("(")
                depth += 1
            else:
                chars.append(")")
                depth -= 1
        chars.extend(")" * depth)
        candidate = "".join(chars)
        # Generate balanced strings by closing every opened prefix.
        balance = 0
        fixed = []
        for char in candidate:
            if char == "(":
                balance += 1
            elif balance:
                balance -= 1
            else:
                char = "("
                balance += 1
            fixed.append(char)
        cases.add("".join(fixed) + ")" * balance)
    return [f"candidate(s={s!r})" for s in cases]
