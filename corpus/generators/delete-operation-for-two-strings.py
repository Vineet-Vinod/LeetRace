import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        a = "".join(
            rng.choice(string.ascii_lowercase) for _ in range(rng.randint(1, 100))
        )
        b = "".join(
            rng.choice(string.ascii_lowercase) for _ in range(rng.randint(1, 100))
        )
        calls.add(f"candidate(word1={a!r}, word2={b!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(word1='leetcode', word2='etco')",
    "candidate(word1='sea', word2='eat')",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
