import random
import string

_STATEMENT_EXAMPLES = (
    "candidate(words=['hello', 'i', 'am', 'leetcode', 'hello'], target='hello', startIndex=1)",
    "candidate(words=['a', 'b', 'leetcode'], target='leetcode', startIndex=0)",
    "candidate(words=['i', 'eat', 'leetcode'], target='ate', startIndex=0)",
)


def generate(seed: int = 0) -> list[str]:
    """Generate word lists of size 1..100 with valid lowercase targets and starts."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    while len(calls) < 600:
        words = [
            "".join(
                rng.choice(string.ascii_lowercase) for _ in range(rng.randint(1, 12))
            )
            for _ in range(rng.randint(1, 100))
        ]
        target = rng.choice(words) if rng.randrange(2) else "zzzz"
        start = rng.randrange(len(words))
        call = f"candidate(words={words!r}, target={target!r}, startIndex={start})"
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
