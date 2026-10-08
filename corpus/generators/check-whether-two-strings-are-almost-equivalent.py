import random
import string

_STATEMENT_EXAMPLES = (
    "candidate(word1='aaaa', word2='bccb')",
    "candidate(word1='abcdeef', word2='abaaacc')",
    "candidate(word1='cccddabba', word2='babababab')",
)


def generate(seed: int = 0) -> list[str]:
    """Generate distinct equal-length lowercase string pairs, each length <= 100."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    while len(calls) < 600:
        length = rng.randint(1, 100)
        first = "".join(rng.choice(string.ascii_lowercase) for _ in range(length))
        second = "".join(rng.choice(string.ascii_lowercase) for _ in range(length))
        call = f"candidate(word1={first!r}, word2={second!r})"
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
