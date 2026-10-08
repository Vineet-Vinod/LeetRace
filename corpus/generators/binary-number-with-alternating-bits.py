import random


def generate(seed: int = 0) -> list[str]:
    """Cover every alternating-bit input through 31 bits and varied non-alternating values."""
    rng = random.Random(seed)
    alternating = {
        int("".join("1" if index % 2 == 0 else "0" for index in range(width)), 2)
        for width in range(1, 32)
    }
    values = set(alternating)
    values.update(range(1, 301))
    while len(values) < 700:
        values.add(rng.randint(1, 2**31 - 1))
    values.add(2**31 - 1)
    return [f"candidate(n={value})" for value in sorted(values)]
