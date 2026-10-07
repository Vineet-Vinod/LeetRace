import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    prime_squares = {
        prime * prime
        for prime in range(2, 101)
        if all(prime % divisor != 0 for divisor in range(2, int(prime**0.5) + 1))
    }
    cases = {1, 2, 4, 9, 10_000} | prime_squares
    while len(cases) < 600:
        cases.add(rng.randint(1, 10_000))
    return [f"candidate(n={value})" for value in sorted(cases)]
