import random

_STATEMENT_EXAMPLES = (
    "candidate(s='RLRRLLRLRL')",
    "candidate(s='RLRRRLLRLL')",
    "candidate(s='LLLLRRRR')",
)


def generate(seed: int = 0) -> list[str]:
    """Generate balanced strings with equal R/L counts and length at most 1000."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    while len(calls) < 600:
        pairs = 500 if len(calls) == 0 else rng.randint(1, 500)
        balance = 0
        chars: list[str] = []
        for remaining in range(pairs * 2):
            if balance == 0 or (balance < pairs and rng.randrange(2)):
                chars.append("R")
                balance += 1
            else:
                chars.append("L")
                balance -= 1
        chars.extend("L" for _ in range(balance))
        s = "".join(chars)
        if len(s) <= 1000:
            call = f"candidate(s={s!r})"
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
