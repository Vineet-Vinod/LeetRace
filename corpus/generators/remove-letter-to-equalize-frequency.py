import random
import string

_STATEMENT_EXAMPLES = ("candidate(word='abcc')", "candidate(word='aazz')")


def generate(seed: int = 0) -> list[str]:
    """Generate lowercase words of length 2..100."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    while len(calls) < 600:
        word = "".join(
            rng.choice(string.ascii_lowercase) for _ in range(rng.randint(2, 100))
        )
        call = f"candidate(word={word!r})"
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
