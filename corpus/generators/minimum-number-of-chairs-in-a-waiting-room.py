import random

_STATEMENT_EXAMPLES = (
    "candidate(s='EEEEEEE')",
    "candidate(s='ELELEEL')",
    "candidate(s='ELEELEELLL')",
)


def generate(seed: int = 0) -> list[str]:
    """Generate valid entry/exit strings; every exit follows a previous entry."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    while len(calls) < 600:
        pairs = rng.randint(1, 25)
        entries = leaves = pairs
        events: list[str] = []
        occupied = 0
        while entries or leaves:
            if entries and (occupied == 0 or (leaves > 0 and rng.randrange(2))):
                events.append("E")
                occupied += 1
                entries -= 1
            else:
                events.append("L")
                occupied -= 1
                leaves -= 1
        s = "".join(events)
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
