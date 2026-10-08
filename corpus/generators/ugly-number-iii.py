import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, int, int, int]] = {
        (3, 2, 3, 5),
        (4, 2, 3, 4),
        (5, 2, 11, 13),
        (1, 1, 1, 1),
        (10**9, 2, 217_983_653, 336_916_467),
        (10**9, 2, 2, 2),
        (10**9, 10**9, 1, 1),
    }
    while len(cases) < 600:
        a, b, c = (rng.randint(1, 10**6) for _ in range(3))
        # The nth multiple of the smallest divisor bounds the answer.
        n = rng.randint(1, min(10**9, 2 * 10**9 // min(a, b, c)))
        cases.add((n, a, b, c))
    assert all(
        1 <= n <= 10**9
        and 1 <= a <= 10**9
        and 1 <= b <= 10**9
        and 1 <= c <= 10**9
        and a * b * c <= 10**18
        for n, a, b, c in cases
    )
    return [f"candidate(n={n}, a={a}, b={b}, c={c})" for n, a, b, c in sorted(cases)]
