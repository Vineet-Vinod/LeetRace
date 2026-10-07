import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    true_calls: set[str] = set()
    while len(true_calls) < 300:
        n = 1 + rng.randrange(30)
        parts = [format(value, "b") for value in range(1, n + 1)]
        rng.shuffle(parts)
        s = "0".join(parts)
        true_calls.add(f"candidate(s={s!r}, n={n})")
    calls.update(true_calls)
    false_calls: set[str] = set()
    while len(false_calls) < 300:
        size = 1 + rng.randrange(1000)
        s = "0" * size
        n = 1 + rng.randrange(10**9)
        false_calls.add(f"candidate(s={s!r}, n={n})")
    calls.update(false_calls)
    calls.update(
        (
            "candidate(s='0110', n=3)",
            "candidate(s='1' * 1000, n=1)",
            "candidate(s='1' * 1000, n=1000000000)",
            "candidate(s='0' * 1000, n=1)",
        )
    )
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = ("candidate(s='0110', n=4)",)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
