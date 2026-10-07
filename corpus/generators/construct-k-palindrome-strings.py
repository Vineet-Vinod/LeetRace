import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        length = rng.randint(1, 200)
        s = "".join(rng.choice(string.ascii_lowercase) for _ in range(length))
        k = rng.randint(1, 200)
        calls.add(f"candidate(s={s!r}, k={k})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(s='annabelle', k=2)",
    "candidate(s='leetcode', k=3)",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
