import random
from datetime import date, timedelta

_STATEMENT_EXAMPLES = (
    "candidate(date='20th Oct 2052')",
    "candidate(date='6th Jun 1933')",
    "candidate(date='26th May 1960')",
)


def generate(seed: int = 0) -> list[str]:
    """Generate valid English dates spanning the original 1900..2100 year bounds."""
    rng = random.Random(seed)
    origin = date(1900, 1, 1)
    boundaries = (
        date(1900, 1, 1),
        date(1900, 12, 31),
        date(2000, 2, 29),
        date(2000, 3, 1),
        date(2100, 1, 1),
        date(2100, 12, 31),
    )
    calls = []
    seen = set()
    for value in boundaries:
        suffix = (
            "th"
            if 11 <= value.day <= 13
            else {1: "st", 2: "nd", 3: "rd"}.get(value.day % 10, "th")
        )
        date_text = f"{value.day}{suffix} {value.strftime('%b')} {value.year}"
        call = f"candidate(date={date_text!r})"
        calls.append(call)
        seen.add(call)
    while len(calls) < 600:
        value = origin + timedelta(
            days=rng.randrange((date(2100, 12, 31) - origin).days + 1)
        )
        suffix = (
            "th"
            if 11 <= value.day <= 13
            else {1: "st", 2: "nd", 3: "rd"}.get(value.day % 10, "th")
        )
        date_text = f"{value.day}{suffix} {value.strftime('%b')} {value.year}"
        call = f"candidate(date={date_text!r})"
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
