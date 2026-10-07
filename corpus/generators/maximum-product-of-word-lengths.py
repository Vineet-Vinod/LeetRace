import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        words = [
            "".join(
                rng.choice(string.ascii_lowercase) for _ in range(rng.randint(1, 100))
            )
            for _ in range(rng.randint(2, 100))
        ]
        calls.add(f"candidate(words={words!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(words=['a', 'aa', 'aaa', 'aaaa'])",
    "candidate(words=['abcw', 'baz', 'foo', 'bar', 'xtfn', 'abcdef'])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
