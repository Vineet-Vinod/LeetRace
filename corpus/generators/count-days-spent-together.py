import random
from datetime import date, timedelta

_STATEMENT_EXAMPLES = (
    "candidate(arriveAlice='08-15', leaveAlice='08-18', arriveBob='08-16', leaveBob='08-19')",
    "candidate(arriveAlice='10-01', leaveAlice='10-31', arriveBob='11-01', leaveBob='12-31')",
)


def generate(seed: int = 0) -> list[str]:
    """Create distinct valid 2022 date intervals with arrival no later than leave."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    origin = date(2022, 1, 1)
    while len(calls) < 600:
        starts = sorted((rng.randrange(365), rng.randrange(365)))
        ends = (rng.randrange(starts[0], 365), rng.randrange(starts[1], 365))
        a0, a1 = (
            (origin + timedelta(days=starts[0])).strftime("%m-%d"),
            (origin + timedelta(days=ends[0])).strftime("%m-%d"),
        )
        b0, b1 = (
            (origin + timedelta(days=starts[1])).strftime("%m-%d"),
            (origin + timedelta(days=ends[1])).strftime("%m-%d"),
        )
        call = f"candidate(arriveAlice={a0!r}, leaveAlice={a1!r}, arriveBob={b0!r}, leaveBob={b1!r})"
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
