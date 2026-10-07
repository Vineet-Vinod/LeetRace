import random
import datetime


def generate(seed: int = 0) -> list[str]:
    """Dates use ISO format and stay within the supported years, including leap-day boundaries."""
    r = random.Random(seed)
    cases = [
        ("2019-06-29", "2019-06-30"),
        ("2020-01-15", "2019-12-31"),
        ("1971-01-01", "2100-12-31"),
        ("2000-02-28", "2000-03-01"),
    ]
    seen = set(cases)
    base = datetime.date(1971, 1, 1)
    while len(cases) < 600:
        a = base + datetime.timedelta(days=r.randrange(0, 365 * 130))
        b = base + datetime.timedelta(days=r.randrange(0, 365 * 130))
        p = (a.isoformat(), b.isoformat())
        if p not in seen:
            seen.add(p)
            cases.append(p)
    return [f"candidate(date1={a!r}, date2={b!r})" for a, b in cases]
