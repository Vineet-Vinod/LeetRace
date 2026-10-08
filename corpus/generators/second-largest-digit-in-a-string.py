import random
import string

_STATEMENT_EXAMPLES = ("candidate(s='dfa12321afd')", "candidate(s='abc1111')")


def generate(seed: int = 0) -> list[str]:
    """Generate strings of lowercase letters and digits with length 1..500."""
    rng = random.Random(seed)
    alphabet = string.ascii_lowercase + string.digits
    calls: list[str] = []
    seen: set[str] = set()
    while len(calls) < 600:
        size = 500 if len(calls) == 0 else rng.randint(1, 100)
        s = "".join(rng.choice(alphabet) for _ in range(size))
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
