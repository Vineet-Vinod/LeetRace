import random
import string

_STATEMENT_EXAMPLES = (
    "candidate(strs=['alic3', 'bob', '3', '4', '00000'])",
    "candidate(strs=['1', '01', '001', '0001'])",
)


def generate(seed: int = 0) -> list[str]:
    """Generate lists of valid lowercase or digit strings, each at most 9 chars."""
    rng = random.Random(seed)
    alphabet = string.ascii_lowercase + string.digits
    calls: list[str] = []
    seen: set[str] = set()
    while len(calls) < 600:
        values = [
            "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 9)))
            for _ in range(rng.randint(1, 100))
        ]
        call = f"candidate(strs={values!r})"
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
