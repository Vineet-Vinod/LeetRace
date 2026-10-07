import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {(2, 3, 1, 2), (4, 4, 4, 3)}
    while len(cases) < 600:
        maximum = rng.randint(1, 1000)
        minimum = rng.randint(1, maximum)
        cases.add((minimum, maximum, rng.randint(1, maximum), rng.randint(1, maximum)))
    cases.update({(1, 100000, 1, 2), (100000, 100000, 3, 7)})
    return [
        f"candidate(minLength={lo}, maxLength={hi}, oneGroup={one}, zeroGroup={zero})"
        for lo, hi, one, zero in cases
    ]
