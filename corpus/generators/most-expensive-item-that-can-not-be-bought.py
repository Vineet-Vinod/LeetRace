import random


def primes(limit: int) -> list[int]:
    result = []
    for value in range(2, limit + 1):
        if all(value % divisor for divisor in range(2, int(value**0.5) + 1)):
            result.append(value)
    return result


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    values = primes(997)
    calls: set[str] = set()
    while len(calls) < 600:
        first, second = rng.sample(values, 2)
        if first * second < 100000:
            calls.add(f"candidate(primeOne={first}, primeTwo={second})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(primeOne=2, primeTwo=5)",
    "candidate(primeOne=5, primeTwo=7)",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
