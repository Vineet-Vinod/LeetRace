import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        n = rng.randrange(2, 102, 2)
        s = "".join(rng.choice("0123456789") for _ in range(n))
        a = rng.randint(1, 9)
        b = rng.randint(1, n - 1)
        calls.add(f"candidate(s={s!r}, a={a}, b={b})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(s='5525', a=9, b=2)",
    "candidate(s='74', a=5, b=1)",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
