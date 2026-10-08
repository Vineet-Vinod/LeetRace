def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(['candidate(expression="2-1-1")', 'candidate(expression="2*3-4*5")'])
    ops = "+-*"
    for index in range(600):
        count = 1 + index % 8
        numbers = [str(rng.randint(0, 99)) for _ in range(count)]
        expression = numbers[0]
        for number in numbers[1:]:
            expression += rng.choice(ops) + number
        if len(expression) > 20:
            expression = (
                str(rng.randint(0, 99)) + rng.choice(ops) + str(rng.randint(0, 99))
            )
        cases.add(f"candidate(expression={expression!r})")
    while len(cases) < 600:
        numbers = [str(rng.randint(0, 99)) for _ in range(rng.randint(1, 5))]
        expression = numbers[0] + "".join(
            rng.choice(ops) + number for number in numbers[1:]
        )
        cases.add(f"candidate(expression={expression!r})")
    return sorted(cases)
