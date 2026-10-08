import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        words = set()
        while len(words) < rng.randint(1, 60):
            words.add(
                "".join(
                    rng.choice(string.ascii_lowercase[:8])
                    for _ in range(rng.randint(1, 30))
                )
            )
        calls.add(f"candidate(words={sorted(words)!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(words=['a', 'banana', 'app', 'appl', 'ap', 'apply', 'apple'])",
    "candidate(words=['w', 'wo', 'wor', 'worl', 'world'])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
