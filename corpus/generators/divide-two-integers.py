import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: dividend/divisor signed 32-bit; divisor nonzero."""
    rng = random.Random(seed)
    calls = {
        "candidate(dividend=10, divisor=3)",
        "candidate(dividend=7, divisor=-3)",
        "candidate(dividend=-(2**31), divisor=-1)",
    }
    while len(calls) < 600:
        dividend = rng.randint(-(2**31), 2**31 - 1)
        divisor = rng.randint(-(2**31), 2**31 - 1)
        if divisor == 0:
            divisor = 1
        calls.add(f"candidate(dividend={dividend}, divisor={divisor})")
    return sorted(calls)
