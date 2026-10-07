import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    values = set(range(1, 601))
    values.update(
        10**k + d for k in range(1, 8) for d in (-1, 0, 1) if 1 <= 10**k + d <= 10**8
    )
    selected = sorted(values)[:550]
    while len(selected) < 599:
        value = rng.randint(1, 10**8)
        if value not in values:
            values.add(value)
            selected.append(value)
    selected.append(10**8)
    return [f"candidate(n={value})" for value in selected]
