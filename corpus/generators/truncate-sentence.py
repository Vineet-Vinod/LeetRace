import random
import string

_STATEMENT_EXAMPLES = (
    "candidate(s='Hello how are you Contestant', k=4)",
    "candidate(s='What is the solution to this problem', k=4)",
    "candidate(s='chopper is not a tanuki', k=5)",
)


def generate(seed: int = 0) -> list[str]:
    """Generate sentences of 1..50 lowercase words, each at most 9 letters and valid prefix lengths."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    while len(calls) < 600:
        words = [
            "".join(
                rng.choice(string.ascii_lowercase) for _ in range(rng.randint(1, 9))
            )
            for _ in range(rng.randint(1, 50))
        ]
        k = rng.randint(1, len(words))
        call = f"candidate(s={' '.join(words)!r}, k={k})"
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
