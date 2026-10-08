import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        words = [
            "".join(rng.choice("abcdef") for _ in range(2))
            for _ in range(rng.randint(1, 200))
        ]
        calls.add(f"candidate(words={words!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(words=['cc', 'll', 'xx'])",
    "candidate(words=['lc', 'cl', 'gg'])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
