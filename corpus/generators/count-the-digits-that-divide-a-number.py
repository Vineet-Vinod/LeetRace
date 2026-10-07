import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = {f"candidate(num={n})" for n in (1, 7, 121, 1248, 999999999, 214748364)}
    while len(calls) < 600:
        digits = str(rng.randint(1, 9)) + "".join(
            str(rng.randint(1, 9)) for _ in range(rng.randint(0, 8))
        )
        calls.add(f"candidate(num={int(digits)})")
    return sorted(calls)
