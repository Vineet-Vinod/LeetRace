import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = []
    seen = set()

    def add(**kw):
        a, b = kw["low"], kw["high"]
        assert a.isdigit() and b.isdigit() and a[0] != "0" and b[0] != "0"
        assert 1 <= int(a) <= int(b) < 10**100 and len(a) <= 100 and len(b) <= 100
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kw.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for kw in [{"low": "1", "high": "11"}, {"low": "90", "high": "101"}] + [
        {"low": "1", "high": "9" * 100},
        {"low": "9" * 100, "high": "9" * 100},
        {"low": "1", "high": "1"},
    ]:
        add(**kw)
    while len(calls) < 600:
        mode = len(calls) % 4
        if mode == 0:
            value = rng.randint(1, 9)
            for _ in range(rng.randint(1, 60)):
                digit = value % 10
                value = value * 10 + rng.choice(
                    [d for d in (digit - 1, digit + 1) if 0 <= d <= 9]
                )
            a, b = value, value
        elif mode == 1:
            a = rng.randint(1, 100000)
            b = a + rng.randint(0, 1000)
        else:
            a = rng.randint(1, 10 ** rng.randint(1, 90))
            b = a + rng.randint(0, 10 ** rng.randint(1, 90))
        add(low=str(a), high=str(b))
    return calls
