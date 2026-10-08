import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        word = "".join(rng.choice("abc") for _ in range(rng.randint(1, 50)))
        calls.add(f"candidate(word={word!r})")
    return sorted(calls)


_AUDIT_BASE_GENERATE = generate
_AUDIT_BOUNDARY_CALLS = (
    "candidate(word='ab' * 25)",
    "candidate(word='abc' * 16 + 'ab')",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_AUDIT_BASE_GENERATE(seed)) | set(_AUDIT_BOUNDARY_CALLS))
