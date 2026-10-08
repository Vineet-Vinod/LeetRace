import random
import string

_STATEMENT_EXAMPLES = (
    "candidate(s='abc', shift=[[0, 1], [1, 2]])",
    "candidate(s='abcdefg', shift=[[1, 1], [1, 1], [0, 2], [1, 3]])",
)


def generate(seed: int = 0) -> list[str]:
    """Generate lowercase strings and 1..100 valid directional shift operations."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    while len(calls) < 600:
        s = "".join(
            rng.choice(string.ascii_lowercase) for _ in range(rng.randint(1, 100))
        )
        shifts = [
            [rng.randrange(2), rng.randint(0, 100)] for _ in range(rng.randint(1, 100))
        ]
        call = f"candidate(s={s!r}, shift={shifts!r})"
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
