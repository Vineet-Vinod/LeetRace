import math
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = {
        "candidate(x=3, y=5, target=4)",
        "candidate(x=2, y=6, target=5)",
        "candidate(x=1000, y=1000, target=1000)",
        "candidate(x=499, y=500, target=1000)",
        "candidate(x=2, y=3, target=1)",
        "candidate(x=1, y=1, target=2)",
    }

    def add(x: int, y: int, target: int) -> None:
        assert 1 <= x <= 1000 and 1 <= y <= 1000
        assert 1 <= target <= 1000
        cases.add(f"candidate(x={x}, y={y}, target={target})")

    # Small capacities support direct state-space checks against the gcd rule.
    for x in range(1, 13):
        for y in range(1, 13):
            g = math.gcd(x, y)
            for target in {1, g, min(x + y, 1000), min(x + y + 1, 1000)}:
                add(x, y, target)

    while len(cases) < 600:
        family = len(cases) % 4
        if family == 0:
            x, y = rng.randint(1, 1000), rng.randint(1, 1000)
            divisor = math.gcd(x, y)
            max_multiple = min((x + y) // divisor, 1000 // divisor)
            target = divisor * rng.randint(1, max_multiple)
        elif family == 1:
            x, y = 2 * rng.randint(1, 500), 2 * rng.randint(1, 500)
            target = rng.randrange(1, min(x + y, 1000) + 1, 2)
        elif family == 2:
            x, y = rng.randint(1, 499), rng.randint(1, 499)
            target = rng.randint(x + y + 1, 1000)
        else:
            x, y = rng.randint(1, 1000), rng.randint(1, 1000)
            target = rng.randint(1, 1000)
        add(x, y, target)

    assert 500 <= len(cases) <= 999 and len(cases) == len(set(cases))
    return sorted(cases)
