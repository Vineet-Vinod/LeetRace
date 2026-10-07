import random


def generate(seed: int = 0) -> list[str]:
    """Cover small intervals and large endpoint cases with 0 <= low <= high <= 10^9."""
    rng = random.Random(seed)
    cases = {(low, high) for low in range(25) for high in range(low, 25)}
    cases.update(
        {
            (0, 10**9),
            (10**9, 10**9),
            (10**9 - 1, 10**9),
            (0, 0),
            (1, 1),
        }
    )
    while len(cases) < 700:
        low = rng.randint(0, 10**9)
        high = rng.randint(low, 10**9)
        cases.add((low, high))
    return [f"candidate(low={low}, high={high})" for low, high in sorted(cases)]
