import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    values = {1, 2, 7, 10, 44, 10**18}
    # Products formed by digits 2 through 9 exercise representable results.
    for _ in range(150):
        product = 1
        for _ in range(rng.randint(1, 12)):
            product *= rng.randint(2, 9)
        if product <= 10**18:
            values.add(product)
    while len(values) < 600:
        values.add(rng.randint(1, 10**18))
    calls = [f"candidate(n={n})" for n in values]
    assert 500 <= len(calls) <= 999
    assert len(calls) == len(set(calls))
    return calls
