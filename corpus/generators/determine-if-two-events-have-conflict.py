import random

_STATEMENT_EXAMPLES = (
    "candidate(event1=['01:15', '02:00'], event2=['02:00', '03:00'])",
    "candidate(event1=['01:00', '02:00'], event2=['01:20', '03:00'])",
    "candidate(event1=['10:00', '11:00'], event2=['14:00', '15:00'])",
)


def generate(seed: int = 0) -> list[str]:
    """Create distinct pairs of valid same-day minute intervals."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    while len(calls) < 600:
        intervals = []
        for _ in range(2):
            start = rng.randrange(24 * 60)
            end = rng.randint(start, 24 * 60 - 1)
            intervals.append(
                [f"{start // 60:02}:{start % 60:02}", f"{end // 60:02}:{end % 60:02}"]
            )
        call = f"candidate(event1={intervals[0]!r}, event2={intervals[1]!r})"
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
