import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set()
    for i in range(600):
        length = 1 + rng.randrange(160)
        if i % 3 == 0:
            alphabet = "abc"
        else:
            alphabet = string.ascii_lowercase
        s = "".join(rng.choice(alphabet) for _ in range(length))
        cases.add(f"candidate(s={s!r})")
    return sorted(cases)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(s='bac')",
    "candidate(s='zza')",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
