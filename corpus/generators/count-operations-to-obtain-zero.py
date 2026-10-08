import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = {
        f"candidate(num1={a}, num2={b})"
        for a, b in [(0, 0), (0, 10**5), (10**5, 1), (10**5, 10**5)]
    }
    while len(calls) < 600:
        calls.add(
            f"candidate(num1={rng.randint(0, 10**5)}, num2={rng.randint(0, 10**5)})"
        )
    return sorted(calls)
