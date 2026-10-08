import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    calls.add("candidate(secret='1807', guess='7810')")
    while len(calls) < 600:
        size = rng.randint(1, 1000)
        secret = "".join(rng.choice("0123456789") for _ in range(size))
        guess = "".join(rng.choice("0123456789") for _ in range(size))
        calls.add(f"candidate(secret={secret!r}, guess={guess!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = ("candidate(secret='1123', guess='0111')",)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
