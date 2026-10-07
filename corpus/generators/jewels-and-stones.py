import random
import string

_STATEMENT_EXAMPLES = (
    "candidate(jewels='aA', stones='aAAbbbb')",
    "candidate(jewels='z', stones='ZZ')",
)


def generate(seed: int = 0) -> list[str]:
    """Generate distinct jewel sets and stone strings over English letters."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    alphabet = string.ascii_letters
    while len(calls) < 600:
        jewels = "".join(rng.sample(alphabet, rng.randint(1, 20)))
        stones = "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 50)))
        call = f"candidate(jewels={jewels!r}, stones={stones!r})"
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
