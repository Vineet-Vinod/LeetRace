import math
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[str, int, int]] = {
        ("0110011", 1, 2),
        ("10101", 3, 1),
        ("01", 1, 1),
        ("0" * 100_000, 1, 1),
    }
    while len(cases) < 600:
        size = rng.randint(1, 90)
        first = rng.randint(1, size)
        second = rng.randint(1, size)
        while math.gcd(first, second) != 1:
            first = rng.randint(1, size)
            second = rng.randint(1, size)
        s = "".join(rng.choice("01") for _ in range(size))
        cases.add((s, first, second))
    assert all(
        1 <= len(s) <= 100_000
        and set(s) <= {"0", "1"}
        and 1 <= num1 <= len(s)
        and 1 <= num2 <= len(s)
        and math.gcd(num1, num2) == 1
        for s, num1, num2 in cases
    )
    return [
        f"candidate(s={s!r}, num1={num1}, num2={num2})"
        for s, num1, num2 in sorted(cases)
    ]
