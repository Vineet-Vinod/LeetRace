import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        word = "".join(rng.choice("aeiou") for _ in range(rng.randint(1, 2000)))
        calls.add(f"candidate(word={word!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(word='a')",
    "candidate(word='aeiaaioaaaaeiiiiouuuooaauuaeiu')",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
