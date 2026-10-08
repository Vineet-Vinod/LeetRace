import random


def primes_up_to(limit: int) -> list[int]:
    prime = [True] * (limit + 1)
    prime[0] = prime[1] = False
    for value in range(2, int(limit**0.5) + 1):
        if prime[value]:
            for multiple in range(value * value, limit + 1, value):
                prime[multiple] = False
    return [value for value, is_prime in enumerate(prime) if is_prime]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    prime_values = primes_up_to(30_000)
    cases: set[tuple[tuple[int, ...], int]] = {
        ((1, 2, 3, 5), 3),
        ((1, 7), 1),
    }
    values = (1, *prime_values[:999])
    cases.add((values, 1))
    while len(cases) < 600:
        arr = (1, *sorted(rng.sample(prime_values, rng.randint(1, 25))))
        fraction_count = len(arr) * (len(arr) - 1) // 2
        cases.add((arr, rng.randint(1, fraction_count)))
    assert all(
        2 <= len(arr) <= 1000
        and arr[0] == 1
        and tuple(sorted(arr)) == arr
        and len(set(arr)) == len(arr)
        and all(value in prime_values for value in arr[1:])
        and 1 <= k <= len(arr) * (len(arr) - 1) // 2
        for arr, k in cases
    )
    return [f"candidate(arr={list(arr)!r}, k={k})" for arr, k in sorted(cases)]
