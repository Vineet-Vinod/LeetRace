import random
import string

_STATEMENT_EXAMPLES = (
    "candidate(words=['bella', 'label', 'roller'])",
    "candidate(words=['cool', 'lock', 'cook'])",
)


def generate(seed: int = 0) -> list[str]:
    """Generate lists of 1..100 lowercase words, each with length 1..100."""
    rng = random.Random(seed)
    calls = [f"candidate(words={(['a' * 100] * 100)!r})"]
    seen = set(calls)
    while len(calls) < 600:
        words = [
            "".join(
                rng.choice(string.ascii_lowercase) for _ in range(rng.randint(1, 30))
            )
            for _ in range(rng.randint(1, 8))
        ]
        call = f"candidate(words={words!r})"
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
