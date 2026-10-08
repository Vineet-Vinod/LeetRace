import random
import string

_STATEMENT_EXAMPLES = (
    "candidate(title='capiTalIze tHe titLe')",
    "candidate(title='First leTTeR of EACH Word')",
    "candidate(title='i lOve leetcode')",
)


def generate(seed: int = 0) -> list[str]:
    """Generate 600 distinct titles of lowercase English words and spaces."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    while len(calls) < 600:
        words = [
            "".join(
                rng.choice(string.ascii_lowercase) for _ in range(rng.randint(1, 10))
            )
            for _ in range(rng.randint(1, 9))
        ]
        title = " ".join(words)
        call = f"candidate(title={title!r})"
        if call not in seen:
            calls.append(call)
            seen.add(call)
    return calls


_BASE_GENERATE = generate


def generate(seed: int = 0) -> list[str]:
    calls = list(_STATEMENT_EXAMPLES)
    seen = set(calls)
    for call in _BASE_GENERATE(seed):
        if call not in seen:
            calls.append(call)
            seen.add(call)
    limit = globals().get("DOMAIN_SIZE", 600)
    if len(calls) < limit:
        raise ValueError("Generator did not produce enough distinct cases")
    return calls[:limit]
