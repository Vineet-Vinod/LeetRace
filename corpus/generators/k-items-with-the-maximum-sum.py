import random


def generate(seed: int = 0) -> list[str]:
    """Generate legal counts up to 50 and k values through the total item count."""
    rng = random.Random(seed)
    cases = {
        (ones, zeros, negative_ones, k)
        for ones in range(4)
        for zeros in range(4)
        for negative_ones in range(4)
        for k in range(ones + zeros + negative_ones + 1)
    }
    while len(cases) < 600:
        ones, zeros, negative_ones = (rng.randint(0, 50) for _ in range(3))
        k = rng.randint(0, ones + zeros + negative_ones)
        cases.add((ones, zeros, negative_ones, k))
    cases.update(
        {
            (50, 50, 50, 0),
            (50, 50, 50, 150),
            (50, 0, 0, 50),
            (0, 50, 0, 50),
            (0, 0, 50, 50),
        }
    )
    return [
        f"candidate(numOnes={ones}, numZeros={zeros}, numNegOnes={negative_ones}, k={k})"
        for ones, zeros, negative_ones, k in sorted(cases)
    ]
