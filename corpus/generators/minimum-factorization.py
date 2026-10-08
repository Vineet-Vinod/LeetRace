import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    values = {1, 2, 10, 15, 48, 100, 2**31 - 1, 9**9}
    while len(values) < 600:
        if rng.random() < 0.55:
            digits = [rng.randint(2, 9) for _ in range(rng.randint(1, 8))]
            product = 1
            for digit in digits:
                product *= digit
            if product <= 2**31 - 1:
                values.add(product)
        else:
            values.add(rng.randint(1, 2**31 - 1))
    assert len(values) == 600 and all(1 <= v <= 2**31 - 1 for v in values)
    return [f"candidate(num={v})" for v in sorted(values)]
