import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    values = {0, 1, -1, 120, -120, 1534236469, -(2**31), 2**31 - 1}
    while len(values) < 600:
        values.add(rng.randint(-(2**31), 2**31 - 1))
    return [f"candidate(x={x})" for x in sorted(values)]
