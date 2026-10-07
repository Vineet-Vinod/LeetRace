import random

_STATEMENT_EXAMPLES = (
    "candidate(details=['7868190130M7522', '5303914400F9211', '9273338290F4010'])",
    "candidate(details=['1313579440F2036', '2921522980M5644'])",
)


def generate(seed: int = 0) -> list[str]:
    """Generate passenger details of 15 digits/chars with unique phone and seat fields."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    while len(calls) < 600:
        count = rng.randint(1, 100)
        phones = rng.sample(range(10**10), count)
        seats = rng.sample(range(100), count)
        details = [
            f"{phone:010d}{rng.choice('MFO')}{rng.randint(0, 99):02d}{seat:02d}"
            for phone, seat in zip(phones, seats)
        ]
        call = f"candidate(details={details!r})"
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
