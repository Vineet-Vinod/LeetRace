import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        text = "".join(
            rng.choice(string.ascii_lowercase[:6]) for _ in range(rng.randint(1, 1000))
        )
        pattern = "".join(rng.choice(string.ascii_lowercase[:6]) for _ in range(2))
        calls.add(f"candidate(text={text!r}, pattern={pattern!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(text='aabb', pattern='ab')",
    "candidate(text='abdcdbc', pattern='ac')",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
